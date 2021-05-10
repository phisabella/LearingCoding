#!/usr/bin/python3
import re
if __name__ == '__main__':
    line = "Cats are smarter than dogs"
    # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
    # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
    matchObj = re.match(r'(.*) are (.*?) .*', line)

    if matchObj:
        print("matchObj.group() : ", matchObj.group())
        print("matchObj.group() : ", matchObj.group(0))
        print("matchObj.group(1) : ", matchObj.group(1))
        print("matchObj.group(2) : ", matchObj.group(2))
    else:
        print("No match!!")

    print('===================')

    # !/usr/bin/python3
    import re

    phone = "2004-959-559 # 这是一个电话号码"

    # 删除注释
    num = re.sub(r'#.*$', "", phone)
    print("电话号码 : ", num)

    # 移除非数字的内容
    num = re.sub(r'\D', "", phone)
    print("电话号码 : ", num)