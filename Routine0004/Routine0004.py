# -*- coding: utf-8 -*-
"""
每天一个python小程序 0004：任一个英文的纯文本文件，统计其中的单词出现的个数
https://blog.csdn.net/shifanfashi/article/details/89384607
"""
import re

file_name = 'Snow Adopted After the Tune of Chin Yuan Chun.md'

lines_count = 0  # 单词数
words_count = 0  # 行数
chars_count = 0  # 字母数
words_dict = {}
lines_list = []

with open(file_name, 'r', encoding='utf-8') as f:
    for line in f:
        lines_count = lines_count + 1
        chars_count = chars_count + len(line)
        match = re.findall(r'[^a-zA-Z0-9]+', line)
        for i in match:
            # 只保留英文单词，删除其他字符
            line = line.replace(i, ' ')
        lines_list = line.split()
        for i in lines_list:
            if i not in words_dict:
                words_dict[i] = 1
            else:
                words_dict[i] = words_dict[i] + 1

print('words_count is', len(words_dict))
print('lines_count is', lines_count)
print('chars_count is', chars_count)

for k, v in words_dict.items():
    print(k, v)
