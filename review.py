data=[]
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
print(len(data))

#共1000000筆資料

sum_len = 0
for x in data:
	sum_len = sum_len + len(x)
print(sum_len/len(data))

#文件中，有1000000筆資料，經過上述運算會得到 data = ['AAA', 'BBBB', 'CCC', ..,'z']
#所以在利用類似下方的概念，得到美一筆資料的長度就可以計算，資料的平均長度

# Q=[12,2,'233',2]
# print(len(Q))
# print(len(Q[2]))
# 4
# 3

new =[]
for s in data:
	if len(s) < 200:
		new.append(s)
		print(s)
print(len(new))

good=[]
for g in data:
	if 'good' in g:
		good.append(g)
print(len(good))
print(good[0])







