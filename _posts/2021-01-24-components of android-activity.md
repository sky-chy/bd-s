---
layout: post
title: Android四大组件以及相关用法——Activity
categories: [Android,四大组件]
description:  Android四大组件以及相关用法—Activity
keywords: Android四大组件, 四大组件, Activity的用法, 生命周期, Activity的生命周期, Activity生命周期, Android四大组件
---

### 一、前言
对于学习Android开发知识的人来说，得从Android四大组件学起；Android的四大组件就是基础之一，其次还有五大储存、六大布局，把这些基础研究透了，Android开发的也就信手拈来了
学习四大组件，建议先从Activity开始，因为这个是在Android应用里面最常见的一个组件，本文只介绍Activity，话不多说，搞起！

### 二、正文
<span style="color:red;font-weight:bold">Activity</span>：通常就代表手机中屏幕中能够与用户交互的一些界面，一个Activity通常就是一个独立的窗口，在我们日常开发中使用Activity最多，并且Activity是以任务栈的机制去执行，即“后进先出”的结构，举个例子，若我们在不修改启动模式的情况下多次启动同一个Activity。系统会创建多个实例依次放入任务栈中。当按返回键返回时，每按一次，一个Activity出栈，直到栈空为止。当栈中无任何Activity时，系统就会回收此任务栈。

