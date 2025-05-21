from flask import Flask, render_template, request, jsonify , send_from_directory ,abort
import json
import os

app = Flask(__name__)

articles = [
    {"id": 1, "title": "選舉的最大秘密", "content": "票多的贏票少的輸！"},
    {"id": 2, "title": "鮭魚", "content": "我愛吃鮭魚:D"},
    {"id": 3, "title": "php", "content": "php是世界上最棒的語言！ 沒有之一！"}
]


app = Flask(__name__)
FILE_DIRECTORY = './file'  

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_file_in_dir(path):
    if not path:
        # 處理根目錄
        return render_template('index.html', articles=articles)
    
    abs_path = os.path.join(FILE_DIRECTORY, path)
    
    # 檢查路徑是否在允許的目錄內
    if not os.path.abspath(abs_path).startswith(os.path.abspath(FILE_DIRECTORY)):
        abort(403)  # Forbidden
    
    if os.path.isfile(abs_path):
        # 如果是文件，則下載
        dir_path, filename = os.path.split(abs_path)
        return send_from_directory(dir_path, filename, as_attachment=True)
    elif os.path.isdir(abs_path):
        # 如果是目錄，則列出內容
        files = os.listdir(abs_path)
        return render_template('directory.html', files=files, current_path=path)
    else:
        abort(404)  # Not found

@app.route('/my_secret_flag_page', methods=['GET', 'POST'])
def secret_flag():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        with open('secret.json') as f:
            secrets = json.load(f)
        
        if username in secrets and secrets[username] == password:
            with open('flag') as f:
                flag = f.read().strip()
            return render_template('login.html', flag=flag)
        else:
            return render_template('login.html', error="Invalid credentials")
    
    return render_template('login.html')

"""
@app.route('/robots.txt')
def robotstxt():
    return "User-agent: *\nDisallow: /my_secret_flag_page"
"""


@app.route('/.git')
def robotstxt():
    return ""

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=80)