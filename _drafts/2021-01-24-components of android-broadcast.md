---
topmost: false
layout: post
title: Android四大组件以及相关用法——Broadcast
categories: [Android,四大组件]
author: CHY
description:  Android四大组件以及相关用法—Broadcast
keywords: CHY,G.M,博客,教程,网站,Android,四大组件,Activity,Server,ContentProvider,Broadcast,BroadcastReceiver
---

### 一、前言
不管学习什么知识，都得先打好基础，就好比建房子，没有基础，楼房建得再好，随时都有可能倒塌；对于学习Android开发知识的人来说也一样，都得从从基础学起；Android的四大组件(Activity, Server, ContentProvider, Broadcast)就是基础之一，还有五大储存，还有六大布局，把这些基础研究透了，Android开发的也就信手拈来了

学习四大组件，建议先从Activity开始，因为这个是在Android应用里面最常见的一个组价，其次是Server，再者是ContentProvider，最后是Broadcast，话不多说，搞起！

### 二、正文

<span style="color:red;font-weight:bold">Activity</span>：通常就代表手机中屏幕中能够与用户交互的一些界面，一个Activity通常就是一个独立的窗口，并且在我们日常开发中使用Activity最多，以下是在Activity的开发过程中会经常接触的一些知识：

  ![生命周期图](/static/images/android/activity life cycle.webp)

  1. Activity生命周期都有哪些？每个生命周期都负责什么？

      + onCreate：不可见状态。第一次创建时调用，创建视图，并且能传递该Activity的上一个状态的Bundle参数。
      + onStart：可见状态，可以显示Activity界面，但此时不能与用户交互。
      + onResume：可见状态，当前界面可以进行交互。
      + onPause：可见状态，此时activity正在停止，接下来会调用onStop。在onPause中可以进行一些数据存储、动画停止、资源回收等。
      + onStop：不可见状态，当前activity停止或者被完全覆盖，当前activity不可见，运行在后台。可以做一些资源释放的操作，不能做太耗时的操作。
      + onRestart：在activity重新启动时调用，由不可见状态变为可见状态。一般打开一个新的Activity在返回之前的activity，旧的activity会调用该生命周期。
      + onDestory：activity销毁。一般可以做一些回收工作和最终资源释放。
      + Activity生命周期的一些使用例子：
        - 正常启动：onCreat->onStart->onResume
        - 正常退出：onPause->onStop->onDestory
        - 横竖屏切换：
          
          - ①在Manifest.xml没有设置android：configChanges属性
            启动：onCreat->onStart->onResume
            切换横屏：onSavedInstance->onPause->onStop->onDestory->onCreate->onStart->onRestoreInstanceState->onResume
            从横屏切换成竖屏：onSavedInstance->onPause->onStop->onDestory->onCreate->onStart->onRestoreInstanceState->onResume->onSavedInstance->onPause->onStop->onDestory->onCreate->onStart->onRestoreInstanceState->onResume(会重新创建两次)
          - ②在Manifest.xml中设置了android：configChanges=“orientation”属性
            启动：onCreate->onStart->onResume
            切换横竖屏：onSavedInstanceState->onPause->onStop->onDestory->onCreate->onStart->onRestoreInstanceState->onResume
            在从横屏切换回竖屏：onSavedInsatnceState->onPause->onStop->onDestpry->onCreate->onStart->onRestoreInstanceState->onResume->onConfigurationChanged
          - ③在Manifest.xml中设置android:configChanges="orientation|screenSize|keyboardHidden"
            进行横屏切换：只会调用一次onConrigurationChanged
            从横屏切换回竖屏：onConfigurationChanged->onConfigurationChanged

  1. Activity是以任务栈的方式去执行，

<span style="color:red;font-weight:bold">Server</span>：是没有界面、生命周期比较长的程序，一般用来监控类的程序

<span style="color:red;font-weight:bold">ContentProvider</span>：内容提供者，用于数据共享，让一个应用程序指定数据集提供给其他应用程序

<span style="color:red;font-weight:bold">Broadcast</span>：广播，主要应用在程序之间传输信息的机制

### 三、注意事项

### 四、相关资源
无
