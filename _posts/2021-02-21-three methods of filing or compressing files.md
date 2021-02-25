---
layout: post
title: Python3对文件的3种归档或者压缩打包方法
categories: Python3
author: CHY
description: Python3对文件的3种归档或者压缩压缩打包方法
keywords: Python3教程, Python教程, 7z压缩, py7zr使用, 文件归档
---

### 一、情景导入
朋友说手上有很多文件需要快速实现归档或者压缩，并且有些文件还需要加入密码保护的，如果靠自己一个一个文件进行归档或者压缩，不知道要到什么时候才能完成，人工和时间成本相对较高，问我有没有什么办法可以实现大量文件快速压缩，同时还能设定是否开启密码保护功能，话不多说，搞起！

### 二、关键词
大量文件、归档、压缩、密码保护、成本

### 三、分析思路
根据上述情景和关键词得知，需用实现对多个文件进行自动化归档或者压缩打包

### 四、工具环境
+ Python 3.7.0
+ py7zr 0.13.0
+ PyCharm 2019.1.2
+ MacOS 10.15.7

### 五、实现步骤
1. 首选获取到源文件的路径，假设源文件的路径变量为`file_paths`;
1. 之后使用ThreadPoolExecutor来创建线程池，并对每个文件进行独立线程操作，假设线程池的变量为`executor`；
1. 创建归档后的目标文件夹
1. 开始[加密]归档文件到目标文件夹

### 六、实操代码
+ 第1种方法，使用zipfile模块

  ```python
  # -*- coding:utf8 -*-
  import os
  import zipfile
  from concurrent.futures.thread import ThreadPoolExecutor

  class ZipFileUtil:
      def __init__(self):
          self.resource_path = '/Users/chenhongye/Documents/Resource'  # 源文件的父目录，需要指定自己的路径，可全部覆盖重写
          self.target_path = '/Users/chenhongye/Documents/Target'  # 归档或打包压缩后的目录，需要指定自己的路径，可全部覆盖重写

          self.file_paths = []  # 所有源文件路径
          self.executor = ThreadPoolExecutor(10)  # 创建容量为10 的线程池

      # 初始化
      def __init(self):
          # 创建保存目录
          if not os.path.exists(self.target_path):
              os.mkdir(self.target_path)

      # 获取所有源文件路径
      def __get_file_path(self):
          file_list = os.listdir(self.resource_path)
          self.file_paths = [os.path.join(self.resource_path, video_name) for video_name in file_list]

      # zipfile模块打包归档，只支持设置提取密码
      def zip(self, path):
          file_base_name = os.path.splitext(os.path.basename(path))[0]
          with zipfile.ZipFile(os.path.join(self.target_path, f'{file_base_name}.zip'), 'w') as f:
              f.write(path)
          return os.path.basename(path)

      # 主入口
      def main(self):
          try:
              self.__get_file_path()
              # 启动线程池
              for data in self.executor.map(self.zip, self.file_paths):
                  print(f'{data}的操作{"成功" if data else "失败"}')
              print('已完成全部操作，程序结束')
          except Exception as e:
              print(e)
          finally:
              self.executor.shutdown()


  if __name__ == '__main__':
      ZipFileUtil().main()
  ```

+ 第2种方法，使用系统命令

  ```python
  # -*- coding:utf8 -*-
  import os
  import zipfile
  from concurrent.futures.thread import ThreadPoolExecutor
  from itertools import repeat


  class ZipFileUtil:
      def __init__(self):
          self.resource_path = '/Users/chenhongye/Documents/Resource'  # 源文件的父目录，需要指定自己的路径，可全部覆盖重写
          self.target_path = '/Users/chenhongye/Documents/Target'  # 归档或打包压缩后的目录，需要指定自己的路径，可全部覆盖重写

          self.file_paths = []  # 所有源文件路径
          self.executor = ThreadPoolExecutor(10)  # 创建容量为10 的线程池
          self.__init()

      # 初始化
      def __init(self):
          # 创建保存目录
          if not os.path.exists(self.target_path):
              os.mkdir(self.target_path)

      # 获取所有源文件路径
      def __get_file_path(self):
          file_list = os.listdir(self.resource_path)
          self.file_paths = [os.path.join(self.resource_path, video_name) for video_name in file_list]

      # cmd命令打包归档，支持归档密码
      def cmd_file(self, path, pwd=None):
          file_base_name = os.path.splitext(os.path.basename(path))[0]
          out_full_name = os.path.join(self.target_path, file_base_name)
          if pwd:
              cmd = f'zip -j -P {pwd} "{out_full_name}.zip" {path}'
          else:
              cmd = f'zip -j "{out_full_name}.zip" {path}'
          os.system(cmd)
          return os.path.basename(path)

      # 主入口
      def main(self):
          try:
              self.__get_file_path()
              # 启动线程池
              for data in self.executor.map(self.cmd_file, self.file_paths, repeat('123456')):
                  print(f'{data}的操作{"成功" if data else "失败"}')
              print('已完成全部操作，程序结束')
          except Exception as e:
              print(e)
          finally:
              self.executor.shutdown()


  if __name__ == '__main__':
      ZipFileUtil().main()
  ```

