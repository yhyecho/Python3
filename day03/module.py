#1. 模块
# Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。

# 我们以内建的sys模块为例，编写一个hello的模块：

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'HuaYang Yu'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()

# 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
# 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；


# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：

# 运行python3 hello.py获得的sys.argv就是['hello.py']；

# 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。

# 最后，注意到最后两行代码：

# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

# 2.作用域

# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
# 似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

# private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
# 调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法
