#aaa
'''
1,startswith(),是否以某个字符串开头，是的话就返回true,不是就返回false,如果设置开始和结束位置
则在指定范围内查找
2,endswith(),是否已某个字符串结尾，是就返回True，不是就返回False,如果设置开始和结束位置
则在指定范围内查找
endswith(字符串，开始位置下标，结束位置下标）

3，isupper().检测字符串中所有的字母是否都为大写，是的话为True,不是为flase
'''
st = 'sixster'
print(st.startswith('six'))  # True
print(st.startswith("sex"))  #flase
print(st.startswith('sis',0,4)) #True


