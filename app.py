from flask import Flask, request, render_template, redirect, url_for, abort

import game
import json

import dbdb



app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    character = game.character(name)
    return render_template('gamestart.html', data=character)




@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        num = request.form['num']
        name = request.form['name']
        print (num,type(num))
        print (name,type(name))
        return "ㅎㅇ {}".format(num)

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
    print(ret[3])
    return render_template('getinfo.html', data=ret)
    #return "번호 : {}, 이름 : {}".format(ret[0], ret[1])

@app.route('/naver')
def naver():
    return redirect('https://www.naver.com')

@app.route('/daum')
def daum():
    return redirect('https://www.daum.net')

@app.route('/move/<a>')
def move(a):
    if a == 'daum':
        return redirect(url_for('daum'))
    elif a == 'naver':
        return redirect(url_for('naver'))
    else:
        abort(404)
@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인하세요", 404

@app.route('/img')
def img():
    return render_template('image.html')

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

@app.route('/method', methods = ['GET   ', 'POST'])
def method():

    if request.method == "GET":
        return "GET 으로 전송이다."
    else:
        num = request.form['num']
        name = request.form['name']
        dbdb.insert_data(num, name)
        return "POST 이다. 학번은:{} 이름은: {}".format(num, name)

if __name__ == '__main__':
    #with app.test_request_context():
    #        print(url_for('daum'))
    app.run(debug=True)
