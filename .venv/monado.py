from flask import Flask, render_template, request, session, redirect, url_for, current_app, g, jsonify
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
import sqlite3, os, json, datetime
from pathlib import Path
from waitress import serve
from datetime import datetime
# flask --app C:\Users\levasseurt26\monado\.venv\monado.py run --host="0.0.0.0" --port="80" --debug --with-threads
# flask --app C:\Users\levasseurt26\monado\.venv\monado.py run --host="0.0.0.0"
# python monado.py

message = "none"
username = ""
say = Path(r"C:/Users/levasseurt26/monado/.venv/log.txt")
suggbox = Path(r"C:/Users/levasseurt26/monado/.venv/suggestions.txt")
users = "/database.db"

app = Flask(__name__)
app.secret_key = b'SIGMA'
UPLOAD_FOLDER = os.path.join('static', 'img')
app.config[UPLOAD_FOLDER] = UPLOAD_FOLDER
bcrypt = Bcrypt(app)
socketio = SocketIO(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db', timeout=10)
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
                if bcrypt.check_password_hash(str((db.execute(f"SELECT pass FROM user WHERE username='{request.form['username']}';").fetchone())[0]), str(request.form['password'])):
                    print(str((db.execute(f"SELECT pass FROM user WHERE username='{request.form['username']}';").fetchone())[0]))
                    session['username'] = request.form['username']
                    db.execute(f"UPDATE user SET active = True WHERE username = '{session['username']}'")
                    db.commit()
                    return redirect(url_for('home'))
                else:
                    print("Wrong Password!")
            except Exception:
                print("username does not exist")
        return render_template("welcome.html")
    else:
        return redirect(url_for('home'))

@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        db = get_db()
        if (db.execute(f"SELECT username FROM user WHERE username='{request.form['username']}';").fetchone()) is None:
            db.execute(f'INSERT INTO user (username, avatar, pass) VALUES (?, ?, ?);', (request.form['username'], url_for('static', filename='img/default_avatar.png'), bcrypt.generate_password_hash(request.form['password']).decode('utf-8')))
            db.execute(f"INSERT INTO profilepage (username, biography) VALUES (?, ?);", (request.form['username'], "I'm new!"))
            db.execute(f"CREATE TABLE IF NOT EXISTS {request.form['username']}_friends (friend TEXT);")
            db.execute(f"CREATE TABLE IF NOT EXISTS {request.form['username']}_chats (id INTEGER);")
            db.commit()
            return redirect(url_for('welcome'))
        else:
            print("That username is already taken!")
    return render_template('accountcreate.html')

# === Sign in ^^^ ============= Home/Chatting ___ ========================================================================================================================================================

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html", user=session['username'])

@app.route("/chat", methods=["POST", "GET"]) # <--------------------------- Working on this =============== Ideally do a lot of this code over since the way I've tried to do this is pretty busted
def chats():
    if request.method == "POST":
        db = get_db()
        data = request.json
        if data["type"] == "NewChat":
            print("Working")
            newback = ",".join(data['addwho'])
            if db.execute(f"SELECT id FROM privchats WHERE backname='{newback}'").fetchone() == None:
                db.execute(f"INSERT INTO privchats (backname) VALUES ('{newback}')")
                newid = db.execute(f"SELECT id FROM privchats WHERE backname='{newback}'").fetchone()[0]
                db.execute(f"CREATE TABLE IF NOT EXISTS chatlog_{newid} (id INTEGER AUTO_INCREMENT PRIMARY KEY, username TEXT, senddate DATE, sendtime TIME, content TEXT, img_attachment IMAGE)")
                for user in data["addwho"]:
                    print(user)
                    db.execute(f"INSERT INTO {user}_chats (id) VALUES ({newid})")
                db.commit()
                return jsonify({"Status":"Success", "Backname":data['addwho'], "ID":newid})
            else:
                return jsonify({"Status":"Exists"})
        if data["type"] == "LoadChats":
            sdata = []
            size = db.execute(f"SELECT rowid FROM {session['username']}_chats ORDER BY rowid DESC limit 1").fetchone()[0]
            for i in range(size, 0, -1):
                currentchat = db.execute(f"SELECT id FROM {session['username']}_chats WHERE rowid = {size - (i-1)}").fetchone()[0]
                namedata = db.execute(f"SELECT chatname FROM privchats WHERE id = currentchat").fetchone()[0]
                avatardata = db.execute(f"SELECT backname FROM privchats WHERE id = currentchat").fetchone()[0]
                data = {"Chatname":namedata, "Backname":avatardata}
                sdata.append(data)
            print(sdata)
            return jsonify(sdata)
    else:
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
        db.execute(f"INSERT INTO chatlog_{currentchat} (username, senddate, sendtime, content, img_attachment) VALUES (?,?,?,?,?);", (session['username'], datetime.now().strftime("%D"), datetime.now().strftime("%H:%M:%S"), message, image))
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
            "image": image,
            "date": datetime.now().strftime("%D"),
            "time": datetime.now().strftime("%H:%M:%S")
        }
        socketio.emit('messageback', data)
        return jsonify(data)
    return render_template("message.html", say=say.read_text(), user=session['username'], message=message, currentchat=currentchat, ping=url_for('static', filename='audio/ping.mp3'))

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
            datedata = db.execute(f"SELECT senddate FROM chatlog_{currentchat} WHERE rowid = {size - (i-1)}").fetchone()[0]
            timedata = db.execute(f"SELECT sendtime FROM chatlog_{currentchat} WHERE rowid = {size - (i-1)}").fetchone()[0]
            data = {"username":namedata, "avatar":avatardata, "content":contentdata, "image":imagedata, "date":datedata, "time":timedata}
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
            print(namedata)
            print("RETURNING!")
            return jsonify(data)
        else:
            pass
    else:
        return redirect(url_for('friends'))

