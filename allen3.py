#練習 allen3
#如果有一文檔，希望找出特定文字，且計數文字
#利用reviews.txt來處理


#讀取reviews.txt 將每一筆留言都塞進data[]
#要將每一筆的留言都分開來 data=[[aaaa ssss],[dewd ewdw ewdwd dwedw]...]

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