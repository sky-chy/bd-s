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