以下是在Activity的开发过程中会经常接触的一些知识：

  1. Activity生命周期都有哪些？每个生命周期都负责什么？

      ![生命周期图](/static/images/android/activity life cycle.webp)

      > onCreate()：不可见状态。第一次创建时调用，创建视图，并且能传递该Activity的上一个状态的Bundle参数。
      
      > onStart()：可见状态，可以显示Activity界面，但此时不能与用户交互。
      
      > onResume()：可见状态，当前界面可以进行交互。
      
      > onPause()：可见状态，此时Activity正在停止，接下来会调用onStop()。在onPause()中可以进行一些数据存储、动画停止、资源回收等。
      
      > onStop()：不可见状态，当前Activity停止或者被完全覆盖，当前Activity不可见，运行在后台。可以做一些资源释放的操作，不能做太耗时的操作。
      
      > onRestart()：在Activity重新启动时调用，由不可见状态变为可见状态。一般打开一个新的Activity在返回之前的Activity，旧的Activity会调用该生命周期。
      
      > onDestory()：Activity销毁。一般可以做一些回收工作和最终资源释放。
      
      > Activity生命周期的一些例子：
        - 当Activity正常启动：onCreat➜onStart➜onResume
        - 当Activity正常退出：onPause➜onStop➜onDestory
        - 当Activity横竖屏切换：
          - 在Manifest.xml没有设置android:configChanges属性
            - 启动：onCreat➜onStart➜onResume
            - 切换横屏：onSavedInstance➜onPause➜onStop➜onDestory➜onCreate➜onStart➜onRestoreInstanceState➜onResume
            - 从横屏切换成竖屏：onSavedInstance➜onPause➜onStop➜onDestory➜onCreate➜onStart➜onRestoreInstanceState➜onResume➜onSavedInstance➜onPause➜onStop➜onDestory➜onCreate➜onStart➜onRestoreInstanceState➜onResume(会重新创建两次)
          - 在Manifest.xml中设置了android:configChanges=“orientation”属性
            - 启动：onCreate➜onStart➜onResume
            - 切换横竖屏：onSavedInstanceState➜onPause➜onStop➜onDestory➜onCreate➜onStart➜onRestoreInstanceState➜onResume
            - 在从横屏切换回竖屏：onSavedInsatnceState➜onPause➜onStop➜onDestpry➜onCreate➜onStart➜onRestoreInstanceState➜onResume➜onConfigurationChanged
          - 在Manifest.xml中设置android:configChanges="orientation \| screenSize \| keyboardHidden"
            - 进行横屏切换：只会调用一次onConrigurationChanged
            - 从横屏切换回竖屏：onConfigurationChanged➜onConfigurationChanged
        - 当ActivityA跳转ActivityB，再按下back返回:
          - ActivityA：onCreate➜onStart➜onResume➜onPause
          - ActivityB：onCreate➜onStart➜onResume
          - ActivityA：onStop
          - 当按下返回键
          - ActivityB：onPause
          - ActivityA：onRestart➜onStart➜onResume
          - ActivityB：onStop➜onDestory

  1. Activity启动模式都有哪些？每个启动模式都有何特点？该如何使用？

      ![生命周期图](/static/images/android/activity start mode.png)

      > Standard 标准模式，也是默认模式：
      - Android创建Activity时的默认模式，永远不会调用onNewIntent()。假设没有为Activity设置启动模式的话，默觉得标准模式。每次启动一个Activity都会又一次创建一个新的实例入栈，无论这个实例是否存在。
      - 应用场景：最为普通的模式，需要注意的是，这个模式下启动Activity会不断产生新的栈

      > SingleTop 栈顶复用模式
      - 分两种处理情况：须要创建的Activity已经处于栈顶时，此时会直接复用栈顶的Activity。不会再创建新的Activity；若须要创建的Activity不处于栈顶，此时会又一次创建一个新的Activity入栈，同Standard模式一样。
      - 应用场景：假设你在当前的Activity中又要启动同类型的Activity，此时建议将此类型Activity的启动模式指定为SingleTop，能够降低Activity的创建，节省内存！例如推送消息的展示页。

      > SingleTask 栈内复用模式
      - 若需要创建的Activity已经处于栈中时，此时不会创建新的Activity，而是将存在栈中的Activity上面的其他Activity所有销毁，使它成为栈顶。
      - 应用场景：最常见的应用场景就是保持我们应用开启后仅仅有一个Activity的实例。最典型的样例就是应用中展示的主页（Home页）。假设用户在主页跳转到其他页面，运行多次操作后想返回到主页，假设不使用SingleTask模式，在点击返回的过程中会多次看到主页，这明显就是设计不合理了。

      > SingleInstance 单实例模式
      - SingleInstance比較特殊，是全局单例模式，是一种加强的SingleTask模式。它除了具有它所有特性外，还加强了一点：具有此模式的Activity仅仅能单独位于一个任务栈中。
      - 应用场景：由于该启动模式会重新创建一个任务栈，所以一般适合启动与程序分离的页面。例如跳转到拨打电话页面或者打开其他应用程序（打开地图App、分享等）

      > Activity启动模式的使用方式：
      - 在AndroidManifest.xml中指定Activity启动模式，例如：
        ```xml
        ...
         <activity android:name="com.chy.test.MainActivity" android:launchMode="singleTask"/>
        ...
        ```
      - 启动Activity时，在Intent中指定启动模式去创建Activity，一种动态的启动模式，在new 一个Intent后，通过Intent的addFlags方法去动态指定一个启动模式，例如：
        ```java
        ...
        Intent intent = new Intent();
        intent.setClass(context, MainActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        context.startActivity(intent);
        ...
        ```
      - 以上两种方式都能够为Activity指定启动模式，可是二者还是有差别的。
        * 优先级：后者比前者的优先级要高，若两者同在时，以后者为准。
        * 限定范围：前者无法为Activity直接指定 FLAG_ACTIVITY_CLEAR_TOP 标识，后者无法为Activity指定 singleInstance 模式。

      > 复用Activity生命周期回调：
      - 一般我们在携带参数跳转时不能将启动模式设置为SingleTop或者SingleTask。因为回复用原来的Activity，在复用的时候不会再去执行onCreate，只有在第一次创建时才会调用onCreate。此时会有一个onNewIntent方法，在Activity实例被复用的时候都会执行该方法，我们可以在该方法中会传入最新的intent，就可以解决上面的问题。一般在该方法中都会重新setIntent并初始化数据等。例如：
      ```java
      ...
      @Override
      protected void onNewIntent(Intent intent) {
          super.onNewIntent(intent);
          setIntent(intent);
          initData();
          initView();
      }
      ...
      ```


### 三、注意事项
无

### 四、相关资源
无
