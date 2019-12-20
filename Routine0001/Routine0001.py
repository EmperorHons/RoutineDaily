# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/shifanfashi/article/details/89383115
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
"""

import base64  # 二进制编码方法
import pysnooper

# 通过id检验优惠券是否存在，通过goods查找商品
coupon = {
    'id': '1234',
    'goods': '0001',
}


# 生成优惠码
@pysnooper.snoop()  # 打印代码执行过程
def gen_coupon(id, goods):
    coupon['id'] = id
    coupon['goods'] = goods

    raw = '/'.join([k + ':' + v for k, v in coupon.items()])  # coupon.items()返回可遍历的(键,值)元组数组,此处返回id与goods组合

    raw_64 = base64.urlsafe_b64encode(raw.encode('utf-8'))  # 将 raw增加 utf-8 编码格式，然后进行二进制格式编码

    c_code = raw_64.decode()  # 解utf-8编码

    return c_code


# 将优惠码保存至coupon.txt
def save_coupon(c_code):
    with open('coupon.txt', 'a+', encoding="utf-8") as file:
        file.write('优惠码:' + c_code + '\n')


# 循环200次
def gen_all():
    for i in range(1000, 1200):
        c_code = gen_coupon(str(i), str(int(i/2)))
        save_coupon(c_code)


if __name__ == '__main__':
    gen_all()
