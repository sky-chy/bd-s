---
layout: post
title: 使用opencv-python对视频进行指定帧画面保存
categories: [Python3,opencv-python]
description: 使用opencv-python对视频进行指定帧画面保存
keywords: Python教程, Python3教程, opencv-python, 视频处理, 帧画面, 自媒体, 保存图片
---

### 一、情景导入
最近我有位搞短视频的朋友跟我说，他上传视频到短视频平台，最后选择封面的时候，感觉那些平台给出来的截图有点鸡肋，但是又不想自己去看完视频来截取封面图片，问问我有没有什么办法可以让多个视频快速产生多张图片，最好是随机产生的，还需要可以自由控制生成数量的，话不多说，搞起！

### 二、关键词
多个视频、随机产生、多张图片、快速、数量

### 三、分析思路
众所周知，视频是由一帧一帧的图片组合而成的，根据上述情景和关键词得知，需要对多个视频进行多张随机指定帧位置的画面来保存，所以得对源视频进行总帧数获取，在视频总帧数的前提下创建随机帧位置数值的数组，对视频进行帧画面判断是否在集合中，如果在随机帧位置数值的集合中，则保存下来。同时也有要求多个视频快速截取，所以得使用多线程技术

### 四、工具环境
+ Python 3.7.0
+ opencv-python 4.5.1.48
+ PyCharm 2019.1.2
+ MacOS 10.15.7

### 五、实现步骤
1. 首先获取到视频的路径，假设源视频的路径的变量为`video_paths`;
1. 之后使用`ThreadPoolExecutor`来创建线程池，并对每个视频进行独立线程操作，假设线程池的变量为`executor`；
1. 创建归档后的目标文件夹
1. 之后使用`opencv-python`模块的获取源视频总帧数，假设源视频总帧数的变量为`video_frame_sum`;
1. 之后使用`random`模块在`video_frame_sum`的基础上去获取指定数量的随机数的数组，假设指定数量的变量为`random_num`，生成`random_num`个随机数并整合到数组的变量为`frame_position`;
1. 之后使用`opencv-python`模块对源视频进行帧位置判断是否在`frame_position`这个数组中，如果成立，便将该帧画面保存到硬盘;

### 六、实操代码

在终端上面执行以下命令安装opencv-python模块

```python
pip install opencv-python
```

