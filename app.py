from flask import Flask, request, render_template, redirect, url_for, abort, session

import game
import json

import dbdb

app = Flask(__name__)

app.secret_key = b'aaa!111/'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/hello/<name>')
def hellovar(name):
    character = game.character(name)
    return render_template('gamestart.html', data=character)

#회원가입
@app.route('/join', methods = ['GET', 'POST'])
def join():
    if request.method == "GET":
        return render_template('join.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        ret = dbdb.ckeck_id(id)
        if ret != None: 
            return '''
            <script> 
            alert('다른 아이디를 사용하세요');
            location.href="/join" 
            </script> 
            '''
        dbdb.insert_data(id,pw,name)
        return redirect(url_for('login'))

#  로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login1.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        ret = dbdb.select_user(id, pw)
        print(ret)
 # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다 
        if ret != None: 
        
            session['user'] = id 
            return ''' 
            <script> alert("안녕하세요~ {}님");
            location.href="/form" 
            </script> 
            '''.format(ret[2]) 
        else: 
            return "아이디 또는 패스워드를 확인 하세요."
# 로그아웃(session제거)
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('form'))

# 로그인 사용자만 접근 가능으로 만듬
@app.route('/form')
def form():
    if 'user' in session:
        return redirect(url_for('getinfo'))
    return redirect(url_for('login'))



##@app.route('/gamestart')
#def gamestart():
    #with open("static/save.txt", "r", encoding='utf-8') as f:
     #   data = f.read()
      #  character = json.loads(data)
       # print(character['items'])
    #return "{} 이 {}아이템을 사용 해서 이겼다.".format(character["name"], character["itmes"])

@app.route('/getinfo')
def getinfo():
    ret = dbdb.select_all()
    print(ret)
    return render_template('getinfo.html', data=ret)
    #return "번호 : {}, 이름 : {}".format(ret[0], ret[1])

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인하세요", 404

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character["items"])
        return "{} 이 {}아이템을 사용 해서 이겼다.".format(character["name"], character["items"][0])
    elif num == 2:
        return "진구"
    else:
        return "없는 캐릭터 입니다." 

@app.route('/method', methods = ['GET', 'POST'])
def method():
    if request.method == "GET":
        return "GET 으로 전송이다."
    else:
        id = request.form['id']
        name = request.form['name']
        with open("static/save.txt","w", encoding='utf-8') as f:
            f.write("%s,%s" % (id, name))
        return "POST 이다. 학번은:{} 이름은: {}".format(id, name)
if __name__ == '__main__':
    #with app.test_request_context():
    #        print(url_for('daum'))
    app.run(debug=True)
