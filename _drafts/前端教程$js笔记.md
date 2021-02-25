---
topmost: false #置顶
layout: post
title: template page
categories: [cate1, cate2]
author: CHY
description: some word here
keywords: keyword1, keyword2
---
## 一、JQuery
### 1、改变浏览器窗口大小的时候让页面自动刷新
```javascript
$(window).resize(function(){//当浏览器大小变化时
    location.reload()//刷新本页面
    //这里你可以写你的刷新代码！
});
```
### 2、当网页加载完毕时候加载
```javascript
$(document).ready(function () {
	...
}
```
## 二、Javascript
### 1、通过navigator判断浏览器是移动端还是pc端
```javascript
function isMobile() {
    const userAgentInfo = navigator.userAgent;
    const mobileAgents = ["Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod"];
    let mobile_flag = false;
    //根据userAgent判断是否是手机
    for (let v = 0; v < mobileAgents.length; v++) {
        if (userAgentInfo.indexOf(mobileAgents[v]) > 0) {
            mobile_flag = true;
            break;
        }
    }
    return mobile_flag;
}
```
### 2、通过尺寸判断设备类型 
```javascript
function screen_Size() {
    const result1 = window.matchMedia('(min-width:1200px)');
    const result2 = window.matchMedia('(min-width:992px)');
    const result3 = window.matchMedia('(min-width:768px)');
    if (result1.matches) {
        return "大台式电脑";
    } else if (result2.matches) {
        return "台式电脑";
    } else if (result3.matches) {
        return "平板电脑";
    } else {
        return "手机";
    }
}
```
### 3、正则判断是否是手机号码
```javascript
function isPhone(account) {
    // 手机号码正则
    const re_phone = /^((\d{3}-\d{8}|\d{4}-\d{7,8})|(1[3|5|7|8|9][0-9]{9}))$/;
    return re_phone.test(account);
}
```
### 4、正则判断是否是邮箱
```javascript
function isMail(account) {
    // 邮箱正则
    const re_mail = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/;
    return re_mail.test(account);
}
```
### 5、取消href跳转属性
```javascript
<a href="javascript:;">
<a href="javascript:void(0);">
```
