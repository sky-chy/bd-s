---
topmost: false #置顶
layout: post
title: template page
categories: [cate1, cate2]
author: CHY
description: some word here
keywords: keyword1, keyword2
---

# 一、系统以及环境
服务器系统：Ubuntu 16.04
项目环境：python 3.7 
框架：Django2.0
服务器环境：Uwsgi、Nginx
性能监测工具：Uwsgitop
使用背景：因为Django自带的服务器没通过安全审核，而且性能低下，原生为单线程运行，不足以应对多线程，高并发的需求。
# 二、安装相关环境
1. 首先将系统中的python环境安装或升级到python3.7（一般情况下，Ubuntu系统已经自带了python 2.x的的环境，但是因为2.x的python离现在的时代有些久远了，所以使用3.x的版本），具体操作请问度娘
2. 安装Django框架，具体安装方法请问度娘。服务器资源比较充裕的，可以安装一个PyCharm开发工具，度娘上面有破解版的，这个工具还算是比较智能化的，不过我是在客户机上面开发好项目再上传到服务器的，因为我的资源比较不充裕。
3. 安装uwsgi，打开系统的终端，执行命令：```pip install uwsgi```进行安装uwsgi工具，稍等片刻就安装好了
4. 基于APT源安装Nginx，在终端里面输入并执行：```sudo apt-get install nginx```，默认目录解说如下：
```/usr/sbin/nginx：```主程序
```/etc/nginx：```存放配置文件
```/usr/share/nginx：```存放静态文件
```/var/log/nginx：```存放日志
5. 安装uwsgi负载监测工具Uwsgitop，在终端里面输入并执行：```pip install uwsgitop```
# 三、创建并修改Django项目
1. 打开PyCharm这个开发工具，创建一个Django项目，等待项目加载完毕之后，执行以下命令
生成项目依赖文件
```pip freeze > requirements.txt```
上传到服务器的时候，```cd```到项目的根路径的时候，输入以下命令执行项目依赖文件的安装
```pip install -r requirements.txt```
<font color="red">上面这两句命令就是为了让系统环境统一</font>
然后在PyCharm开发工具的终端尝试使用```python manage.py runserver 0.0.0.0:8000```来运行项目，然后到本地浏览器去输入```http://127.0.0.1:8000```看看能否跳出Django的欢迎页面，如果能跳出就继续往下看，如果不能，就先让项目跑起来。

2. 在项目的根路径里面（与```manage.py```文件同级）创建一个```uwsgi.xml```文件，如下图所示，这个文件存在的意义就是让你服务器安装好的uwsgi工具可以对你的项目进行相关配置，具体内容如下
```html
<uwsgi>
    <socket>:8000</socket><!-- 与nginx通讯的端口-->
    <!--<http>:8000</http>-->
    <chdir>/(xxx项目的上级路径)/XXX</chdir>
    <module>YYY.wsgi</module><!--wsgi.py文件所在的位置-->
    <processes>4</processes> <!-- 进程数 -->
    <threads>2</threads> <!-- 线程数 -->
    <disable-logging>false</disable-logging>   <!--  true只记录uwsgi错误和内部消息，不记录常规请求信息，false反之-->
    <daemonize>/(uwsgi文件夹的上级路径)/uwsgi/uwsgi.log</daemonize><!--记录请求日志的文件所在的位置-->
    <!--<socket>/(uwsgi文件夹的上级路径)/uwsgi/uwsgi.sock</socket>--><!--与nginx工具通讯的所在位置-->
    <pidfile>/(uwsgi文件夹的上级路径)/uwsgi/uwsgi.pid</pidfile><!--对uwsgi进程管理的文件所在的位置-->
    <stats>/(uwsgi文件夹的上级路径)/uwsgi/uwsgi.status</stats><!--对uwsgi负载情况记录的文件所在的位置-->
    <master>true</master><!--开启主线程-->
    <vacuum>true</vacuum><!--true当服务器退出的时候自动清理环境，删除unix socket文件和pid文件，false反之-->
    <buffer-size>65535</buffer-size><!--uwsgi的最大缓存-->
</uwsgi>
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181116164438805.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0NTc4ODMz,size_16,color_FFFFFF,t_70)

3. 修改Django项目中的```setting.py```文件，首先吧```DEBUG=True```改成```DEBUG=False	```切换为生产模式，并在```setting.py```文件里面的空白地方填入一下内容，然后记得在把项目上传到服务端之后，记得先cd到项目的根路径，然后执行```Python manage.py collectstatic```把所有的静态资源取出来做全局静态资源，不然，NGINX 那里无法配置静态资源路径喔
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static_all')
STATIC_URL = '/static/'
STATIC_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```
到此，我们的项目就创建完毕了

