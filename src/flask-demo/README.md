# 快速入门
## 一个最小的应用
一个最小的应用看起来像这样:
```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```
## 外部可见服务器
当你运行服务器，你会注意到它只能从你自己的计算机上访问，网络中其它任何的地方都不能访问。 这是因为默认情况下，调试模式，应用中的一个用户可以执行你计算机上的任意 Python 代码。

如果你关闭 debug 或者信任你所在网络上的用户，你可以让你的服务器对外可用，只要简单地改变方法 run() 的调用像如下这样:
```py
app.run(host='0.0.0.0')
```
这让你的操作系统去监听所有公开的 IP。

## 调试模式
run() 方法是十分适用于启动一个本地开发服务器，但是你需要在修改代码后手动重启服务器。 这样做并不好，Flask 能做得更好。如果启用了调试支持，在代码修改的时候服务器能够自动加载， 并且如果发生错误，它会提供一个有用的调试器。

有两种方式开启调式模式。一种是在应用对象上设置标志位:
```py
app.debug = True
app.run()
```
或者作为 run 的一个参数传入:
```py
app.run(debug=True)
```
两种方法效果是一样的。
## 路由
现代 Web 应用程序有优雅的 URLs。这能够帮助人们记住 URLs，这点在面向使用慢网络连接的移动设备的应用上有用。 如果用户不必通过点击首页而直接访问想要的页面，很可能他们会喜欢这个页面而且下次再次访问。

正如上面所说， **route()** 装饰器是用于把一个函数绑定到一个 URL 上。这有些基本的例子:

```py
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
```
但是不仅如此！你可以动态地构造 URL 的特定部分，也可以在一个函数上附加多个规则。
##  变量规则

为了给 URL 增加变量的部分，你需要把一些特定的字段标记成 <variable_name>。这些特定的字段将作为参数传入到你的函数中。当然也可以指定一个可选的转换器通过规则 <converter:variable_name>。 这里有一些不错的例子:
```py
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```
## HTTP方法
HTTP (也就说 web 应用协议)有不同的方法来访问 URLs。默认情况下，路由只会响应 GET 请求， 但是能够通过给 route() 装饰器提供 methods 参数来改变。这里是些例子:
```py
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```
如果使用 GET 方法，HEAD 方法将会自动添加进来。你不必处理它们。也能确保 HEAD 请求 会按照 HTTP RFC (文档在 HTTP 协议里面描述) 要求来处理， 因此你完全可以忽略这部分 HTTP 规范。 同样地，自从 Flask 0.6 后，OPTIONS 也能自动为你处理。

也许你并不清楚 HTTP 方法是什么？别担心，这里有一个 HTTP 方法的快速入门以及为什么它们重要：

HTTP 方法（通常也称为“谓词”）告诉服务器客户端想要对请求的页面 做 什么。下面这些方法是比较常见的：

### GET
浏览器通知服务器只 获取 页面上的信息并且发送回来。这可能是最常用的方法。
### HEAD
浏览器告诉服务器获取信息，但是只对 头信息 感兴趣，不需要整个页面的内容。 应用应该处理起来像接收到一个 GET 请求但是不传递实际内容。在 Flask 中你完全不需要处理它， 底层的 Werkzeug 库会为你处理的。
### POST
浏览器通知服务器它要在 URL 上 提交 一些信息，服务器必须保证数据被存储且只存储一次。 这是 HTML 表单通常发送数据到服务器的方法。
### PUT
同 POST 类似，但是服务器可能触发了多次存储过程，多次覆盖掉旧值。现在你就会问这有什么用， 有许多理由需要如此去做。考虑下在传输过程中连接丢失：在这种情况下浏览器 和服务器之间的系统可能安全地第二次接收请求，而不破坏其它东西。对于 POST 是不可能实现的，因为 它只会被触发一次。
### DELETE
移除给定位置的信息。
### OPTIONS
给客户端提供一个快速的途径来指出这个 URL 支持哪些 HTTP 方法。从 Flask 0.6 开始，自动实现了它。
现在比较有兴趣的是在 HTML4 和 XHTML1，表单只能以 GET 和 POST 方法来提交到服务器。在 JavaScript 和以后的 HTML 标准中也能使用其它的方法。同时，HTTP 最近变得十分流行，浏览器不再是唯一使用 HTTP 的客户端。比如，许多版本控制系统使用 HTTP。
## 静态文件
动态的 web 应用同样需要静态文件。CSS 和 JavaScript 文件通常来源于此。理想情况下， 你的 web 服务器已经配置好为它们服务，然而在开发过程中 Flask 能够做到。 只要在你的包中或模块旁边创建一个名为 static 的文件夹，在应用中使用 /static 即可访问。

