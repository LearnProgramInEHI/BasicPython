# 函数的参数
'''
位置参数
默认参数，指向不变对象
可变参数
关键字参数
'''
# 可变参数
def add(*args):
    s = 0
    for i in args:
        s+=i
    return s

r = add(1,2,3,4,5,6,7,9,10)
print(r)

# 关键字参数
def score(**kw):
    for k,v in kw.items():
        print(k,'=====>',v)

score(johnw=100,michael=90)

# 解包
a = [1,2,3,4,5]
print(*a)

# 原理
'''
可变参数，将传进去的参数一个个加入一个tuple，然后在进行运算
关键字参数，将传进去的参数一个个组成一个dict，然后在运算
默认参数以位置参数为准，如果这个位置有值，那么会覆盖默认参数。
'''

# 练习
'''
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x,y):
    return x*y
'''
def product(*args):
    if len(args) == 0:
        raise TypeError()
    s = 1
    for i in args:
        s = s*i
    return s

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


