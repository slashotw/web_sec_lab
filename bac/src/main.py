from flask import Flask, redirect, url_for, render_template, request, make_response, jsonify
import json
import os
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
flag = r"flag{p0st1ng_sh1t}"


BLOG_FILE = 'blog_posts.json'
DEFAULT_POSTS = [
    {"title": "延邊刺客", "content": """我個人認為
義大利麵就應該拌 42 號混泥土
因為這個螺絲釘的長度很容易直接影響到挖掘機的扭矩

你往裡砸的時候
一瞬間他就會產生大量的高能蛋白
俗稱 UFO，會嚴重影響經濟的發展
以至於對整個太平洋和充電器的核污染

再或者說
透過這勾股定理
很容易推斷出人工飼養的東條英機
他是可以捕獲野生的三角函數

所以說
不管這秦始皇的切面是否具有放射性
川普的 N 次方是否有沈澱物
都不會影響到沃爾瑪跟維爾康在南極匯合

你往裡砸的時候
一瞬間他就會產生大量的高能蛋白
俗稱 UFO，會嚴重影響經濟的發展
以至於對整個太平洋和充電器的核污染

再或者說
透過這勾股定理
很容易推斷出人工飼養的東條英機
他是可以捕獲野生的三角函數"""},
    {"title": "☝️ 😐👇", "content": "雨停滯天空之間 ☝️ 😐👇 像淚在眼眶盤旋👇😐☝️ 這也許是最後一 ✋ 🤚 😐 次見面😐 ✋ 🤚"},
    {"title": "夜店", "content": "我第一次去夜店唯一一次，只進去了3分鐘，我是被同學綁去的 ，剛進去就受不了，那裡沒有書，沒有考卷，沒有老師，太吵雜了，並不適合我，我只想好好學習，考取功名，報效國家！"},
    {"title": "三個步驟教妳攻掠資工男", "content": "1. 首先妳要知道資工男是全世界最好騙的男生族群 因為平時讀書或是寫程式很少聽到謊言 教授不爽不會裝好臉色 所以資工男是沒有辨別謊言的能力的 基本上妳說的一字一句他都會相信 特別如果又是他想聽的 所以甜言蜜語是非常必要的 這邊提供一些關鍵字 範例：「今天你又沒有刮鬍子齁」「你最近是不是在趕程設作業死線看起來很憔悴」基本上只要講出這個資工男就會高潮： 「你怎麼知道！」他就會覺得妳有看到他的細節2. 資工男的生活非常的無聊 每天就是不斷讀書和刷OJ 所以千萬別問他最近發生的事 那只是讓彼此都痛苦 因為他會講一堆奇怪名詞聽都聽不懂 真的很解 最好的分享方式就是把他當成Chat gpt 妳講妳想講的事情 他一定秒回妳3. 資工男長期生存在壓力大的環境 所以他們找存在的方式就是從女性身上得到安慰 甚至是自己存在的價值 多給資工男一些肯定和安慰他們很容易就會對妳產生依賴 範例：「哇你寫這些遞迴是什麼呀可以教我嗎」「你的演算法速度好快喔 好man哦」這時候資工男就會覺得自己還是很有用處的資工男很多都沒什麼經驗的 什麼技巧都不會學會之後謹慎使用 因為長期沒碰過女生 所以每個都是純愛戰士 大部分人都很專情 保證可以碰但是整天在把妹妹的那種奇形種不可以碰"},
    {"title": "dddd懂得都懂", "content": "關於這個事，我簡單說兩句，你明白就行，總而言之，這個事呢，現在就是這個情況，具體的呢，大家也都看得到，也得出來說那麼幾句，可能，你聽的不是很明白，但是意思就是那麼個意思，不知道的你也不用去猜，這種事情見得多了，我只想說懂得都懂，不懂的我也不多解釋，畢竟自己知道就好，細細品吧。你們也別來問我怎麼了，利益牽扯太大，說了對你我都沒好處，當不知道就行了，其餘的我只能說這裡面水很深，牽扯到很多東西。詳細情況你們自己是很難找的，所以我只能說懂得都懂。不懂的人永遠不懂，所以大家最好是不懂就不要去了解,懂太多不好。"},
    {"title": "糟了", "content": "糟了，這是從左心室開始，新鮮的動脈血液從左心室經體動脈被壓出，經過全身組織與組織各處完成氧氣與二氧化碳的交換後由動脈血變為靜脈血，經由下腔靜脈回到右心房，再進入右心室，之後血液由右心室射出經肺動脈流到肺毛細血管，在此與肺泡進行氣體交換，吸收氧氣並排出二氧化碳，缺氧血變為充氧血；然後經肺靜脈流回左心房的感覺！ ！ ！"},
    {"title": "這我", "content": "一个个的，不知道慌啥，都是老交易员了，30%的回调是在预期内的，再说平常控制仓位注意风险都是老生常谈了不用我多说了吧。我今天一天都没打开账户，短期盈亏不要影响长期判断，是一个成熟交易员的心理素质。我现在打开账户看看仓位你就知道了，哎我操，我仓位呢?"}
]

def load_posts():
    if os.path.exists(BLOG_FILE):
        with open(BLOG_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_POSTS

def save_posts(posts):
    with open(BLOG_FILE, 'w') as f:
        json.dump(posts, f)


def clear_posts():
    while True:
        time.sleep(300)  # 每分鐘執行一次
        save_posts(DEFAULT_POSTS)
        print("===clear posts===")

# 啟動清理文章的背景任務
threading.Thread(target=clear_posts, daemon=True).start()


@app.route('/')
def index():
    posts = load_posts()
    role = request.cookies.get('role')
    resp = make_response(render_template('index.html', posts=posts, role=role))
    if not request.cookies.get('role'):
        resp.set_cookie(key='role',value= 'guest')
    return resp

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    role = request.cookies.get('role')
    if role == 'admin' :
        if request.headers.get('X-Forwarded-For') =='localhost' or request.headers.get('X-Forwarded-For') == '127.0.0.1' :
            if request.method == 'POST':
                title = request.form['title']
                content = request.form['content']
                if title and content:
                    posts = load_posts()
                    posts.append({"title": title, "content": content})
                    save_posts(posts)
                    print(posts)
                    return redirect(url_for('index'))
            posts = load_posts()
            return render_template('admin.html', posts=posts, role=role,flag=flag)

    return "無權限訪問或非本地訪問" 


if __name__ == "__main__":
    save_posts(DEFAULT_POSTS)
    app.run(debug=False,host="0.0.0.0",port=80)