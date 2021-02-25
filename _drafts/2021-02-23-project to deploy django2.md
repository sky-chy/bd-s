---
topmost: false #置顶
layout: post
title: 在Ubuntu 16.04中结合Uwsgi+Nginx来部署Django2的项目
categories: [Python3,Django2]
author: CHY
description: 在Ubuntu 16.04中结合Uwsgi+Nginx来部署Django2的项目
keywords: 陈宏业, Python3, Django2, Python, Django, Nginx, Uwsgi, Ubuntu, 服务器, 阿里云, 腾讯云
---

### 一、情景导入
在Ubuntu系统环境里面部署基于Python3的Django2项目，同时还需要解决Django原生单线程缺陷、自带服务器安全性低和响应慢的问题，实现项目的高并发等高性能的需求

### 二、关键词
Django2、Uwsgi、Nginx、高并发

### 三、分析思路
关于思路前提，在[情景导入](#一情景导入)的时候已经很明确了，不过需要确定自己的Django项目是1.x还是2.x的，如果项目是Django2.x的，那么就跟本文有很多相似的地方了，否则就得另寻他处的解决方法了；在部署项目之前，需要先完善项目的生产环境，因为一台服务器不一定只有一个后端的项目，为了考虑多个项目的依赖冲突，这里推荐为项目装上虚拟环境来各个生产环境进行虚拟隔离管理

### 四、工具环境
+ Ubuntu 16.04
+ python 3.7.0
+ Django 2.0
+ Uwsgi 2.0.19.1
+ Nginx 1.18.0

### 五、实现步骤
无

### 六、实操代码
无

### 七、归纳总结
无

### 八、注意事项
无

### 九、相关资源
无
