# for 循环打印list中的元素
names = ['Echo', 'Bob', 'Meng']
for name in names:
    print(name)

# 计算1到10的和
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# range()函数生成整数序列
# list(range(5)) 转换成list
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break 跳出整个循环
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

# continue 跳出当次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
         continue
    print(n)
