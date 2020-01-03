# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/shifanfashi/article/details/89420656
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
"""
import os
import pysnooper
import re


@pysnooper.snoop()
def main():
    num_code = 0
    num_empty = 0
    num_note = 0

    os.chdir(r'E:\Jetbrains\Projects\RoutineDaily\Routine0007')
    # os.chdir() 方法用于改变当前工作目录到指定的路径。

    f = open('Routine007.py', encoding='utf-8')
    read_f = f.readlines()
    f.close()
    # 获取全部代码

    pattern = '.*#'  # 正则表达式

    for i in read_f:
        if "#" in i:
            if re.findall(pattern, i)[0][:-1].isspace() or re.findall(pattern, i)[0][:-1] == "":
                num_note += 1
            else:
                num_code += 1
        elif i.isspace():
            # isspace() 方法检测字符串是否只由空格组成。
            num_empty += 1
        else:
            num_code += 1

    print('the number of code is %d' % (num_code + num_empty + num_note))
    print('the number of empty is %d' % num_empty)
    print('the number of note is %d' % num_note)
    return


if __name__ == '__main__':
    main()
