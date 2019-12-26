# -*- coding: utf-8 -*-


import random
import redis
from tqdm import tqdm
from time import sleep

r = redis.Redis(host='localhost', port=6379, db=0)

list = []
# 生成26个大写字母
for x in range(65, 91):
    a = str(chr(x))
    list.append(a)
# 生成26个小写字母
for x in range(97, 123):
    a = str(chr(x))
    list.append(a)
# 生成10个数字
for x in range(10):
    list.append(str(x))


# 生成16位激活码
def gen_code():
    s = ''
    for x in range(16):
        a = random.choice(list)
        s = s + a
        # print(s)
    return s


# 生成200个激活码
for x in tqdm(range(200), desc="执行进度", ncols=50):
    code = gen_code()
    r.set(x, code)
    sleep(0.01)

print('执行完毕')
