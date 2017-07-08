# 不可变对象
# 之前我们讲了, str是不变对象，而list是可变对象

a = ['c', 'b', 'a']
a.sort()
print(a)

s = 'abc'
obj = s.replace('a', 'A')
print(s)
print(obj)

# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

# 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

