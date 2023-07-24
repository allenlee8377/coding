age = input('how old r u?')
age = int(age)
if age < 18:
	print('you r so young, so you can not drive')
elif age >=18:
	car = input('Can you drive? Y/N: ')
	if car == 'Y':
		print('Good~ we cae go a driving trip')
	elif car == 'N':
		print('do you want to learn it ?')
	else:
		print('please enter Y/N')
else:
	print('please enter numbers')