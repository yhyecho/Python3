# 另一种有序列表叫元组tuple,tuple和list非常类似,但是tuple一旦初始化就不能修改,更安全
# tuple 所谓的不变，并不是值不变，而是指向不变
t = (1, 2)
print(t)

# 定义一个元素的元组时，一定要有逗号(1,) 避免和数学运算中的小括号()产生歧义
t2 = (1)
t3 = (1,)
print(t2)
print(t3)

# 定义一个包含list的tuple, tuple中的list的内容可以改变
tlist = ('a', 'b', ['A', 'B'])
print(tlist)
tlist[2][0] = 'X'
tlist[2][1] = 'Y'
print(tlist)

# 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
