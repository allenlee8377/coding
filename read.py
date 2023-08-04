#loading file

# 把AA.txt打開(with) 讀取(r)出來，且把AA.txt 用f 來替稱
with open('AA.txt','r') as f:
	for line in f:
		print(line)

#AABBCC
#
#DD
#

d = []
with open('AA.txt','r') as f:
	for line in f:
		d.append(line)
print(d)

#['AABBCC\n', 'DD']

d = []
with open('AA.txt','r') as f:
	for line in f:
		d.append(line.strip())
print(d)

#['AABBCC', 'DD'] : 把\n 空格符號移除
