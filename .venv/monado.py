from flask import Flask, render_template, request, session, redirect, url_for
from pathlib import Path
from waitress import serve
# flask --app C:\Users\levasseurt26\monado\.venv\monado.py run --host="0.0.0.0" --port="80" --debug --with-threads

message = ""
username = ""
say = Path(r"C:/Users/levasseurt26/monado/.venv/log.txt")

app = Flask(__name__)
app.secret_key = b'SIGMA'

@app.route("/", methods=["POST", "GET"])
def welcome():
    if 'username' not in session:
        if request.method == "POST":
            session['username'] = request.form["username"]
            return redirect(url_for('chat'))
        return render_template("welcome.html")
    else:
        return redirect(url_for('chat'))

@app.route("/chat", methods=["POST", "GET"])
def chat():
    print(say.read_text())
    #if 'username' not in session:
        #pass
    if request.method == "POST":
        message = request.form["message"]
        with open("log.txt", "a") as f:
            f.write("\n" + session['username'] + ": " + message)
    return render_template("message.html", say=say.read_text(), user=session['username'])

@app.route("/goodbye", methods=["POST", "GET"])
def goodbye():
    session.pop('username', None)
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    #serve(app, host='0.0.0.0', port=5588)
    app.run(host='0.0.0.0', port=5588, debug=True)