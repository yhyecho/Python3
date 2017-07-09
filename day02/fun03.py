# 函数的参数

# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了


# 位置参数
def power(x):
    return x * x


def power2(x, n):
    s = 1
    while n > 0:
        n = n - 1 
        s = s * x
    return s

print('2^4 = ', power2(2, 4))

# 默认参数
def power3(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print('2^2 = ', power(2))

def enroll(name, gender, age=6, city='nanjing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1, 2, 3]))

print(add_end(['x', 'y', 'z']))

print(add_end())
print(add_end())
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 但是调用的时候，需要先组装出一个list或tuple：
print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))


def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc2(1, 2))
print(calc2())

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print(calc2(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Echo', 25, gender='M', job='Programer')

extra = {'city': 'nanjing', 'job': 'Engineer'} 
person('Jack', 24, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。



