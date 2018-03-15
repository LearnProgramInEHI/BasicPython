# dict
'''
dict是key和value映射组合，也叫做字典
常用的几个方法
items： 循环取出key和value
keys: 只取出key
values： 之取出value
pop: 删除一个值

'''
classMate= {'johnw':100,'jack':90,'michael':80}
for k,v in classMate.items():
    print(k,'====>',v)
    
classMate.pop('johnw')
print(classMate)

# set 存储key，都是不可变对象,无重复对象，可以看做集合
print(set([1,2,3]))
print({1,2,3,4})
