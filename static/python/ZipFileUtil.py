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

    # zipfile模块打包归档，只支持设置提取密码
    def zip(self, path):
        file_base_name = os.path.splitext(os.path.basename(path))[0]
        with zipfile.ZipFile(os.path.join(self.target_path, f'{file_base_name}.zip'), 'w') as f:
            f.write(path)
        return os.path.basename(path)

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
            # for data in self.executor.map(self.zip, self.file_paths):
            #     print(f'{data}的操作{"成功" if data else "失败"}')
            # print('已完成全部操作，程序结束')

            # for data in self.executor.map(self.cmd_file, self.file_paths, repeat('123456')):
            #     print(f'{data}的操作{"成功" if data else "失败"}')
            # print('已完成全部操作，程序结束')

            for data in self.executor.map(self.py7z, self.file_paths, repeat('123456')):
                print(f'{data}的操作{"成功" if data else "失败"}')
            print('已完成全部操作，程序结束')
        except Exception as e:
            print(e)
        finally:
            self.executor.shutdown()


if __name__ == '__main__':
    ZipFileUtil().main()
