---
topmost: false #置顶
layout: post
title: Android 各版本API的基本特性
categories: [Android, SDK]
author: CHY
description: Android 各API的基本特性
keywords: Android SDK, Android, SDK特性, 安卓SDK
---

### 一、前言
众所周知，Android系统的版本迭代比较快，从2008年9月开始的Android1.0到现在的Android11.0，总共经历了30个版本的Api的迭代，从第23版的Api开始，就对系统进行了大刀阔斧的改革。实话说，从这个版本开始，Google就安全方面有点向苹果看齐了，不过业界大佬的事情，咱门也说不清，只能说，跟着官方走就好了

### 二、正文 
以下是Android各版本的相关对比：

|Android版本|Api版本|版本信息|
|:----------|:------:|:----|
|[Android 11.0 R](https://developer.android.google.cn/about/versions/11)|30|——|
|[Android 10.0 Q](https://developer.android.google.cn/about/versions/10)|29|——|
|Android 9.0 Pie|28|1、加入了全新的"自适应"电池功能,可以让手机智能判断用户对App的使用情况,并且还可以智能调节CPU的使用,最大限度地降低耗电量(加入人工智能)<br/>2、重新设计系统界面,重绘系统图标,在屏幕底部增加了一个短横符号,其作用相当于原来的Home键.<br/>3、提供了人工智能的API,整合形成"MLKit".<br/>4、手机支持翻转手机进入免打扰模式.|
|Android 8.1 Oreo|27|——|
|Android 8.0 Oreo|26|1、TensorFlow Lite概念；<br/>2、画中画；<br/>3、Notification Dots；<br/>4、智能文本选择（Smart Text Selection）；<br/>5、自动填写（Auto-Fill）；<br/>6、Google Play Protect；<br/>7、系统/应用启动程序加速；<br/>8、Play Console Dashboard <br/>9、Android O中大部分的界面改变都在设置菜单中,整体更加简洁<br/>10、自适应图标,即:桌面图标都是相同的形状<br/>11、后台进程,严格限制了后台进程对手机资源的调用.<br/>12、取消了大部分静态广播注册|
|Android 7.1 Nougat|25|——|
|Android 7.0 Nougat|24|1、多窗口支持,可以指定应用允许的最小尺寸.同时打开两个应用,并且在多窗口模式中,增加了拖拽功能,对于开发者,可以设置Activity允许的最小尺寸,分屏模式(屏幕一分为二)、画中画模式(TV上应用,视频播放窗口一直在最顶层显示)、Freeform模式(应用界面可以自由拖动或者修改大小)<br/>2、增加了JIT编译器,并对ART进行代码分析,使得安装提速并且所占空间减少.<br/>3、对通知进行了许多的增强,消息传递可以自定义,开发者只需要用到MessagingStyle进行配置即可.<br/>4、低耗电模式<br/>5、Android N 引入一项新的应用签名方案 APK Signature Scheme v2,它能提供更快的应用安装时间和更多针对未授权 APK 文件更改的保护.|
|Android 6.0 Marshmallow|23|1、App Permissions（软件权限管理）。<br/>2、Chrome Custom Tabs（网页体验提升）。<br/>3、App Links（APP关联）。<br/>4、Android Pay（安卓支付）。<br/>5、Fingerprint Support（指纹支持）。<br/>6、Power & Change（电量管理 ）|
|Android 5.1 Lollipop|22|——|
|Android 5.0 Lollipop|21|1、谷歌将为Android的语音服务Google Now加入一个名为OK Google Everywhere的全新功能。<br/>2、Android 5.0可能还会加入更多的健身功能，考虑到谷歌在发布了Android Wear，后者与智能手表及谷歌眼镜等可穿戴设备的协作应该会成为下个版本的重点功能。<br/>3、整合碎片化<br/>4、传言Google将在Android5.0中，禁止厂商进行深度定制。<br/>5、数据迁移<br/>6、独立平板<br/>7、功能按键<br/>8、接口风格|
|Android 4.4.4 KitKat|20|——|
|Android 4.4 KitKat|19|1、优化了RenderScript计算和图像显示,取代OpenCL<br/>2、支持两种编译模式<br/>3、Android 4.4 KitKat针对RAM占用进行了优化，甚至可以在一些仅有512MB RAM的老款手机上流畅运行。<br/>4、新图标、锁屏、启动动画和配色方案<br/>5、新的拨号和智能来电显示<br/>6、加强主动式语音功能<br/>7、集成Hangouts IM软件<br/>8、全屏模式<br/>9、支持Emoji键盘<br/>10、轻松访问在线存储<br/>11、无线打印<br/>12、屏幕录像功能<br/>13、内置字幕管理功能<br/>14、计步器应用<br/>15、低功耗音频和定位模式<br/>16、新的接触式支付系统<br/>17、新的蓝牙配置文件和红外兼容性|
|Android 4.3 Jelly Bean|18|1、用户账户配制<br/>2、拨号盘联系人自动补全<br/>3、OpenGL 3.0<br/>4、蓝牙低耗电技术<br/>5、WIFI关闭后保持位置功能<br/>其它特性<br/>新的相机应用UI<br/>新的开发者工具<br/>通过邮件分享截屏时，日期和时间会自动加入进去。|
|Android 4.2 Jelly Bean|17|1、完整的Chrome浏览器<br/>2、全新的手机风景模式<br/>3、全新的文件管理器<br/>4、文本输入选项的改进<br/>5、一个明确的升级方法<br/>6、Android Key Lime Pie精简版<br/>7、具有开关切换的用户界面<br/>8、全新的电源管理系统<br/>9、更为轻便的主题模式<br/>10、全新的锁屏页面<br/>11、全新的时钟界面|
|Android 4.1 Jelly Bean|16|1.更快、更流畅、更灵敏<br/>2.增强通知栏<br/>3.全新搜索<br/>4.桌面插件自动调整大小<br/>5.加强无障碍操作<br/>6.语言和输入法扩展<br/>7.新的输入类型和功能<br/>8.新的连接类型<br/>9.新的媒体功能<br/>10.浏览器增强<br/>11.Google服务|
|Android 4.0.3 - 4.0.4 Ice Cream Sandwich|15|——|
|Android 4.0 - 4.0.2 Ice Cream Sandwich|14|1、蓝色主题<br/>2、接近于桌面版的Chrome Lite浏览器，有离线阅读，同步Chrome书签，新的标签样式等。<br/>3、截图功能<br/>4、更强大的图片编辑功能<br/>5、自带照片应用堪比Instagram，可以加滤镜、加相框，进行360度全景拍摄，照片还能根据地点来排序<br/>6、Gmail加入手势、离线搜索功能，UI更强大。<br/>7、新功能People：以联系人照片为核心，界面偏重滑动而非点击，集成了Twitter、Linkedin、Google+等通讯工具。有望支持用户自定义添加第三方服务。<br/>8、新增流量管理工具，可具体查看每个应用产生的流量。<br/>9、正在运行的程序可以像电脑一样的互相切换<br/>10、人脸识别功能<br/>11、系统优化、速度更快<br/>12、支持虚拟按键，手机可以不再拥有任何按键<br/>13、专为3D优化的驱动<br/>14、平板电脑和智能手机通用|
|Android 3.2 Honeycomb|13|1、支持7英寸设备<br/>2、引入了应用显示缩放功能|
|Android 3.1 Honeycomb|12|1、Honeycomb 蜂巢（改进3.0BUG）<br/>2、经过优化的Gmail电子邮箱；<br/>3、全面支持GoogleMaps<br/>4、将Android手机系统跟平板系统再次合并从而方便开发者。<br/>5、任务管理器可滚动，支持USB 输入设备（键盘、鼠标等）。<br/>6、支持 Google TV、可以支持XBOX 360无线手柄<br/>7、widget支持的变化，能更加容易的定制屏幕widget插件。|
|Android 3.0 Honeycomb|11|1、Fragments：较activity粒度小的拥有独自生命周期的模块。可作为acitivity的一部分，activity通过FragmentManager管理独自的fragments back stack。<br/>2、Action Bar：activity顶部标题栏的替代品，通常含logo，点击出现原menu菜单项–称作action item。可与tab、Fragments back stack合用。<br/>3、粘贴版：系统范围的复制、粘贴。通过系统服务CLIPBOARD_SERVICE。<br/>4、Drag and drop：在view中监听drag、drop动作，通过ClipData（与系统粘贴版无关）传递数据。<br/>5、App widgets：支持GridView、ListView、StackView及ViewFlipper。<br/>6、Content loader：Loader类简化异步数据加载；CursorLoader简化ContentProvider的数据加载。<br/>7、动画支持扩展：全新动画框架，更灵活。<br/>8、硬件绘制加速： android:hardwareAccelerated=”true” 启用OpenGl硬件绘制加速。支持renderscript脚本语言。|
|Android 2.3.3-2.3.7 Gingerbread|10|——|
|Android 2.3 - 2.3.2 Gingerbread|9|1、优化针对平板<br/>2、全新设计的UI增强网页浏览功能<br/>3、·n-app purchases功能|
|Android 2.2 - 2.2.3 Froyo|8|1、整体性能大幅度的提升<br/>2、3G网络共享功能。<br/>3、Flash的支持。<br/>4、App2sd功能。<br/>5、全新的软件商店。<br/>6、更多的Web应用API接口的开发。|
|Android 2.1 Éclair|7|——|
|Android 2.0.1 Éclair|6|——|
|Android 2.0 Éclair|5|1、优化硬件速度<br/>2、 “Car Home”程序<br/>3、支持更多的屏幕分辨率<br/>4、改良的用户界面<br/>5、新的浏览器的用户接口和支持HTML5<br/>6、新的联系人名单<br/>7、更好的白色/黑色背景比率<br/>8、改进Google Maps3.1.2<br/>9、支持Microsoft Exchange<br/>10、支持内置相机闪光灯<br/>11、支持数码变焦<br/>12、改进的虚拟键盘<br/>13、支持蓝牙2.1<br/>14、支持动态桌面的设计|
|Android 1.6 Donut|4|1、重新设计的Android Market手势<br/>2、支持支持CDMA网络<br/>3、文字转语音系统（Text-to-Speech）<br/>4、快速搜索框<br/>5、全新的拍照接口<br/>6、查看应用程序耗电<br/>7、支持虚拟私人网络（VPN）<br/>8、支持更多的屏幕分辨率。<br/>9、支持OpenCore2媒体引擎<br/>10、新增面向视觉或听觉困难人群的易用性插件|
|Android 1.5 Cupcake|3|1、拍摄/播放影片，并支持上传到Youtube<br/>2、支持立体声蓝牙耳机，同时改善自动配对性能<br/>3、最新的采用WebKit技术的浏览器，支持复制/贴上和页面中搜索<br/>4、GPS性能大大提高<br/>5、提供屏幕虚拟键盘<br/>6、主屏幕增加音乐播放器和相框widgets<br/>7、应用程序自动随着手机旋转<br/>8、短信、Gmail、日暦，浏览器的用户接口大幅改进，如Gmail可以批量删除邮件<br/>9、相机启动速度加快，拍摄图片可以直接上传到Picasa<br/>10、来电照片显示|
|Android 1.1 Petit Four|2|——|
|Android 1.0|1|2008 年9月发布的Android第一版|

### 三、注意事项
无

### 四、相关资源
[Android的发展历史](https://www.cnblogs.com/djdh/p/10449223.html)

[Android历史版本](https://baike.baidu.com/item/Android%E5%8E%86%E5%8F%B2%E7%89%88%E6%9C%AC/1578450)

[Android各版本特性](https://blog.csdn.net/pkorochi/article/details/104495274)

[android api各个版本特性简单描述到6.0](https://blog.csdn.net/WuLex/article/details/83651107)

[Android 10系统新特性解读](https://blog.csdn.net/xiangzhihong8/article/details/88108825)
