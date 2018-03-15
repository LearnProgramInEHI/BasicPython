# 第一个程序
print('Hello world')

# 整数不能和字符串相加
'''
print(1+'2')  #TypeError: unsupported operand type(s) for +: 'int' and 'str'

'''
# 浮点数和整数会相互转换
print(1.0+2)

# 整数和布尔值可以相加，True = 1 False = 0
print(1+True)
print(True == 1)
print(False == 0)

# 字符编码问题
'''
python 文件开头习惯写如下字符
#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''

# 输出格式化字符
print('Hello %s'%('johnw',))
print('Hello {0}'.format('world'))