```python
# -*- coding:utf8 -*-
import os
import random
import cv2

from concurrent.futures.thread import ThreadPoolExecutor

class CaptureUtil:
    # 初始化
    def __init__(self):
        self.resource_path = '/Users/你的用户名/Documents/Resource'  # 视频的父目录，需要指定自己的路径，可全部覆盖重写
        self.target_path = '/Users/你的用户名/Documents/Target'  # 保存帧画面的目录，需要指定自己的路径，可全部覆盖重写

        self.video_paths = []  # 所有源视频路径
        self.executor = ThreadPoolExecutor(10)  # 创建容量为10 的线程池
        self.random_num = 3  # 指定获取帧画面的数量
        self.quality = 70  # 保存jpg格式帧画面的质量，数值越高，质量越好，范围1-99
        self.__init()

    # 初始化
    def __init(self):
        # 创建保存帧画面的目录
        if not os.path.exists(self.target_path):
            os.mkdir(self.target_path)

    # 获取源视频路径
    def __get_video_paths(self):
        video_list = os.listdir(self.resource_path)
        self.video_paths = [os.path.join(self.resource_path, video_name) for video_name in video_list]

    # 获取视频总帧数
    def __get_video_frame_sum(self, path):
        capture = cv2.VideoCapture(path)
        if not capture.isOpened():
            return os.path.basename(path), False
        video_frame_sum = capture.get(cv2.CAP_PROP_FRAME_COUNT)  # 视频文件的帧数
        self.__capture_video(capture, video_frame_sum, path)
        return os.path.basename(path), True

    # 对视频进行随机抽帧
    def __capture_video(self, capture, video_frame_sum, path):
        frame_num = 0  # 以获取的帧画面数量
        frame_index = 0  # 帧画面迭代位置
        frame_position = [random.randint(10, video_frame_sum) for _ in range(self.random_num)]  # 需要获取的随机帧位置
        file_name = os.path.splitext(os.path.basename(path))[0]  # 文件名称
        print(f'正在对{file_name}查找需要保持的帧画面...')
        while True:
            success, frame = capture.read()
            if not success or frame_num == self.random_num:
                break

            frame_index += 1
            if frame_index - 1 in frame_position:
                saved_name = f'{self.target_path}{os.sep}{file_name}{frame_index}.jpg'
                print(f'正在保存{saved_name}')
                saved_path = os.path.join(self.target_path, saved_name)
                cv2.imwrite(saved_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), self.quality])
                frame_num += 1
        capture.release()

    # 主入口
    def main(self):
        try:
            self.__get_video_paths()
            # 启动线程池
            for data in self.executor.map(self.__get_video_frame_sum, self.video_paths):
                print(f'{data[0]}的抽帧操作{"成功" if data[1] else "失败"}')
            print('已完成全部操作，程序结束')
        except Exception as e:
            print(e)
        finally:
            self.executor.shutdown()


if __name__ == '__main__':
    CaptureUtil().main()
```
### 七、归纳总结
* 从Python3.2开始，标准库为我们提供了concurrent.futures模块，它提供了ThreadPoolExecutor和ProcessPoolExecutor两个类，实现了对threading和multiprocessing的进一步抽象（这里主要关注线程池），不仅可以帮我们自动调度线程，还可以做到：

    * 主线程可以获取某一个线程（或者任务的）的状态，以及返回值；

    * 当一个线程完成的时候，主线程能够立即知道；

    * 让多线程和多进程的编码接口一致；

    * 本文使用map函数来进行线程池操作，最终结果是按顺序返回的，此非硬性要求；

* opencv是一个强大的图像处理和计算机视觉库，opencv-python是opencv的一个Python分支：

    * 启动线程池后，每个线程均会独立操作一个视频，代码如下：

    ```python
    ...
    # 启动线程池
    for data in self.executor.map(self.__get_video_frame_sum, video_paths):
    ...
    ```

    * 先使用VideoCapture函数加载相关路径的源视频，代码如下：

    ```python
    ...
    capture = cv2.VideoCapture(path)
    ...
    ```

    * 再去获取该视频的总帧数，代码如下：

    ```python
    ...
    video_frame_sum = capture.get(cv2.CAP_PROP_FRAME_COUNT)  # 视频文件的帧数
    ...
    ```

    * 之后在无限循环中找到需要保存的帧画面位置

    * 最后使用imwrite函数对找到的帧画面进行保存，代码如下：

    ```python
    ...
    cv2.imwrite(saved_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), self.quality])
    ...
    ```

* os模块相关操作：

    * os.path.exists 是判断一个路径是否存在，需要绝对路径

    * os.mkdir 是创建目录，需要绝对路径

    * os.path.join 是拼接一个或多个路径部分

    * os.path.basename 是获取路径下的文件名称

    * 更多说明，请参考[相关资源](#九相关资源)的Python3 os.path模块文档

* random模块产生一个数组的随机数：

    * 使用randint函数结合for循环产生指定数量内的数值，代码如下：
    
    ```python
    ...
    frame_position = [random.randint(10, video_frame_sum) for _ in range(self.random_num)]  # 需要获取的随机帧位置
    ...
    ```

### 八、注意事项
> 安装库时别混淆python-opencv2和opencv-python两个库

> 使用opencv-python库时，注意是导入cv2 ，代码：```import cv2```

### 九、相关资源
[Python3 os.path模块文档](https://docs.python.org/zh-cn/3.7/library/os.path.html)

[CaptureUtil.py文件下载](/static/files/python/CaptureUtil.py)
