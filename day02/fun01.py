# Python内置了很多有用的函数,我们可以直接调用

# abs()
print(abs(100))
print(abs(-20))
print(abs(12.34))

# max()
print(max(1,2))

# 数据类型转换
# int()
print(int('123'))

# float()
print(float('12.34'))

# str()
print(str(100))

# bool()
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

a = abs # 变量a指向abs函数
c = a(-1) # 所以也可以通过a调用abs函数
print(c)

# 调用Python的函数，需要根据函数定义，传入正确的参数。如果函数调用出错，一定要学会看错误信息，所以英文很重要！
