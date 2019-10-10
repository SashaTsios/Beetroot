#First task w 3 attemps to enter a correct number
count = 0
while True:
	phone_n = input('Enter your mobile number: +38')
	count += 1
	if count > 3:
		print('Enough wrong entries')
		break
	else:
		if phone_n.isdigit() and len(phone_n) == 10:
			text = '+38{} is ok'
			print(text.format(phone_n))
			break
		elif phone_n.isdigit() and len(phone_n) != 10:
			print('Check the length of your mobile number')
		else:
			print('Please exclude letters from the number')

#Second
a = 5 + 1 == 7
aa = '5 + 1 == 7'
print(aa)
input1 = input('Is it True or False? It is: ')
if a == True and input1.lower() == 'true':
	print('Good job!')
elif a == False and input1.lower() == 'false':
	print('Good job!')
else:
	print('Try again!')

#Third
name = input('your name is: ')
variable_name = 'alex'
if name.lower() == variable_name:
	final_text = '{} = {}'
	print(final_text.format(name, variable_name))
	print('True')