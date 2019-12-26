# -*- coding: utf-8 -*-


from tqdm import tqdm
from time import sleep
from random import choice
import string
import pymysql.cursors
import pysnooper
from termcolor import colored


@pysnooper.snoop('log.txt')
def get_code(dict, length, count):
    # 根据给定字典，长度来得出激活码
    print(colored("开始执行", 'green'))
    for i in tqdm(range(1, int(count) + 1), desc='执行进度', ncols=100):
        code = ""
    # 通过count限制激活码个数，循环调用choice来计算激活码
        for l in range(0, int(length)):
            code = code + str(choice(dict))
        save_to_mysql(i, code)
        sleep(0.01)
    print(colored("执行完毕", 'blue'))


def save_to_mysql(id, code):
    # 将数据保存到MySQL数据库
    host = ("localhost")
    user = ("root")
    pass_ = ("root")
    db = ("test")
    # 设置数据库连接相关信息
    connect = pymysql.connect(host, user, pass_, db)
    cursor = connect.cursor()
    # 链接数据库并设置游标
    sql = "insert into activeCode(id, code) values ('%d', '%s')"
    data = (id, code)
    cursor.execute(sql % data)
    connect.commit()  # sql执行后必须提交才能存入数据库
    # cursor.close()
    connect.close()
    # 执行sql语句


if __name__ == '__main__':
    dict = string.ascii_letters[:]
    # 设定字典为'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = input("请输入激活码个数：")
    if count == "":
        count = "1"
    length = input("请输入激活码长度：")
    if length == "":
        length = "8"
    get_code(dict, length, count)
