from flask import Flask, render_template, request, session
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

flag1 = r'flag{thats_too_easy}'
flag2 = r'flag{why_u_attack_my_database_qqq}'

BLACKLIST = ['alter', 'begin', 'cast', 'create', 'cursor', 'distinct', 'declare', 'delete', 'drop', 'end',
             'exec', 'execute', 'fetch', 'insert', 'kill', 'sys', 'sysobjects',
             'syscolumns', 'table', 'update']

@app.before_first_request
def sqlite_generate():
    con = sqlite3.connect('main.db')
    cursor = con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS user 
    (id INT PRIMARY KEY NOT NULL,
    username TEST NOT NULL,
    password TEST NOT NULL);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS flag_is_here
    (id INT PRIMARY KEY NOT NULL,
    flagcol TEST NOT NULL,
    meow TEST NOT NULL);''')

    cursor.execute("SELECT * FROM user WHERE username='admin'")
    if not cursor.fetchone():
        cursor.execute(f"INSERT INTO user (id, username, password) VALUES (0, 'admin', '{os.urandom(10).hex()}')")

    cursor.execute(f"SELECT * FROM flag_is_here WHERE flagcol='{flag2}'")
    if not cursor.fetchone():
        cursor.execute(f"INSERT INTO flag_is_here (id, flagcol, meow) VALUES (0, '{flag2}', 'sqlmap is cool :D')")

    con.commit()
    con.close()

def checklogin(ac, pw):
    if any(word in ac.lower() for word in BLACKLIST) or any(word in pw.lower() for word in BLACKLIST):
        return "WARNING: DO NOT TRY TO CHANGE OR REWRITE THE FLAG"

    try:
        con = sqlite3.connect('main.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM user WHERE username='{ac}' AND password='{pw}'")
        res = cur.fetchone()
        con.close()

        if res:
            if res[1] == 'admin':
                return 1
        else:
            return "Login failed"
    except Exception as err:
        return str(err)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        result = checklogin(user, password)
        if result ==1 :
            return flag1 
        else:
            return render_template("index.html", result=result)
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=80)