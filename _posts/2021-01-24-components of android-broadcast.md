---
topmost: false
layout: post
title: Android四大组件以及相关用法——Broadcast
categories: [Android,四大组件]
author: CHY
description:  Android四大组件以及相关用法—Broadcast
keywords: Android, 四大组件, Broadcast, BroadcastReceiver, Android四大组件
---

### 一、前言
对于学习Android开发知识的人来说，得从Android四大组件学起；Android的四大组件就是基础之一，其次还有五大储存、六大布局，把这些基础研究透了，Android开发的也就信手拈来了
学习四大组件，建议先从[Activity](/2021/01/24/components-of-android-activity/)开始，因为这个是在Android应用里面最常见的一个组件，之后是[Server](/2021/01/24/components-of-android-server/)，其次是Broadcast，本文只介绍Broadcast，话不多说，搞起！

### 二、正文
<span style="color:red;font-weight:bold">Broadcast</span>：中文名为广播，是四大组件之一，主要用于接受APP发送的广播，内部通信实现机制：自定义广播接收者BroadcastReceiver，并复写onRecvice方法；通过android系统的Binder机制向AMS（Activity Manager Service）进行注册；广播发送者通过Binder机制向AMS发送广播；AMS查找符合条件的（IntentFilter/Permission等）的BroadcastReceiver，将广播发送到BroadcastReceiver(一般情况下是Activity)相应的消息循环队列中；消息循环执行拿到此广播，回调BroadcastReceiver 中的onReceiver()方法

以下是在Broadcast的开发过程中会经常接触的一些知识：

  1. 广播的应用场景是什么？

      > 同一个App中不同组件之间的消息通信。

      > 不同App组件之间传递消息。

  1. 有哪几种广播？分别有什么区别？

      > 按照注册方式分为：静态广播和动态广播
      - 静态广播：在Manifest.xml中通过<receiver></receiver>进行注册的广播，例如：
        ```xml
          ...
          <receiver android:name=".broadcast.CommonBroadcastReceiver">
              <intent-filter>
                  <!-- 关机广播 -->
                  <action android:name="android.intent.action.ACTION_SHUTDOWN" />
              </intent-filter>
          </receiver>
          ...
        ```
      - 动态广播：通过context.registerReceiver显示注册的广播，例如
        ```java
          IntentFilter intentFilter = new IntentFilter();
          intentFilter.addAction("android.intent.action.ACTION_SHUTDOWN");
          registerReceiver(new CommonBroadcastReceiver(),intentFilter);
        ```
      - 两者的区别：
        * 静态广播在程序没有运行或者程序已经销毁了，仍然可以收广播。动态广播是在程序中通过代码显示注册，因此必须在程序运行的时候才能收到广播。
        * 静态广播处理的时候每次都创建一个新的广播其接收对象，但动态广播一般都是一个广播接收器。
        * 针对一个无序广播，所有动态广播接收者都优先于所有的静态广播。同一个应用内先注册的广播接收者先收到广播。

      > 广播的发送方式来说：
      - 普通广播（无序广播）：通过context.sendBroadcast或者context.sendBroadcastAsUser发送给当前系统中所有注册的接收者。
      - 有序广播：接收者按照优先级处理广播，并且前面处理广播的接收者可以终止广播的传递，一般通过context.sendOrderBroadcast或者context.sendOrderBroadcastAAsUser.（有序广播可以中止广播也能修改数据，无序广播都不能）
      - 粘性广播：可以发送给以后注册的广播接收者。系统会将之前发送的粘性广播保存在AMS中，一旦注册了与已保存广播符合的接收者，注册完成之后就会立刻收到广播。一般通过context.sendStickyBroadcast或者context.sendStickyOrderBroadcast。

  1. 广播发送和接收的原理?

      > 发送原理：
      - 继承BroadcastReceiver，重写onReceive()方法。
      - 通过Binder机制向ActivityManagerService注册广播。
      - 通过Binder机制向ActivityMangerService发送广播
      
      > 接收原理：
      - ActivityManagerService查找符合相应条件的广播（IntentFilter/Permission）的
      - BroadcastReceiver，将广播发送到BroadcastReceiver所在的消息队列中。
      - BroadcastReceiver所在消息队列拿到此广播后，回调它的onReceive()方法。

  1. Binder机制是什么？

      > Android Binder是用来做进程通信的，Android的各个应用以及系统服务都运行在独立的进程中，它们的通信都依赖于Binder。

  1. Android里的Intent传递的数据有大小限制吗，如何解决？

      > Intent传递数据大小的限制大概在1M左右，超过这个限制就会静默崩溃。处理方式如下：
      - 进程内：EventBus，文件缓存、磁盘缓存。
      - 进程间：通过ContentProvider进行款进程数据共享和传递。

  1. BroadcastReceiver的生命周期？
      > BroadcastReceiver的onReceive（）方法执行完成后，BroadcastReceiver的实例就会被销毁。如果onReceive（）方法在10s内没有执行完毕，Android会认为改程序无响应。所以在BroadcastReceiver里不能做一些比较耗时的操作，否则会弹出“Application NoResponse”对话框。特别说明的是，这里不能使用子线程来解决 ，因为BroadcastReceiver的生命周期很短，子线程可能还没有结束BroadcastReceiver就先结束了。BroadcastReceiver一旦结束，此时它所在的进程很容易在系统需要内存时被优先杀死，因为它属于空进程。

### 三、注意事项
无

### 四、相关资源
无
