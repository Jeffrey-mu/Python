# Django 快速入门
## 安装 
```shell
pip3 install Django
```
## 创建项目
```shell
django-admin startproject djangosite
```
- 这将在您的当前目录中创建一个djangosite目录。
```
djangosite/
    manage.py
    djangosite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
这些文件是：

- 外部djangosite/根目录是您项目的容器。它的名字对 Django 无关紧要。您可以将其重命名为您喜欢的任何名称。
- manage.py：一个命令行实用程序，可让您以各种方式与此 Django 项目进行交互。您可以阅读 django-admin 和 manage.pymanage.py中的所有详细信息。
- 内部djangosite/目录是您项目的实际 Python 包。它的名称是 Python 包名称，您需要使用它来导入其中的任何内容（例如djangosite.urls）。
- djangosite/__init__.py: 一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果您是 Python 初学者，请阅读官方 Python 文档中有关包的更多信息。
- djangosite/settings.py：此 Django 项目的设置/配置。 Django 设置会告诉你设置是如何工作的。
- djangosite/urls.py：这个 Django 项目的 URL 声明；由 Django 驱动的站点的“目录”。您可以在URL dispatcher中阅读有关 URL 的更多信息。
- djangosite/asgi.py：为您的项目提供服务的兼容 ASGI 的 Web 服务器的入口点。有关更多详细信息，请参阅如何使用 ASGI进行部署。
- djangosite/wsgi.py: 为您的项目提供服务的 WSGI 兼容 Web 服务器的入口点。有关更多详细信息，请参阅如何使用 WSGI进行部署。
## 开发服务器
```shell
python manage.py runserver
```
- 使用您的 Web 浏览器访问http://127.0.0.1:8000/ 。您会看到“恭喜！” 页面，火箭起飞。有效！
### 更改端口
```shell
python3 manage.py runserver 8080
```
- 如果要更改服务器的 IP，请将其与端口一起传递。例如，要监听所有可用的公共 IP（如果您正在运行 Vagrant 或想在网络上的其他计算机上炫耀您的工作，这很有用），请使用：
```shell
 python manage.py runserver 0:8000
```
### 自动重新加载runserver
- 开发服务器会根据需要自动为每个请求重新加载 Python 代码。您无需重新启动服务器即可使代码更改生效。但是，添加文件等某些操作不会触发重新启动，因此在这些情况下您必须重新启动服务器。
### 项目与应用
- 项目和应用程序有什么区别？应用程序是做某事的网络应用程序——例如，博客系统、公共记录数据库或小型投票应用程序。项目是特定网站的配置和应用程序的集合。一个项目可以包含多个应用程序。一个应用程序可以在多个项目中。
- 要创建您的应用程序，请确保您在同一目录中manage.py 并键入以下命令：
```shell
python manage.py startapp polls
```
### 写你的第一个视图
- 让我们写第一个视图。打开文件polls/views.py 并将以下 Python 代码放入其中：
```py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
- 这是 Django 中最简单的视图。要调用视图，我们需要将其映射到一个 URL——为此我们需要一个 URLconf。

要在 polls 目录中创建 URLconf，请创建一个名为urls.py. 您的应用程序目录现在应该如下所示：
- 下一步是将根 URLconf 指向polls.urls模块。在 mysite/urls.py中，添加一个导入并在列表中django.urls.include插入一个 ，这样您就有：include()urlpatterns
### path()论据：route
- route是一个包含 URL 模式的字符串。当处理一个请求时，Django 从第一个模式开始urlpatterns并沿着列表向下移动，将请求的 URL 与每个模式进行比较，直到找到匹配的一个。

- 模式不搜索 GET 和 POST 参数或域名。例如，在对 的请求中https://www.example.com/myapp/，URLconf 将查找 myapp/. 在对 的请求中https://www.example.com/myapp/?page=3，URLconf 也会查找myapp/.
### path()论据：view¶
- 当 Django 找到匹配的模式时，它会调用指定的视图函数，并将HttpRequest对象作为第一个参数，并将路由中任何“捕获”的值作为关键字参数。我们稍后会给出一个例子。

### path()论据：kwargs¶
- 任意关键字参数可以在字典中传递给目标视图。我们不会在教程中使用 Django 的这个特性。

### path()论据：name¶
- 命名你的 URL 可以让你从 Django 的其他地方明确地引用它，尤其是在模板中。这个强大的功能允许您对项目的 URL 模式进行全局更改，而只需触摸一个文件。
