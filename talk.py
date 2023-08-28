#Line對話紀錄,利用vvv.txt做出一些事情



#把對話紀錄取之後，如果line有在f裡面，那我就一直對line做切割，
#將對話紀錄(大集合)切成數的小集合s
#[:3] 開始[0]有，結束[3]沒有包含
#[-2:] 尾巴開始  [-2][-1][0][1][2] [A,B,C,D,E]

talk=[]
with open('vvv.txt','r', encoding='utf-8') as f:
	for line in f:
		talk.append(line.strip())  #用空格做區分

for line in talk:
	s = line.split(' ')
	time = s[0]

for line in talk:
	allen = line.split(' ')
	An = allen[1]+allen[2]
	Ant= allen[3:]
	if An == 'AllenLee(煜杰)':
		print(An,':',Ant)

for line in talk:
	eason = line.split(' ')
	En = eason[1]
	Ent= eason[2:]
	if En == 'Eason':
		print(En,':',Ent)
