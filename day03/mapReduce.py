# map/reduce
# Python内建了map()和reduce()函数

# 1. map
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

L = list(r)
print(L)

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

# 不需要map()函数，写一个循环，也可以计算出结果：

L2 = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L2.append(f(n))
print(L2)

# 的确可以，但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？

# 把这个list所有数字转为字符串：
L3 = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L3)

# reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

# 比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
def add(x, y):
    return x + y

L4 = reduce(add, [1, 3, 5, 7, 9])
print(L4)

# 把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x, y):
    return x * 10 + y

L5 = reduce(fn, [1, 3, 5, 7, 9])
print(L5)

# 假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！
