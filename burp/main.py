from flask import Flask, redirect, url_for, render_template,request,flash,session,make_response,render_template_string
import json
app = Flask(__name__)



@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST" :
        try :
            q = request.form["score"]
            if int(q) >= 1000000 :
                return r"flag{cyberluck_get_u_pass_midexam}" 
            else :
                return render_template("index.html",alert="陰德不夠...")
        except :
           return r"err"
    else :
        return render_template("index.html")
    



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)