+ 第3种方法，使用py7zr模块，需要另外安装
  
  在终端上面执行以下命令安装py7zr模块
  ```python
  pip install py7zr
  ```

  ```python
  # -*- coding:utf8 -*-
  import os
  import zipfile
  from concurrent.futures.thread import ThreadPoolExecutor
  from itertools import repeat

  import py7zr


  class ZipFileUtil:
      def __init__(self):
          self.resource_path = '/Users/chenhongye/Documents/Resource'  # 源文件的父目录，需要指定自己的路径，可全部覆盖重写
          self.target_path = '/Users/chenhongye/Documents/Target'  # 归档或打包压缩后的目录，需要指定自己的路径，可全部覆盖重写

          self.file_paths = []  # 所有源文件路径
          self.executor = ThreadPoolExecutor(10)  # 创建容量为10 的线程池
          self.__init()

      # 初始化
      def __init(self):
          # 创建保存目录
          if not os.path.exists(self.target_path):
              os.mkdir(self.target_path)

      # 获取所有源文件路径
      def __get_file_path(self):
          file_list = os.listdir(self.resource_path)
          self.file_paths = [os.path.join(self.resource_path, video_name) for video_name in file_list]

      # py7zr模块打包归档，支持密码
      def py7z(self, path, pwd=None):
          file_name = os.path.basename(path)
          file_base_name = os.path.splitext(file_name)[0]
          out_full_name = os.path.join(self.target_path,  f'{file_base_name}.7z')
          if pwd:
              with py7zr.SevenZipFile(out_full_name, 'w', password=pwd) as archive:
                  archive.writeall(path, file_name)
          else:
              with py7zr.SevenZipFile(out_full_name, 'w') as archive:
                  archive.writeall(path, file_name)
          return os.path.basename(path)

      # 主入口
      def main(self):
          try:
              self.__get_file_path()
              # 启动线程池
              for data in self.executor.map(self.py7z, self.file_paths, repeat('123456')):
                  print(f'{data}的操作{"成功" if data else "失败"}')
              print('已完成全部操作，程序结束')
          except Exception as e:
              print(e)
          finally:
              self.executor.shutdown()


  if __name__ == '__main__':
      ZipFileUtil().main()

  ```

### 七、归纳总结
* 遇到一个问题，需要学会举一反三去思考来解决它，博主始终相信一句话，问题既然是人类产生的，人类就肯定可以解决，只是时间的问题而已；不过，本文恰好用了三种办法去解决一个小问题，虽然有点小瑕疵，但是总体过得去

* zipfile模块和系统命令都是Python3自带的，不需要额外安装，负责调用即可

* 本文继续使用线程池技术去进行多线程操作多个文件

* 文中涉及的zipfile、py7zr模块还有更多的用法等待挖掘

### 八、注意事项
> zipfile模块归档文件，会一起把相关路径打包进去，可能是博主知识浅薄，还不知道怎么去掉这个路径，这个等有空再研究了

> 执行cmd命令，注意文件路径如果有空格的，记得用“”包裹着，或者把空格转反斜杠+空格，例如`\ `，例如 `"/Users/public/Documents/Resource/a file.txt"`，或者 `/Users/public/Documents/Resource/a\ file.txt`

> Python3自带的zipfile不支持设置密码压缩，但是支持设置密码来解压，其他两个均支持设置密码加解压

> 使用线程池技术为大量文件操作开启多个独立的工作流程

> 线程池map方法传多个参数的时候，需要保证参数的类型和数量保持一致

### 九、相关资源
[Python3 zipfile模块的文档](https://docs.python.org/zh-cn/3.7/library/zipfile.html)

[系统zip命令的常用参数介绍](https://www.cnblogs.com/lesten/p/11603998.html)

[py7zr模块的官网](https://github.com/miurahr/py7zr)

[ZipFileUtil.py文件下载](/static/files/python/ZipFileUtil.py)
