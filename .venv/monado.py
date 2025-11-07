from flask import Flask, render_template, request, session, redirect, url_for, current_app, g, jsonify
from werkzeug.utils import secure_filename
import sqlite3, os
from pathlib import Path
from waitress import serve
# flask --app C:\Users\levasseurt26\monado\.venv\monado.py run --host="0.0.0.0" --port="80" --debug --with-threads
# flask --app C:\Users\levasseurt26\monado\.venv\monado.py run --host="0.0.0.0"

message = "none"
username = ""
say = Path(r"C:/Users/levasseurt26/monado/.venv/log.txt")
users = "/database.db"

app = Flask(__name__)
app.secret_key = b'SIGMA'
UPLOAD_FOLDER = os.path.join('static', 'img')
app.config[UPLOAD_FOLDER] = UPLOAD_FOLDER

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
        db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('database.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

init_db()

@app.route("/", methods=["POST", "GET"])
def welcome():
    if 'username' not in session:
        if request.method == "POST":
            db = get_db()
            try:
                if str((db.execute(f"SELECT pass FROM user WHERE username='{request.form['username']}';").fetchone())[0]) == str(request.form['password']):
                    print(str((db.execute(f"SELECT pass FROM user WHERE username='{request.form['username']}';").fetchone())[0]))
                    session['username'] = request.form['username']
                    return redirect(url_for('home'))
                else:
                    print("Wrong Password!")
            except Exception:
                print("username does not exist")
        return render_template("welcome.html")
    else:
        return redirect(url_for('chat'))

@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        db = get_db()
        if (db.execute(f"SELECT username FROM user WHERE username='{request.form['username']}';").fetchone()) is None:
            db.execute(f'INSERT INTO user (username, avatar, pass) VALUES (?, ?, ?);', (request.form['username'], url_for('static', filename='img/default_avatar.png'), request.form['password']))
            db.execute(f"INSERT INTO profilepage (username, biography) VALUES (?, ?);", (request.form['username'], "I'm new!"))
            db.commit()
            return redirect(url_for('welcome'))
        else:
            print("That username is already taken!")
    return render_template('accountcreate.html')

# === Sign in ^^^ ============= Home/Chatting ___ ========================================================================================================================================================

@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html", user=session['username'])

@app.route("/chat", methods=["POST", "GET"])
def chats():
    return render_template("chats.html", user=session['username'])

@app.route("/chat/<currentchat>", methods=["POST", "GET"])
def chat(currentchat):
    global message
    #if 'username' not in session:
        #return redirect(url_for('welcome'))
    if request.method == "POST":
        message = request.form["message"]
        image = request.files["image"]
        print("1", str(image))
        db = get_db()
        if image:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config[UPLOAD_FOLDER], filename))
                print("2", filename)
                print("3", str(url_for('static', filename='img/' + str(filename))))
                image = str(url_for('static', filename='img/' + str(filename)))
        else:
            image = ""
        print("4", image)
        db.execute(f"INSERT INTO chatlog_{currentchat} (username, content, img_attachment) VALUES (?,?,?);", (session['username'], message, image))
        db.commit()
        avatar = db.execute(f"SELECT avatar FROM user WHERE username='{session['username']}'").fetchone()[0]
        print(avatar)
        print(image)
        print(message)
        with open(say, "a") as f:
            f.write("\n" + session['username'] + ": " + message)
        data = {
            "user": session['username'],
            "avatar": avatar,
            "message": message,
            "image": image
        }
        return jsonify(data)
    return render_template("message.html", say=say.read_text(), user=session['username'], message=message, currentchat=currentchat)

@app.route("/chatlog/<currentchat>", methods=["POST", "GET"])
def test(currentchat):
    if request.method == "POST":
        db = get_db()
        sdata = []
        size = db.execute(f"SELECT rowid FROM chatlog_{currentchat} ORDER BY rowid DESC limit 1").fetchone()[0]
        for i in range(size, 0, -1):
            namedata = db.execute(f"SELECT username FROM chatlog_{currentchat} WHERE rowid = {size - (i-1)}").fetchone()[0]
            avatardata = db.execute(f"SELECT avatar FROM user WHERE username = '{namedata}'").fetchone()[0]
            contentdata = db.execute(f"SELECT content FROM chatlog_{currentchat} WHERE rowid = {size - (i-1)}").fetchone()[0]
            imagedata = db.execute(f"SELECT img_attachment FROM chatlog_{currentchat} WHERE rowid = {size - (i-1)}").fetchone()[0]
            data = {"username":namedata, "avatar":avatardata, "content":contentdata, "image":imagedata}
            sdata.append(data)
        print(sdata)
        return jsonify(sdata)
    else:
        return redirect(url_for('home'))

@app.route("/profile/<username>", methods=["POST", "GET"])
def profile(username):
    db = get_db()
    print(username)
    print(session['username'])
    if username == session['username']:
        if request.method == "POST":
            newavatar = request.files["avatar_upload"]
            biography = request.form["biographyupdate"]
            if newavatar:
                filename = secure_filename(newavatar.filename)
                newavatar.save(os.path.join(app.config[UPLOAD_FOLDER], filename))
                print(filename)
                print(str(url_for('static', filename='img/' + str(filename))))
                db.execute(f"UPDATE user SET avatar = '{str(url_for('static', filename='img/' + str(filename)))}' WHERE username='{session['username']}'")
            if biography != "":
                db.execute(f"UPDATE profilepage SET biography = ? WHERE username = ?", (biography, username))
            db.commit()
        print(session['username'])
        biography = db.execute(f"SELECT biography FROM profilepage WHERE username='{session['username']}'").fetchone()[0]
        grab = db.execute(f"SELECT avatar FROM user WHERE username='{session['username']}'").fetchone()[0]
        avatar = grab if grab != None else url_for('static', filename='img/default_avatar.png')
        return render_template('profile.html', currentuser=session['username'], user=username, avatar=avatar, biography=biography, edit=True)
    else:
        biography = db.execute(f"SELECT biography FROM profilepage WHERE username='{username}'").fetchone()[0]
        grab = db.execute(f"SELECT avatar FROM user WHERE username='{username}'").fetchone()[0]
        avatar = grab if grab != None else url_for('static', filename='img/default_avatar.png')
        return render_template('profile.html', currentuser=session['username'], user=username, avatar=avatar, biography=biography, edit=False)

@app.route("/friends", methods=["POST", "GET"])
def friends():
    db = get_db()
    return render_template("friends.html", user=session['username'])

@app.route("/friends/find", methods=["POST", "GET"])
def findfriends():
    if request.method == "POST":
        db = get_db()
        data = {}
        usercheck = request.form['friendsearch']
        namedata = db.execute(f"SELECT username FROM user WHERE username = '{usercheck}'").fetchone()[0]
        if namedata != None:
            avatardata = db.execute(f"SELECT avatar FROM user WHERE username = '{namedata}'").fetchone()[0]
            data = {"username":namedata, "avatar":avatardata}
            print("RETURNING!")
            return jsonify(data)
        else:
            pass
    else:
        return redirect(url_for('friends'))

@app.route("/goodbye", methods=["POST", "GET"])
def goodbye():
    session.pop('username', None)
    return redirect(url_for('welcome'))

@app.route("/nuke", methods=["POST", "GET"])
def nuke():
    db = get_db()
    db.execute("DROP TABLE IF EXISTS chatlog_1")
    session.pop('username')
    db.commit()
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    #serve(app, host='0.0.0.0', port=5588)
    app.run(host='0.0.0.0', port=5588, debug=True)

""" Someday Do's
- Hash Passwords
"""