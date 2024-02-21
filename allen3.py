#練習 allen3
#如果有一文檔，希望找出特定文字，且計數文字
#利用reviews.txt來處理
#讀取reviews.txt 將每一筆留言都塞進data[]
#要將每一筆的留言都分開來 data=[[aaaa ssss],[dewd ewdw ewdwd dwedw]...]


# 輸入單字，找出出現幾次
def seachword():
	xdata = []
	zdata = []

	with open('reviews.txt','r') as f:
		for aa in f:
			xdata.append(aa.strip().replace(',','').replace('!','').replace('[','').replace(']','').replace('"','').split(' '))

	for yy in xdata:
		for zz in yy:
			zdata.append(zz)
	
	word = input('輸入要找的字，會統計出現幾次: ')
	print(zdata.count(word))

#將處理好的reviews，直接羅列出各種單字出現的次數
def dictory():
	xdata = []
	zdata = []
	with open('reviews.txt','r') as f:
		for aa in f:
			xdata.append(aa.strip().replace('.','').replace(',','').replace('!','').replace('[','').replace(']','').replace('"','').split(' '))
	for yy in xdata:
		for zz in yy:
			zdata.append(zz)
	dic={}
	for dd in zdata: #在 zdata[]確認是否有dd，重複出現的+1，沒有出現過的
		if dd in dic:
			dic[dd] = dic[dd] + 1
		else:
			dic[dd] = 1
	for dd in dic:
		print(dd,',',dic[dd])

#全部變成字母與符號，可以搜尋該字母/符號出現的次數
def singlesymbo():
	bb = []
	zz = []
	with open('reviews.txt','r') as f:
		for aa in f:
			bb.append(aa.strip())
	for cc in bb:
		for dd in cc:
			for ee in dd:
				zz.append(ee)
	word = input('輸入要找的字母或符號，會統計出現幾次: ')
	print(zz.count(word))			

#全部變成字母與符號，直接羅列出各種字母與符號出現的次數
def dic_singlesymbo():
	bb = []
	zz = []
	with open('reviews.txt','r') as f:
		for aa in f:
			bb.append(aa.strip())
	for cc in bb:
		for dd in cc:
			for ee in dd:
				zz.append(ee)
	dic={}
	for xx in zz: #在 zdata[]確認是否有xx，重複出現的+1，沒有出現過的
		if xx in dic:
			dic[xx] = dic[xx] + 1
		else:
			dic[xx] = 1
	print(dic)
    print(dic)