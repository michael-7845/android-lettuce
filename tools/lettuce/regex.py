# -*- coding: utf-8 -*- 
import re

# text模式, 文本
# 类似格式的表达式: 【"xyz123"】, xyz123为text值
# 其中, ""中间的字符串被提取为text值, 中间的字符不能为"
mode_text = ur'"([^"]+)"' #ur'([^\s]+)'
# int模式, 整数
# 无符号整数的表达式: 如【123】或【7】
mode_int = ur'(\d+)'
# position模式, 坐标
# 无符号整数形成的坐标的表达式: 如【8,10】
# 其中, 8为x坐标, 10为y坐标
mode_position = ur'(\d+),(\d+)'
# word模式, 单词
# a-z/A-z/_形成的单词的表达式: 如【supermarket】
mode_word = ur'(\w+)'
# keycode模式, 键码
# 格式0x的十六进制表达式: 如【0x3E】或【0xFF】
# 以后可能会使用整数, 不再使用键码.
mode_keycode = ur'(0x[\da-fA-F]+)'
# file模式, 文件路径名
# 非@字符组成的字符串,请满足日常文件路径/目录路径/文件名/目录名要求: 如【123.txt】或【/sdcard/123.txt】
mode_file= ur'([^@]+)'
mode_activity=mode_file

# pv, 即property-value简写.
# mode_validch, pv表达式中的合法字符:除了1. 空白字符（如空格／回车／制表等不会被打印显示的字符）2. 英文逗号, 3. 英文等号=, 其他的都认为是pv表达式的合法字符
mode_validch = ur'(?:[^\s,=])'
# pv表达式
# 类似以下格式的等式,中间用英文等号分隔: xxx=yyy,aaa=bbb,...
# 其中, x/y/a/b有前面定义的validch组成
mode_pvs = ur'((?:%s+=%s+[,]?)+)' % (mode_validch, mode_validch) # property=value,...的正则表达式
# [代码扩展用到]提取pv表达式为各个等式的正则表达式, 普通feature文件撰写不会用到.
mode_pv_sentence = ur'(%s+=%s+)[,]?' % (mode_validch, mode_validch)
# [代码扩展用到]从pv表达式分解为p和v的正则表达式, 普通feature文件撰写不会用到.
mode_pv_extract = ur'(%s+)=(%s+)' % (mode_validch, mode_validch)

#mode_int_coor = ur'((\d+)[,]?)+' #废弃

def get_dict_from_cond(cond):
    regex_cond = re.compile(mode_pv_sentence)
    t = regex_cond.findall(cond)
    regex_kv = re.compile(mode_pv_extract)
    dict = {}
    for s in t:
        m = regex_kv.match(s)
        if m is not None: 
            dict[m.group(1)] = m.group(2)
    return dict