@app.route("/friends/add", methods=["POST", "GET"])
def addfriends():
    if request.method == "POST":
        db = get_db()
        data = request.json
        if data["type"] == "Send":
            print(db.execute(f"SELECT COUNT(1) FROM friendrequests WHERE sender='{session['username']}' AND receiver='{data['fname']}'").fetchone()[0])
            if db.execute(f"SELECT COUNT(1) FROM friendrequests WHERE sender='{session['username']}' AND receiver='{data['fname']}'").fetchone()[0] > 0:
                print("Request Already Sent!")
                return jsonify({"Status":"Fail"})
            else:
                db.execute(f"INSERT INTO friendrequests (sender, receiver) VALUES (?, ?);", (session['username'], data['fname']))
                db.commit()
                print("SENT!")
                return jsonify({"Status":"Success"})
        elif data["type"] == "Rescind":
            db.execute(f"DELETE FROM friendrequests WHERE sender='{session['username']}' AND receiver='{data['fname']}'")
            db.commit()
            print("REMOVED")
            return jsonify({"Status":"Success"})
        elif data["type"] == "Accept":
            db.execute(f"INSERT INTO {session['username']}_friends (friend) VALUES ('{data['fname']}')")
            db.execute(f"INSERT INTO {data['fname']}_friends (friend) VALUES ('{session['username']}')")
            db.execute(f"DELETE FROM friendrequests WHERE sender='{data['fname']}' AND receiver='{session['username']}'")
            db.commit()
            print(db.execute(f"SELECT friend FROM {session['username']}_friends").fetchone()[0])
            return jsonify({"Status":"Success"})
        elif data["type"] == "Deny":
            db.execute(f"DELETE FROM friendrequests WHERE sender='{data['fname']}' AND receiver='{session['username']}'")
            db.commit()
            print("DENIED")
            return jsonify({"Status":"Success"})
        elif data["type"] == "List":
            outdata = []
            indata = []
            fridata = []
            sdata = []
            if db.execute(f"SELECT COUNT(1) FROM friendrequests").fetchone()[0] > 0:
                outsize = db.execute(f"SELECT rowid FROM friendrequests ORDER BY rowid DESC limit 1").fetchone()[0]
                for i in range(outsize, 0, -1):
                    senderdata = db.execute(f"SELECT sender FROM friendrequests WHERE rowid = {outsize - (i-1)}").fetchone()[0]
                    receiverdata = db.execute(f"SELECT receiver FROM friendrequests WHERE rowid = {outsize - (i-1)}").fetchone()[0]
                    if senderdata == session['username']:
                        avatardata = db.execute(f"SELECT avatar FROM user WHERE username = '{receiverdata}'").fetchone()[0]
                        data = {"username":receiverdata, "avatar":avatardata}
                        outdata.append(data)
                    elif receiverdata == session['username']:
                        avatardata = db.execute(f"SELECT avatar FROM user WHERE username = '{senderdata}'").fetchone()[0]
                        data = {"username":senderdata, "avatar":avatardata}
                        indata.append(data)
            size = db.execute(f"SELECT rowid FROM {session['username']}_friends ORDER BY rowid DESC limit 1").fetchone()
            if size != None:
                size = size[0]
            else:
                size = 0
            for i in range(size, 0, -1):
                namedata = db.execute(f"SELECT friend FROM {session['username']}_friends WHERE rowid = {size - (i-1)}").fetchone()[0]
                avatardata = db.execute(f"SELECT avatar FROM user WHERE username = '{namedata}'").fetchone()[0]
                IsActive = db.execute(f"SELECT active FROM user WHERE username = '{namedata}'").fetchone()[0]
                activedata = "Online" if IsActive == True else "Offline"
                data = {"username":namedata, "avatar":avatardata, "active":activedata}
                fridata.append(data)
            sdata.append(outdata)
            sdata.append(indata)
            sdata.append(fridata)
            print(sdata)
            return jsonify(sdata)
        elif data["type"] == "Unfriend":
            db.execute(f"DELETE FROM {session['username']}_friends WHERE friend='{data['fname']}'")
            db.execute(f"DELETE FROM {data['fname']}_friends WHERE friend='{session['username']}'")
            db.commit()
            return jsonify({"Status":"Success"})
    else:
        return redirect(url_for('friends'))

