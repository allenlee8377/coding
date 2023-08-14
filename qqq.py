#練習把EXCEL讀出


def readfile(filename):
	list1 =[]
	with open(filename,'r') as data:
		for line in data:
			A = line.strip().split(',')
			list1.append(A)

	B = input('你想知道第幾列的數據?: ') # Y軸
	C = input('你想知道第幾行的數據?: ') # X軸
	B = int(B)
	C = int(C)

	if 0< C <= 6 : 
		print(list1[B][C-1])
	else :
		print('XXXXXX')
		

readfile('qqq.csv')
readfile('aaa.csv')

#------------------------
#
#function化
#-----------------------