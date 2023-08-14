import os #operating system

line=[]
sline=[]
products = []
if os.path.isfile('aaa.csv'):
	print('我們找到檔案了')
	with open('aaa.csv','r') as f:
		for line in f:
			if '品項,價格'in line:
				continue 
	#--------------------------------------------
	#遇到條件符合，擇跳過"這次的for"直接執行下一個for
	#break 是直接跳出for loop
	#--------------------------------------------
			s = line.strip().split(',')
			print(s)
	#--------------------------------------------
	#strip 會把 空格 或 換行 移除
	#--------------------------------------------
	with open('aaa.csv','r') as d:
		for line in d:
			if '品項,價格'in line:
				continue
			name, price = line.strip().split(',')
			sline.append([name,price])
	print(sline)
	#--------------------------------------------
	#strip 會把 空格 或 換行 移除
	#把資料讀出來 變成一個2D清單
	#--------------------------------------------

	while True:
		name = input('please enter products name. if quit, enter "q":  ')
		if name == 'q':
			break
		price = input('please enter price:  ')
		p = []
		p.append(name)
		p.append(price)
		products.append(p)

	for p in products:
		print(p[0],p[1])
	#--------------------------------------------
	# 大清單裡面有小清單，用for loop可以把一個一個內含物品拿出
	#--------------------------------------------
	with open('aaa.csv','w') as f:
	#--------------------------------------------
	#加上編碼基本上就不會有亂碼 with open('aaa.csv','w', encoding = 'utf-8') as f:
	#實測結果會有亂碼，不要加就不會有，可能是版本問題
	#--------------------------------------------
		f.write('品項,價格\n')

	#--------------------------------------------
	#記得要有下一行
	#--------------------------------------------
		for p in products:
			f.write(p[0] +','+ p[1]+'\n')

	#--------------------------------------------
	# 字串可以用加法連起來 '123'+'abc' =123abc
	# 可以改用.csv，這可以存更多屬性
	# with open 這個會有自動close的東西，只要離開with open就會自動close
	#--------------------------------------------

else:
	print('沒有這個檔案')


#讀取檔案



