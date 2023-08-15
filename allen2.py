#自我練習#2
#今天有建立了一個.csv檔，然後將訊號名稱，電壓,電流輸入進去。
#現在要用function的方式處理(還有return儲存執行資料)
#----------------------------------------------------------

#建立自訂名稱的csv檔案
def create_csvfile():
	filename = input('請輸入檔名與副檔名系統會自動建立基礎檔案:\n')
	return filename
	
#輸入"訊號名稱"，"電壓","電流"的資料，並存在data[]此集合裡面
def data_keyin():
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
	return data

#將data[]的資料，存在新建立的.csv內

def date_write(filename,data):
	with open(filename+'.csv','w') as f:
		f.write('訊號名稱,電壓,電流,\n') 
		for d in data:
			f.write(d[0] +','+ d[1]+ ','+d[2]+'\n')

#將需要的function拉進來main1() function處理
def main1():
	x = input('請問有要執行程式嗎? y/n \n')
	if x == 'n':
		print('程式結束')
	else:
		filename_A = create_csvfile()
		data_B = data_keyin()
		date_write(filename_A,data_B)

#最後只有一句話，就可以處理所有的事情，或是取消

main1()