from flask import Flask, request, render_template, redirect, url_for, abort, session
from random import *
import game
import json
import os

import dbdb

app = Flask(__name__)

app.secret_key = b'aaa!111/'

@app.route('/')
def index():
    return render_template('main1.html')

@app.route('/end',methods = ['GET', 'POST'])
def end():
    if request.method == 'GET':
        return redirect(url_for("index"))
    else :
        ck = request.form['chk']
        random = randint(1,3)
        vs = ""
        prin = ""
        if random == 1:
            vs = "가위" 
        elif vs == 2:
            vs = "바위"
        elif random == 3: 
            vs = "보"
        dbdb.create_data()
        if ck == "보" and vs == "가위":
            prin = "패배"
            dbdb.in_data('null','패배')
        elif ck == "가위" and vs == "보":
            prin = "승리"
            dbdb.in_data('null','승리')
        elif ck == "바위" and vs == "보":
            prin = "패배"
            dbdb.in_data('null','패배')
        elif ck == "보" and vs == "바위":
            prin = "승리"
            dbdb.in_data('null','승리')
        elif ck == "가위" and vs == "바위":
            prin = "패배"
            dbdb.in_data('null','패배')
        elif ck == "바위" and vs == "가위":
            prin = "승리"
            dbdb.in_data('null','승리')
        else :
            prin = "비김"
            dbdb.in_data('null','비김')

        
        return render_template('end.html',data=prin)

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
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        ret = dbdb.select_user(id, pw)
 # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다 
        if ret != None: 
        
            session['user'] = id 
            return redirect(url_for('index'))
        else: 
            return redirect(url_for('login'))
# 로그아웃(session제거)
@app.route('/logout')
def logout():
    if os.path.isfile('data.db'):
         os.remove('data.db')
    session.pop('user', None)

    return redirect(url_for('index'))

# 로그인 사용자만 접근 가능으로 만듬
@app.route('/form')
def form():
    if 'user' in session:
        return redirect(url_for('getinfo'))
    return redirect(url_for('login'))
@app. route('/gamestart')
def gamestart():
    if 'user' in session:
        a = randint(1,5)
        if a == 1 :
            return render_template('tung.html')
        elif a == 2 :
            return render_template('dola.html')
        elif a == 3 :
            return render_template('jin.html')
        elif a  == 4 :
            return render_template('bi.html')
        else :
            return render_template('is.html')
    return redirect(url_for('login'))

@app.route('/getinfo')
def getinfo():
    if 'user' in session:
        ret = dbdb.select_all()
        return render_template('getinfo.html', data=ret)
    return redirect(url_for('login'))

@app.route('/gamedata')
def gamedata():
    if 'user' in session:
        ret = dbdb.select_data()
        return render_template('gamedata.html', data=ret)
    return redirect(url_for('login'))


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
    app.run(debug=True)
