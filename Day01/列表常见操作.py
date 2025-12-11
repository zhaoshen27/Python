'''
一，列表的操作
1.1添加元素
append(),extend(),insert()
'''
li = ['oen','two','three']
# print(li)
# li.append('four')   #append 在变量中添加元素，整体添加
# print(li)
# li.extend('five')   #extend 分散添加，将一个类型中的元素逐一添加，extend对下要用可迭代对象，否则会报错
# print(li)
# li.extend(4)
# print(li)    #执行将会报错 TypeError: 'int' object is not iterable
# li.insert(3,'one') #insert 指定下表位置添加，在下表位置添加元素，如果下标位有元素，原有的将会后移
# print(li)

'''1.2 修改元素'''
# 直接修改,通过下表可以直接进行修改
# li = [1,2,3]
# print(li[1])  #打印下标对应的字符
# li[1] = 'a'     #指定下标位用 a 替换
# print(li)     # 1 a 3

'''1.3查询'''
