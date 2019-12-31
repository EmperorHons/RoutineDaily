# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/shifanfashi/article/details/89394026
第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
"""
from PIL import Image
# PIL是Python Imaging Library 是图像存档和批处理应用程序的理想选择。您可以使用该库创建缩略图，在文件格式之间进行转换，打印图像等。
import os.path
# os.path 模块主要用于获取文件的属性
import pysnooper


@pysnooper.snoop()
def Size(dirPath, size_x, size_y):
    f_list = os.listdir(dirPath)

    for i in f_list:
        if os.path.splitext(i)[1] == '.png' \
                or os.path.splitext(i)[1] == '.jpg' \
                or os.path.splitext(i)[1] == '.bmp' \
                or os.path.splitext(i)[1] == '.jpeg' \
                or os.path.splitext(i)[1] == '.gif' \
                or os.path.splitext(i)[1] == '.psd' \
                or os.path.splitext(i)[1] == '.tiff' \
                or os.path.splitext(i)[1] == '.tga' \
                or os.path.splitext(i)[1] == '.eps':
            img = Image.open(os.path.join(r'E:\Jetbrains\Projects\RoutineDaily\Routine0005\Wallpaper', i))
            img.thumbnail((size_x, size_y))

            img.save(i)
            print(i)


Size(r'E:\Jetbrains\Projects\RoutineDaily\Routine0005\Wallpaper', 1136, 640)