@app.route("/worlds", methods=["POST", "GET"])
def worlds():
    db = get_db()
    return render_template("worlds.html", user=session['username'])

@app.route("/suggestion", methods=["POST", "GET"])
def suggestion():
    db = get_db()
    if request.method == "POST":
        idea = request.form["idea"]
        db.execute(f"INSERT INTO suggestions (user, idea) VALUES ('{session['username']}', '{idea}')")
        with open(suggbox, "a") as f:
            f.write("\n" + session['username'] + ": " + idea)
    if session['username'] == "Almighty":
        return render_template("suggestion.html", user=session['username'], box=suggbox.read_text())
    else:
        return render_template("suggestion.html", user=session['username'], box="")


@app.route("/goodbye", methods=["POST", "GET"])
def goodbye():
    db = get_db()
    db.execute(f"UPDATE user SET active = False WHERE username = '{session['username']}'")
    db.commit()
    session.pop('username', None)
    return redirect(url_for('welcome'))

@app.route("/nuke", methods=["POST", "GET"])
def nuke():
    db = get_db()
    db.execute("DROP TABLE IF EXISTS chatlog_1")
    db.execute("DROP TABLE IF EXISTS friendrequests")
    db.execute("DROP TABLE IF EXISTS user")
    db.execute("DROP TABLE IF EXISTS privchats")
    session.pop('username')
    db.commit()
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    #serve(app, host='0.0.0.0', port=5588)
    app.run(host='0.0.0.0', port=5588, debug=True)

""" Someday Do's
- Hash Passwords
"""