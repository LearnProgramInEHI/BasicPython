# 递归函数
'''
一个函数在内部调用自己本身，就是递归函数。
递归函数的一个缺点就是会栈溢出？这个时候要使用 “尾递归” 的方式进行优化。目前python还没有实现尾递归优化

什么是尾递归优化？
调用函数 ===> 内存增加一层的栈 ===> 函数返回 ===> 内存减少一层栈 ===> 不断递归就不断增加，最后溢出
尾递归：
调用函数 ===> 内存增加一层栈 ===> 最后返回自己后面就没有语句执行了，这一层的内存释放,永远只保存一层栈
'''
# 实现斐波那契数列
def f(n):
    if n <= 1:
        return n
    return f(n-1)+f(n-2)
        
a = f(10)
print(a)

# 实现斐波那契数列,输入n，显示斐波那契数列的前n个数.

def fact(n):
    l = [0]
    a= 0
    b = 1
    for i in range(n):
        a,b = b,a+b
        l.append(a)
    return l

f = fact(10)
print(f)
        
# 汉诺塔
def move(n,a,b,c):
    if n == 1:
        print(a,'==>',c)
    else:
        move(n-1,a,c,b)
        print(a,'==>',c)
        move(n-1,b,a,c)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')
# 计算阶乘
def f(n):
    if n ==1:
        return 1
    return n*f(n-1)

print(f(150))