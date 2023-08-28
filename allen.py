#自我練習#1
#今天有建立了一個.csv檔，然後將訊號名稱，電壓,電流輸入進去。


#建立自訂名稱的csv檔案

filename = input('請輸入檔名與副檔名系統會自動建立基礎檔案:\n')
	
#輸入"訊號名稱"，"電壓","電流"的資料，並存在data[]此集合裡面

data=[]
while True:
	signal_name = input('請輸入訊號名稱，如不需要請按q 結束:\n')
	if signal_name == 'q':
		break
	voltage = input('請輸入電壓(V):\n')
	current = input('請輸入電流(A):\n')
	d = []
	d.append(signal_name)
	d.append(voltage)
	d.append(current)
	data.append(d)

#將data[]的資料，存在新建立的.csv內

with open(filename+'.csv','w') as f:
	f.write('訊號名稱,電壓,電流,\n') 
	for d in data:
		f.write(d[0] +','+ d[1]+ ','+d[2]+'\n')