# 四、修改服务端的nginx工具
1. 登录服务端，我这里采用的是阿里云的学生ECS服务器（才9.9元/月，条件好的，不建议采用这个服务器，因为它真的是不好用，太卡了，只是我资金不足，就只能采用这个服务器了,[点我进入购买阿里云服务器](https://promotion.aliyun.com/ntms/yunparter/invite.html?userCode=iw0mmx6h))

2. 打开终端输入 ```cd /etc/nginx```，回车，然后输入 ```ls ./```，回车，看看有没有存在```nginx.conf```这个文件，如果没有，那可能是你没安装好这个工具，这时候就得请万能的度娘帮你解决找不到这个文件的问题了

3. 找到文件之后，在终端里面继续输入```vim nginx.conf```来打开这个文件，然后按一下键盘上的```i```键就可以输入字符了，如果这个文件的第一行存在```user```的，就把后面的字段改为```root```,如果不存在的，就写```user root```到这个文件的第一行，然后找到```http{  }```标签，并在里面加入以下代码
```python
server{
	listen 80;#暴露给外网的端口
	server_name localhost;#服务器ip
	charset utf-8;#为了避免中文乱码
	access_log off:
	location /static{
		alias /(xxx项目的上级路径)/XXX/static_all;#这个路径就是在setting.py文件中写下的STATIC_ROOT的绝对路径
	}
	location /{
		uwsgi_pass 127.0.0.1:8000;#这个是在项目中的uwsgi.xml配置好的http请求路径和端口
		include /etc/nginx/uwsgi_params;	
	}
	location=/favicon.ico{
		log_not_found off;
		access_log off;
		root html;
	}
}
```
然后按一下键盘上的```Esc```键，再在英文状态下输入```:wq```，点击回车键进行保存输入的内容
到此，nginx工具就部署好了，现在把项目上传到服务器。

# 五、创建uwsgi的相关文件
在XXX（你的文件夹）中输入```mkdir```创建一个```uwsgi```文件夹,并cd到这个文件夹，然后依次执行```touch uwsgi.log```,```touch uwsgi.pid```,```touch uwsgi.sock```,```touch uwsgi.status```来创建（上面配置uwsgi.xml文件中所说的四个文件）四个uwsgi文件，然后回到你项目的根目录

# 六、运行项目
1. 先cd到项目的根路径，在终端中输入```uwsgi -x uwsgi.xml```，先加载项目中的uwsgi配置信息，然后再执行```/etc/init.d/nginx start ```来运行nginx工具就把项目运行起来了

2. 在你的浏览器里面输入"http://外网IP:端口"，例如:```http://47.107.1.205:80```就能看到你部署的Django项目了

# 七、相关命令
```linux
1. /etc/init.d/nginx start  启动nginx服务
2. /etc/init.d/nginx restart  重启nginx 服务
3. /etc/init.d/nginx stop  停止nginx 服务

针对uwsgi.pid文件
4. uwsgi -x uwsgi/uwsgi.xml             # uwsgi.xml方式启动
5. uwsgi --ini uwsgi/uwsgi.ini			 # uwsgi.ini方式启动
6. uwsgi --reload uwsgi/uwsgi.pid          # 重启
7. uwsgi --stop uwsgi/uwsgi.pid            # 关闭
```
# 八、uwsgi.ini方式的配置文件
uwsgi的配置有好几种方式，常用的就是ini和xml
```python
[uwsgi]#这个必写
uid = nginx #使用nginx用户和组
gid = nginx
chdir = /webser/www/demosite #指定项目目录，在配置多站点时，不要启用
module = demosite.wsgi #加载demosite/wsgi.py这个模块，在配置多站点时，不要启用
master = true #启动主进程。
processes = 2 #启动2个工作进程
listen = 120 #设置socket的监听队列大小（默认：100）
socket = /test/myapp.sock #指定socket文件，也可以指定为127.0.0.1:9000，这样就会监听到网络套接字
pidfile = /var/run/uwsgi.pid #指定pid文件
vacuum = true #当服务器退出的时候自动删除unix socket文件和pid文件。
enable-threads = true #允许用内嵌的语言启动线程。这将允许你在app程序中产生一个子线程
buffer-size = 32768 #设置用于uwsgi包解析的内部缓存区大小为64k。默认是4k。
reload-mercy = 8 #设置在平滑的重启（直到接收到的请求处理完才重启）一个工作子进程中，等待这个工作结束的最长秒数。这个配置会使在平滑地重启工作子进程中，如果工作进程结束时间超过了8秒就会被强行结束（忽略之前已经接收到的请求而直接结束）
max-requests = 5000 #为每个工作进程设置请求数的上限。当一个工作进程处理的请求数达到这个值，那么该工作进程就会被回收重用（重启）。你可以使用这个选项来默默地对抗内存泄漏
limit-as = 256 #通过使用POSIX/UNIX的setrlimit()函数来限制每个uWSGI进程的虚拟内存使用数。这个配置会限制uWSGI的进程占用虚拟内存不超过256M。如果虚拟内存已经达到256M，并继续申请虚拟内存则会使程序报内存错误，本次的http请求将返回500错误。
harakiri = 60 #一个请求花费的时间超过了这个harakiri超时时间，那么这个请求都会被丢弃，并且当前处理这个请求的工作进程会被回收再利用（即重启）
daemonize = /var/log/myapp_uwsgi.log # 使进程在后台运行，并将日志打到指定的日志文件或者udp服务器
disable-logging = true # 不记录请求信息的日志。只记录错误以及uWSGI内部消息到日志中
```
# 九、相关问题
1. 出现!!! no internal routing support, rebuild with pcre support !!!这个问题
```python
pip uninstall uwsgi
sudo apt-get install libpcre3 libpcre3-dev
pip install uwsgi
```
# 十、Ubuntu 安装python3.7
https://www.cnblogs.com/ningvsban/p/4384995.html

参考链接
https://www.jianshu.com/p/c3b13b5ad3d7
https://blog.csdn.net/eightbrother888/article/details/79503716
https://blog.csdn.net/fengzq15/article/details/78633827
https://yq.aliyun.com/ziliao/147659
