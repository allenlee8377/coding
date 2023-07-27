import random
r = random.randint(1,100)
print('please try to find the correct number, it betewwn 1 to 100')
count =0 
while True :
	print('This is the NO.',count,'times')
	count = count +1
	x = input('plz enter number :')
	x = int(x)
	if x == r:
		print('Congratulation!!!')
		break
	elif x > r :
		print('x More than ans')
	else:
		print('x LESS than ans')

