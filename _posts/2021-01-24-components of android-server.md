---
layout: post
title: Android四大组件以及相关用法——Server
categories: [Android,四大组件]
description:  Android四大组件以及相关用法—Server
keywords: 四大组件, Android四大组件, Server, 服务, 启动服务, 销毁服务, 生命周期, Server的生命周期, Server生命周期, Android四大组件
---

### 一、前言
对于学习Android开发知识的人来说，得从Android四大组件学起；Android的四大组件就是基础之一，其次还有五大储存、六大布局，把这些基础研究透了，Android开发的也就信手拈来了
学习四大组件，建议先从Activity开始，因为这个是在Android应用里面最常见的一个组件，然后再到[Server](/2021/01/24/components-of-android-server/)，本文只介绍[Server](/2021/01/24/components-of-android-server/)，话不多说，搞起！

### 二、正文
<span style="color:red;font-weight:bold">Server</span>： 是没有界面、生命周期比较长的程序，地位与Activity并列，然而，Server在后台运行，可跨进程调用，无法自己运行。

以下是在Server的开发过程中会经常接触的一些知识：

  1. Server生命周期都有哪些？常用的方法有哪些？

      ![生命周期图](/static/images/android/server life cycle.webp)

      > onCreate()：首次创建服务时，系统将调用此方法。如果服务已在运行，则不会调用此方法，该方法只调用一次。

      > onStartCommand()：当另一个组件通过调用`startService()`请求启动服务时，系统将调用此方法。

      > onDestroy()：当服务不再使用且将被销毁时，系统将调用此方法。

      > onBind()：当另一个组件通过调用`bindService()`与服务绑定时，系统将调用此方法。

      > onUnbind()：当另一个组件通过调用`unbindService()`与服务解绑时，系统将调用此方法。

      > onRebind()：当旧的组件与服务解绑后，另一个新的组件与服务绑定，onUnbind()返回true时，系统将调用此方法。

      > 在Server的生命周期里，常用的方法有：
        - 手动调用的方法： 
          * startService() 启动服务
          * stopService() 关闭服务
          * bindService() 绑定服务
          * unbindService() 解绑服务
        - 自动调用的方法：
          * onCreat() 创建服务
          * onStartCommand() 开始服务
          * onDestroy() 销毁服务
          * onBind() 绑定服务
          * onUnbind() 解绑服务

  1. Server的启动方式有哪些？生命周期怎么运作？

      ![生命周期图](/static/images/android/server start mode.webp)

      > 第一种，start方式，该方式的执行过程为onCreate➜onStartCommad➜onDestory：
        - 用过start方式开启服务即便是调用者销毁service也不会被销毁，与现有的activity分离，不能与activity进行通信
        - 启动服务：startService()
        - 单次：onCreate()➜onStartCommand()
        - 多次：onCreate()➜onStartCommand()➜onStartCommand() ……
        - 多次启动服务onCreate只会执行一次，onStartCommand()会执行多次
        - 停止服务：stopService()，Server内执行onDestroy()

      > 第二种，bind方式，该方式的执行过程为onCreate➜onBind➜onUnbind➜onDestory：
        - 通过bind方式开启服务会与调用者生命周期进行绑定，并且能够与activity进行通信，调用者销毁service也会销毁
        - 绑定服务：bindService()，Server内执行onCreate()➜onBind()
        - 解绑服务：unbindService()，Server内执行onUnbind()➜onDestroy()
        
      > 先bind再进行start：
        - onCreate➜onBind➜onServiceConnected➜onStartCommand➜onUnbind➜onDestory

      > 先start再进行bind:
        - onCreate➜onStartCommand➜onBind➜onServiceConnected➜onUnbind➜onDestory

  1. Server执行在哪个线程？能否进行耗时操作？
      
      > Server一般默认都运行在主线程（除非指定Server的运行线程），所以Server中不能进行耗时操作。如果有特殊情况可以在清单文件中配置Server所在的线程，例如：
      
      ```xml
      ...
      <service android:name="com.baidu.location.f" android:enabled="true" android:process=":remote" ></service>
      ...
      ```

  1. 如何保证Server不被杀死？

      > 设置优先级，通过在清单文件中intent-filter中通过```android:priority=“1000”```来设置优先级，优先级越高越不容易被杀死

      > 在onStartCommend中调用startForeground将service提升为前台进程，最后记得在onStop中调用stopForeground

      > 将Server设置为START_STICKLY,当service被杀死之后会重启，重传intent，保持与之前一样
    
      > Server被杀死之后进行拉活。例如双线程唤起，当一个线程被杀死之后，另一个线程可以立即重启进程。或者依靠系统唤起

  1. 重复调用startService或者bindService会重复执行生命周期吗？
      
      > 重复执行startService会重复执行onStartCommand，但是onCreate只执行一次

      > 重复执行startService会重复执行onStartCommand，但是onCreate只执行一次 

      > 重复执行bindService所有生命周期不会重复执行，onBind和onCreate只执行一次

  1. 在Server中onStartCommand中能否执行网络操作？如何在Server中进行网络操作?

      > 可以在onStartCommand中进行网络操作，如果要在网络请求中进行耗时操作可以选择IntentService，IntentService是Service的子类，用来处理异步请求。

      > IntentService在onCreate中通过HandleThread单独开启一个线程来处理Intent请求对象对应的任务，可以避免事务处理而阻塞线程。

      > onHandleIntent()方法针对不同的intent进行不同的事务处理即可，执行完一个Intent请求对象的工作之后，如果没有新的intent请求到达，则自动停止Service，否则会取出下一个intent请求处理任务。

  1. Service中可以弹出Toast吗？

      > 弹出toast就需要一个上下文对象context，而Service本身就是Context的子类，因此在Service中弹出Toast是完全可以的。

### 三、注意事项
  1. 需要注意两种启动方式的区别：
  * startService()：开启Service，调用者退出后Service仍然存在。
  * bindService()：开启Service，调用者退出后Service也随即退出。

### 四、相关资源
无
