#print('%\t' *10)
#name = 'bingbing'
#print('b' in name)
# name = 'sixstat'
# print(name[0])
# print(name[-1])
# st = 'abcdefghijk'
# # print(st[0:4])
# # print(st[5:7])
# # print(st[6:])
# # print(st[:5])
# print(st[-1:-6:-1])
#3 字符串常见操作
#3.1 查找

'''find（） 检查某个字符窜是否包含在字符串中，如果有这个字符这返回整个字符串中的字符开始
位置的下表，否则就返回-1
'''

# name = 'bingbing'
# print(name.find('b')) #检测到第一个b，下标为0
# print(name.find('i')) #检测第一个i的下表为1
# print(name.find('ing')) #默认检测字符串中的首字符的下标
# print(name.find('b',3)) #指定某个下标之后开始查找，冰返回下标位
# #可简写print(name.find('b',3))
# print(name.find('b',5)) #超出范围，不包含 返回-1
# print(name.find('b',3,5)) #指定一个范围段，并返回下标位
# print(name.find('b',3,4)) #包前不包后

#index（）find 检查某个字符窜是否包含在字符串中，如果有这个字符这返回整个字符串中的字符开始
#位置的下表，否则就报错，index（字符串，开始位置下标，结束位置下表）
#注意：开始和结束位置下表可以省略，表示在整个字符串中
# test = '我命由我不由天'
# print(test.index('命')) # 1
# #print(test.index('命',2)) # 报错，从下表2开始找，没有找到
# print(test.index('命',1,2)) # 1

'''
count()，返回某个字符串在整个字符串中出现的次数。没有就返回0,
count(字符串，开始位置下标，结束位置下表）
注意：开始和结束位置下标可以省略，表示在整个字符串中查找
'''
# name = 'bingbingb'
# print(name.count('b')) # 3
# print(name.count('a')) # 0
# print(name.count('b',4)) #2 冲下标位置开始找
# print(name.count('b',1,5)) # 1 从下标1开始到下标6中间找
