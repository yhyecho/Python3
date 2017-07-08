# python 内置了字典dict 其他语言中为map,使用键－值(key-value),具有极快的查找速度

d = {'Echo': 95, 'Bob': 75, 'Meng': 65}
print(d['Meng'])

d['Ai'] = 66
print(d)

d['Ai'] = 67
print(d['Ai'])

print('Da' in d)

print('Ai' in d)

print(d.get('Da'))

print(d.get('Da',-1))

print(d.pop('Ai'))

print(d)

# 和list比较,dict有以下几个特点：
# 1. 查找和插入的速度极快，不会随着key的增加而变慢
# 2. 需要占用大量的内存, 内存浪费多

# list特性
# 1. 查找和插入的时间随着元素的增加而增加
# 2. 占用空间小，浪费内存很少
# 所以dict是用空间换取时间的一种方法

# Set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

s = set([1, 2, 3])
print(s)

# 重复元素在set中自动被过滤
s2 = set([1, 1, 2, 2, 3, 3])
print(s2)

s.add(4)
print(s)
s.add(4)
print(s)

s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作

s3 = set([1, 2, 3])
s4 = set([2, 3, 4])
s5 = s3 & s4
print(s5)
s6 = s3 | s4
print(s6)
