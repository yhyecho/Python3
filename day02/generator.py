# 生成器
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

print(next(g))
print(next(g))
print(next(g))

# 我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

# 正确的方法是使用for循环，因为generator也是可迭代对象：
print('--------')
g2 = (x * x for x in range(10))
for n in g:
    print(n)

# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# a, b = b, a + b 
# 相当于
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
fib(6)

