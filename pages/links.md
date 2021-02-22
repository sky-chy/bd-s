---
layout: page
title: 链接
description: 没有链接的博客是孤独的
keywords: 友情链接
comments: true
menu: 链接
permalink: /links/
---
 
{% for link in site.data.links %}
> {{ link.type }}
  <ul>
    {% for ch in link.children %}
      <li style="margin-bottom:10px"><a href="{{ ch.url }}" target="_blank">
        {{ ch.name }}
        {% if ch.des %}<div>{{ ch.des }}</div>{% endif %}
      </a></li> 
    {% endfor %}
  </ul>
{% endfor %}
