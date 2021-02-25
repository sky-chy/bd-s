---
layout: page
title: 关于本站
description: 打码改变世界
keywords: Chen Hongye, 陈宏业
comments: true
menu: 关于
permalink: /about/
---

博主人比较懒，总是幻想代码能实现一切

在本站，你可以尽情的游览，同时还有更多有趣的文章等你发现

如果有什么不懂的，可以加博主的微信一起探讨，添加时记得发送备注：博客看到的

## 联系

<ul>
{% for website in site.data.social %}
<li>{{website.sitename }}：<a href="{{ website.url }}" target="_blank">@{{ website.name }}</a></li>
{% endfor %}
<li>邮箱：<a href="mailto:{{ site.email }}" target="_blank">{{ site.email }}</a></li>
{% if site.url contains 'chyblog.cn' %}
<li>
博主微信：<br />
<img style="height:192px;width:192px;border:1px solid lightgrey;" src="{{ assets_base_url }}/assets/images/wx_qrcode.jpg" alt="一切随猿" />
</li>
<li>
博主抖音：<br />
<img style="height:192px;width:192px;border:1px solid lightgrey;" src="{{ assets_base_url }}/assets/images/dy_qrcode.jpg" alt="一切随猿" />
</li>
{% endif %}
</ul>


## 技能关键词

{% for skill in site.data.skills %}
### {{ skill.name }}
<div class="btn-inline">
{% for keyword in skill.keywords %}
<button class="btn btn-outline" type="button">{{ keyword }}</button>
{% endfor %}
</div>
{% endfor %}
