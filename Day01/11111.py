'''
1,修改元素
replace():替换
replace(旧内容，新内容，替换次数）
注意：替换次数可以省略，默认全部替换
'''
# name = '好好学习，天天向上'
# print(name.replace('天','时')) #好好学习，时时向上
# print(name.replace('天','时',1)) #好好学习，时天向上，数字1代表只替换一个
'''
2,split();指定分隔符来切换字符串
'''
# st = 'hello,python'
# print(st.split(',')) #['hello','python'] 以逗号作为分割符，并且打印出来的带中括号，这个逗号是字符串中有的
# print(st.split('a')) #['hello,python']，变量中没有 a,所以无法找的以a为参数来进行分割
# print(st.split('o')) #['hell', ',pyth', 'n'] 以变量中的o为分隔符进行分割
# print(st.split('o',1)) #['hell', ',python'] 指定只分割1次

'''
3,capitalize();第一个字符大写
'''
# name = 'bingbing'
# print(name.capitalize())

'''
4,lower();大写字母转换为小写
5，upper();小写字母转为小写

'''
# st = 'aBcD'
# print(st.lower()) #abce
# print(st.upper()) #ABCD
