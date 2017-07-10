# sorted
# 排序算法

# Python内置的sorted()函数就可以对list进行排序：

L1 = sorted([36, 5, -12, 9, -21])
print(L1)

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
L2 = sorted([36, 5, -12, 9, -21], key=abs)
print(L2)

# 字符串排序
L3 = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(L3)

L4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(L4)

L5 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(L5)

# 从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
