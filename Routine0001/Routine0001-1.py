# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/shifanfashi/article/details/89383115
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
"""

import base64
import pysnooper

# 通过id检验优惠券是否存在，通过goods查找商品
coupon = {
    'id': '1234',
    'goods': '0001',
}


@pysnooper.snoop()
def gen_coupon(id, goods):
    coupon['id'] = id
    coupon['goods'] = goods
    raw = '/'.join([k + ':' + v for k, v in coupon.items()])
    raw_64 = base64.urlsafe_b64encode(raw.encode('utf-8'))
    c_code = raw_64.decode()
    return c_code


def save_coupon(c_code):
    with open('coupon.txt', 'a+', encoding="utf-8") as file:
        file.write('优惠码:' + c_code + '\n')


def gen_all():
    for i in range(1000, 1200):
        c_code = gen_coupon(str(i), str(int(i/2)))
        save_coupon(c_code)


if __name__ == '__main__':
    gen_all()