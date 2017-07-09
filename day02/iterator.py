# 迭代器
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型, 如list, tuple, dict, set, str 等
# 一类是generator,包括生成器和带yield的generator function

# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

# 可以使用isinstance()判断一个对象是否是Iterator对象：

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

from collections import Iterator
isinstance(iter([]), Iterator)
isinstance(iter('abc'), Iterator)

# 凡是可作用于for循环的对象都是Iterable类型；

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]
    pass

# 完全等价于
# 首先获得Iterator对象
it = iter([1, 2, 3, 4, 5])
# 循环
while True:
    try:
        #获得下一个值：
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

