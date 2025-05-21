from flask import Flask, render_template, jsonify
import base64

app = Flask(__name__)

FLAG = r"CTF{i_hacked_myself}"

@app.route('/')
def index():
    encoded_flag = base64.b64encode(FLAG.encode()).decode()
    return render_template('index.html', encoded_flag=encoded_flag)

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=80)