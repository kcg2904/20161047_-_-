from flask import Flask, request, render_template, redirect, url_for, abort, session 
import dbdb 

app = Flask(__name__) 
app.secret_key = b'aaa!111/' 
@app.route('/') 
def index(): 
    return '메인페이지' 
# 로그인 
@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    if request.method == 'GET': 
        return render_template('login1.html') 
    else: 
        id = request.form['id'] 
        pw = request.form['pw'] 
        # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다 
        if id == 'abc' and pw == '1234': 
            session['user'] = id 
            return ''' 
                <script> alert("안녕하세요~ {}님"); 
                location.href="/form" </script> 
                '''.format(id) 
        else: 
            return "아이디 또는 패스워드를 확인 하세요." 
# 로그아웃(session 제거) 
@app.route('/logout') 
def logout(): 
    session.pop('user', None) 
    return redirect(url_for('form')) 

# 로그인 사용자만 접근 가능으로 만들면 
@app.route('/form') 
def form(): 
    if 'user' in session: 
        return render_template('test.html') 
    return redirect(url_for('login')) 
    
@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET': 
        return 'GET 으로 전송이다.' 
    else: 
        id = request.form["id"] 
        pw = request.form["pw"] 
        return redirect(url_for('form'))

if __name__ == '__main__': 
    app.run(debug=True)

