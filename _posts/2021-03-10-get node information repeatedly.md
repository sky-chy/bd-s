---
topmost: false #置顶
layout: post
title: boundingClientRect重复回调
categories: [小程序, uni-app]
author: CHY
description: some word here
keywords: uniapp, uni.createSelectorQuery,小程序API,Uniapp Api,计算高度,uniapp计算控件高度
---

### 一、情景导入
近日，博主在自定义组件中使用`uni.createSelectorQuery()`这个API去获取节点信息来计算页面控件高度的时候，发现重复获取了一个数据，导致计算的数据不符合预期

### 二、关键词
重复获取

### 三、分析思路
无

### 四、工具环境
+ MacOS 10.15.7
+ HBuilder X 3.1.4.20210305

### 五、实现步骤
```js
<script>
  export default {
    data() {
      return {
        contentHeight:0
      }
    },
  
    ......
  
    mounted() {
      const systemInfo = uni.getSystemInfoSync()
      this.contentHeight = systemInfo.windowHeight

      // 如果存在多个selector的节点，声明变量后再使用selectAll或者select可能会导致boundingClientRect回调多次
      const query = uni.createSelectorQuery().in(this);
      query.selectAll('.grader-parent').boundingClientRect(data => {
        if (data.length === 0) {
          return
        }
        this.contentHeight -= data[0].height 
      }).exec();

      // 如果存在多个selector的节点，又想保证boundingClientRect只回调一次，可以尝试直接链式调用
      uni.createSelectorQuery().in(this).select('.grader-parent').boundingClientRect(data => {
        if (!data) {
          return
        }
        this.contentHeight -= data.height 
      }).exec();
    }
  
    ......
  
  }
</script>
```

### 六、实操代码
无

### 七、归纳总结
无

### 八、注意事项
无

### 九、相关资源
无
