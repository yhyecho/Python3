# def定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
# return None可以简写为return

print(my_abs(-10))

# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass

# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

# 参数检查

def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs2('A'))

# 返回多个值

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print(move(100, 100, 60, math.pi / 6))

# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# 函数可以同时返回多个值，但其实就是一个tuple

