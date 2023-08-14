#range 就是範圍的意思
#這是一個內建功能，這是清單產生器

range(5) #[0,1,2,3,4]
range(3) #[0,1,2]

print(range(5))
print(range(5)[2])
print('--------------')

for i in range(5):
	print(i)

print('--------------')

import random

for i in range(5):
	r = random.randint(0,100)
	print(r)
