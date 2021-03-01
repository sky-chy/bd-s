---
topmost: false
layout: post
title: Android四大组件以及相关用法——ContentProvider
categories: [Android,四大组件]
author: CHY
description:  Android四大组件以及相关用法—ContentProvider
keywords:  Android, 四大组件, ContentProvider, Android四大组件
---

### 一、前言
对于学习Android开发知识的人来说，得从Android四大组件学起；Android的四大组件就是基础之一，其次还有五大储存、六大布局，把这些基础研究透了，Android开发的也就信手拈来了
学习四大组件，建议先从[Activity](/2021/01/24/components-of-android-activity/)y开始，因为这个是在Android应用里面最常见的一个组件，之后是[Server](/2021/01/24/components-of-android-server/)，其次是[Broadcast](/2021/01/24/components-of-android-broadcast/)，最后是ContentProvider，本文只介绍ContentProvider，话不多说，搞起！

### 二、正文

<span style="color:red;font-weight:bold">ContentProvider</span>：ContentProvider管理android以结构化方式存放的数据。他以相对安全的方式封装数据并且提供简易的处理机制。Content provider提供不同进程间数据交互的标准化接口。保证被访问数据的安全性。内容提供器可以选择只对哪一部分数据进行共享，从而保证我们程序中的隐私数据不会有泄漏的风险，以下是在ContentProvider的开发过程中会经常接触的一些知识：

  1. 在Android中为什么要使用ContentProvider？

      > 隐藏数据的实现方式，对外提供统一的数据访问接口。

      > 更好的数据访问权限管理。contentProvider可以对开发的数据进行权限设置，不同的Uri对应不同的权限，只有符合权限要求的组件才能访问到ContentProvider的具体操作。

      > 封装了跨进程共享的逻辑，我们只需要使用Uri即可访问数据，由系统管理ContentProvider的创建、生命周期及访问的线程分配，我们只管通过ContentResolver访问ContentProvider所提示的数据接口，不需要关心他所在的线程是否启动。

  1. 运行在主线程的ContentProvider为什么不会影响主线程UI操作？

      > ContentProvider的onCreat是运行在主线程的，而query、insert、delete等等，一些操作是运行在线程池中的工作线程的。，所以调用这些方法并不会阻塞ContentProvider所在进程的主线程，但可能会阻塞调用者所在进程的UI线程，所以调用ContentProvider操作仍然需要放在子线程去做，虽然直接进行的增删改查操作直接是在工作线程进行的，但是系统会让你的调用线程等待这个异步操作完成才能进行其他操作。

  1. 与sql实现上有什么区别？

      > ContentProvider隐藏了数据存储的细节，内部实现对用户完全透明，用户只要关心操作数据的Uri就可以，ContentProvider可以实现不同app之间数据共享。

      > sql也能进行增删改查，但是这能对本程序下的数据进行操作，不能操作其他程序的数据。

      > ContentProvider可以增删改查本地文件、xml文件的读取。
  
  1. 如何访问asserts中的数据库？

      > 以前工程中由db文件，会存放在raw文件中	，用户安装后将db文件复制到data/data/packagename/database下就能直接访问。但现在只需要几行代码即可：
      ```java
        ...
        //初始化
        AssetsDatabaseManager.initManager(context);
        //数据库都需要获取管理对象
        AssetsDatabaseManager assets=AssetsDatabaseManager.getManager();
        //通过管理对象获取数据库
        db=assets.getDatabase("address.db);
        ...
      ```

  1. 说说ContentProvider、ContentResolver、ContentObserver 之间的关系

      > ContentResolver中提供了一系列的方法用于对数据进行CRUD，内容URI给内容提供器ContentProvider中的数据建立了唯一标识符，ContentObserver监听Uri数据的变化
      - ContentProvider：管理数据，提供数据的增删改查操作，数据源可以是数据库、文件、XML、网络等。ContentProvider为这些数据提供了统一的接口，可以用来做进程间数据共享;
      - ContentResolver：ContentResolver可以不同的URI操作不同的ContentProvider中的数据库，外部进程可以通过ContentResolver 与ContentProvider进行交互;
      - ContentObserver ：观察ContentProvider中的数据变化，并将变化通知给外界。

### 三、注意事项
无

### 四、相关资源
无
