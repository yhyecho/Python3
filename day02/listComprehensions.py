# 列表生成式

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

L1 = list(range(1, 11))
print(L1)

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
L2 = []
for x in range(1, 11):
    L2.append(x * x)

print(L2)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
L3 = [x * x for x in range(1, 11)]
print(L3)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
L4 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L4)

# 还可以使用两层循环，可以生成全排列：
L5 = [m + n for m in 'ABC' for n in 'XYZ']
print(L5)

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

import os # 导入os模块，模块的概念后面讲到
dirL = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(dirL) 

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

# 因此，列表生成式也可以使用两个变量来生成list：
d2 = {'x': 'A', 'y': 'B', 'z': 'C' }
L6 = [k + '=' + v for k, v in d.items()]
print(L6)

# 最后把一个list中所有的字符串变成小写：
L7 = ['Hello', 'World', 'IBM', 'Apple']
L8 = [s.lower() for s in L7]
print(L8)

# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
 
