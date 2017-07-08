# 数据类型 list是一种有序的集合可以随时添加和删除其中的元素
classmates = ['Echo', 'Zhang', 'Meng']
print(classmates)
print(len(classmates))
print(classmates[2])
print('获取list中的最后一个元素', classmates[-1])

# append末尾添加
classmates.append('Shuo')
print(classmates)

# insert指定位置添加
classmates.insert(1, 'Ai')
print(classmates)

# pop() 删除末尾的元素
classmates.pop()
print(classmates)

# pop(i) 删除指定位置上的元素
classmates.pop(2)
print(classmates)

classmates[0] = 'Yu'
print(classmates)

#list里面的元素数据类型也可以不同
L = ['Apple', 123, True]
print(L)

# list元素也可以是另一个list比如
s = ['python', 'java', ['asp', 'php'], 'shcema']
print(len(s))

p = ['asp', 'php']
p2 = ['python', 'java', p, 'schema']
print(p2[2][1])



