# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/shifanfashi/article/details/89384666
第 Routine0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
"""

from PIL import Image, ImageDraw, ImageFont


def add_num(image):
    draw = ImageDraw.Draw(image)  # 建立画布
    font = ImageFont.truetype('arialuni.ttf', size=50)  # 调用本地字体本地字体
    fillcolor = '#f0000f'  # 红色
    width, height = image.size
    draw.text((width - 60, 0), '14', font=font, fill=fillcolor)  # 确定字体大小，画上 15
    image.save('result-1.jpg', 'png')  # 保存图片
    # return 0


if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)
