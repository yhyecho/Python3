#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 计算机中8比特＝1字节 一个英文字符占1个字节，一个中文字符占2～4个字节
print('ord()函数获取字符的整数表示')
print(ord('A'))
print(ord('中'))

print('chr()函数把编码转换为对应的字符')
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')

# 编码的发展 ASCII -> Unicode -> utf-8
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes 例如
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode(ascii)) 无法编码，超出ASCII编码的范围

# 把bytes变为str
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 计算str包含多少个字符 可以用len() 函数
print(len('ABC'))
print(len('中文'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 格式化 %d整数  %f浮点数  %s字符串  %x十六进制整数
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 10000))
print('growth rate: %d%%' % 7)

