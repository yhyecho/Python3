# 偏函数

# 绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。

# int() 函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：

# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：

num = int('12345', base=8)
print(num)

num2 = int('12345', 16)
print(num2)

def int2(x, base=2):
    return int(x, base)

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：

import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))

# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
