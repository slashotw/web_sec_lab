from flask import Flask, redirect, url_for, render_template,request,flash,session,make_response
import random
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html") , 200 , [("half_flag",r"flag{u_found_")]



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)