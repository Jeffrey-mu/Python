from flask import Flask, url_for, render_template, request

app = Flask(__name__)
# 静态文件 只要在你的包中或模块旁边创建一个名为 static 的文件夹
@app.route('/')
def hello_world():
    return 'welcome flaskApp, Hello World!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        if (request.form['username'] and request.form['password']):
            return 'login success'
        else:
            error = 'Invalid username/password'
    # the code below this is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    # 动态地构造 URL 的特定部分


@app.route('/user/<username>')
def user(username):
    return 'User %s' % username
# 重定向行为


@app.route('/projects/')
def projects():
    return 'The project page'

# HTTP方法
@app.route('/about', methods=['GET', 'POST'])
def about():
    return 'The about page'

if __name__ == '__main__':
    # app.run()
    # 调试模式  在代码修改的时候服务器能够自动加载
    app.debug = True
    # 或者 app.run(debug=True)
    app.run(host='0.0.0.0')
