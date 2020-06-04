from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/main')
def index():
    return render_template('login1.html')
@app.route('/new')
def new():
    return render_template('new1.html')
@app.route('/method', methods = ['GET   ', 'POST'])
def method():
    user = request.form['user']
    pw = request.form['pw']
    if user == 'abc' and pw == '1234':
        i = "임시 아이디와 비  밀번호가 맞습니다. 입력한 아이디와 비밀번호({}, {})".format(user, pw)
        return i
    else:
        i = "임시 아이디와 비밀번호가 아닙니다. 입력한 아이디와 비밀번호({}, {})".format(user, pw)
        return i

if __name__ == '__main__':
    app.run(debug=True)