给静态文件生成 URL ，使用特殊的 '**static**' 端点名:
```py
url_for('static', filename='style.css')
```
这个文件应该存储在文件系统上称为 static/style.css。
## 渲染模板
在 Python 中生成 HTML 并不好玩，实际上是相当繁琐的，因为你必须自行做好 HTML 转义以保持应用程序的安全。 由于这个原因，Flask 自动为你配置好 Jinja2 模版。

你可以使用方法 **render_template()** 来渲染模版。所有你需要做的就是提供模版的名称以及你想要作为关键字参数传入模板的变量。这里有个渲染模版的简单例子:
```py
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```
Flask 将会在 **templates** 文件夹中寻找模版。因此如果你的应用是个模块，这个文件夹在模块的旁边，如果它是一个包，那么这个文件夹在你的包里面:
### Case 1: 一个模块:
/application.py
/templates
    /hello.html
### Case 2: 一个包:

/application
    /__init__.py
    /templates
        /hello.html
- 这里是一个模版的例子：
```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
```

## 接收请求数据
对于 web 应用来说，对客户端发送给服务器的数据做出反应至关重要。在 Flask 中由全局对象 request 来提供这些信息。如果你有一定的 Python 经验，你会好奇这个对象怎么可能是全局的，并且 Flask 是怎么还能保证线程安全。 答案是上下文作用域:
### 局部上下文
Flask 中的某些对象是全局对象，但不是通常的类型。这些对象实际上是给定上下文的局部对象的代理。 虽然很拗口，但实际上很容易理解。

想象下线程处理的上下文。一个请求传入，web 服务器决定产生一个新线程(或者其它东西， 底层对象比线程更有能力处理并发系统)。当 Flask 开始它内部请求处理时，它认定当前线程是活动的上下文并绑定当前的应用和 WSGI 环境到那 个上下文（线程）。它以一种智能的方法来实现，以致一个应用可以调用另一个应用而不会中断。

所以这对你意味着什么了？如果你是做一些类似单元测试的事情否则基本你可以完全忽略这种情况。 你会发现依赖于请求对象的代码会突然中断，因为没有请求对象。解决方案就是自己创建一个请求并把它跟上下文绑定。 针对单元测试最早的解决方案是使用 test_request_context() 上下文管理器。结合 with 声明，它将绑定一个测试请求来进行交互。这里是一个例子:
## 重定向和错误
- 你能够用 redirect() 函数重定向用户到其它地方。能够用 abort() 函数提前中断一个请求并带有一个错误代码。 这里是一个它们如何工作的例子:
```py
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```
这是一个相当无意义的例子因为用户会从主页重定向到一个不能访问的页面（ 401意味着禁止访问）， 但是它说明了重定向如何工作。

默认情况下，每个错误代码会显示一个黑白错误页面。如果你想定制错误页面，可以使用 errorhandler() 装饰器:
```py
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```
注意到 404 是在 render_template() 调用之后。告诉 Flask 该页的错误代码应是 404 ， 即没有找到。默认的 200 被假定为：一切正常。
