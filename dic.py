#字典
#dic
#dictionary 字典 也是用來裝東西的
# a = []  清單
# b = {}  字典
# 一個叫作words的字典，裡面裝了兩個東西，東西之間要用 ',' 隔開
# 這個東西，就是在words這個字典裡面去查詢，是否有apple這個東西
# 整體這個架構，就是有「配對」的意味
#
# 字典 = { key#1:值#1 , key#2:值#2, ...}


words = {
	
	'apple' : '蘋果' ,
	'banana': '香蕉'
}

print(words['apple'])

words['tea'] = '茶' # 如果有等號,等於要新增key，可以用這樣的方式

print(words['tea'])
print(words)


# print(words['pinapple']) 如果我執行一個不存在的 key
#--------------------------------------------------
#Traceback (most recent call last):
#  File "C:\Users\allenlee\Desktop\coding\dic.py", line 20, in <module>
#    print(words['pinapple'])
#          ~~~~~^^^^^^^^^^^^
#KeyError: 'pinapple'
#--------------------------------------------------


def fun1():
	test1 = [1,2,3,4,5,6,7,8,9,10]
	test2 = ['a','b','c','d','e','f','g','h','i','j']

	x = input('請輸入x: ')
	x = int(x)
	y = input('請輸入y: ')
	y = int(y)

	if x > 0 and y > 0:
		A = {test1[x-1]:test2[y-1]}
		print(A)
	elif x > 10 and y >10:
		print('請輸入小於等於10的數')
	else:
		print('不可輸入小於等於0的術')

def fun2():
	test1 = [ [1,'a'],[2,'b'],[3,'c'],[4,'d'] ]

	x = input('請輸入x, 可以得到對應的答案: ')
	x = int(x)

	if x > 0:
		A = {test1[x-1][0]:test1[x-1][1]}
		print(A)
	elif x > 5:
		print('請輸入小於等於4的數')
	else:
		print('不可輸入小於等於0的術')


