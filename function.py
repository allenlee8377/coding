#function 函式/功能
#function 式用來 [收納] 程式碼的東西
# 他是一個功能，功能不是執行
# 例如我設計一個按鈕，但我沒有按他，但他有功能

def wash():
	print('加水')
	print('加洗衣精')
	print('旋轉')

wash()

#-------------------
#wash() 收納了這三行程式碼
#
#單獨跑到 wash() 就會執行 收納進去的程式碼
#
#-------------------
print('\n以下執行三次 wash，等於執行 9行程式碼，所以這個東西就是用來模組化\n')
wash()
wash()
wash()
print('\n')

def say_hi(girl):
	print('hi')
	print('hi^^')
	if girl:
		print('安安你好')

#say_hi()
say_hi(True)
say_hi(False)

#-----------------------------
# parameter 參數，可以把say_hi()的()填入參數
# 有點像投幣孔
# **** 如果funcrion要使用到外部的東西，通常這件事情比較不好。
#-----------------------------

print('\n')
print('\n')
dry = True
def wash2(dry = False, water = 8):
	print('加水',water,'分滿')
	print('加洗衣精')
	print('旋轉')
	if dry == True:
		print('烘衣服')

wash2(dry=True)


#-----------------------------
#return的用意是"回傳"，不是回歸，如果function有return，可以把該次執行的結果，存下來。
#
#
#-----------------------------
print('\n')
print('\n')
def add(x,y):
	return x + y
result = add(3,4)
print(result)

def average(numbers):
	avg = sum(numbers)/len(numbers)
	return avg

print(average([1,2,3]))
print(average([10110,55646,67]))


