action = input('Enter an arithmetic action to complete ( + | - | / | * | ** | **2 ): ')
dict = {'+': 'addition', '-': 'subtraction', '/': 'division', '*': 'multiplication', '**': 'power', '**2': 'square'}
dict_value = dict[action]
text0 = 'You choose: {}'
print(text0.format(dict_value))
text = '{} {} {} = {}'
text2 = '{} {} = {}'
if action == '+' or action == '-' or action == '/' or action == '*' or action == '**':
	while True:
		value1 = input('Type first number: ')
		try:
			float_value1 = float(value1)
		except ValueError:
			print('Please enter a number correctly!')
		else:
			print(value1)
			break
	while True:
		value2 = (input('Type second number: '))
		try:
			float_value2 = float(value2)
		except ValueError:
			print('Please enter a number correctly!')
		else:
			print(value2)
			break

	fv1 = float(value1) #float value1
	iv1 = int(float(value1)) #integer value1
	fv2 = float(value2) #float value2
	iv2 = int(float(value2)) #integer value2
	if fv1 != 0 and fv2 != 0:
		intORfloat1 = iv1 / fv1
		intORfloat2 = iv2 / fv2
		if intORfloat1 == 1.0 and intORfloat2 == 1.0:	
			value1_new = int(value1)
			value2_new = int(value2)
		else:
			value1_new = float(value1)
			value2_new = float(value2)
	elif fv1 == 0 and fv2 != 0:
		intORfloat2 = iv2 / fv2
		if intORfloat2 == 1.0:	
			value1_new = int(value1)
			value2_new = int(value2)
		else:
			value1_new = float(value1)
			value2_new = float(value2)
	elif fv1 != 0 and fv2 == 0:
		intORfloat1 = iv1 / fv1
		if intORfloat1 == 1.0:	
			value1_new = int(value1)
			value2_new = int(value2)
		else:
			value1_new = float(value1)
			value2_new = float(value2)
	else:		
		value1_new = int(value1)
		value2_new = int(value2)
	if action == '+':
		addition = value1_new + value2_new
		print(addition)
		print(text.format(value1_new, action, value2_new, addition))
	elif action == '-':
		subtraction = (value1_new - value2_new)
		print(text.format(value1_new, action, value2_new, subtraction))
	elif action == '*':
		multiplication = (value1_new * value2_new)
		print(text.format(value1_new, action, value2_new, multiplication))
	elif action == '**':
		power = (value1_new ** value2_new)
		print(text.format(value1_new, action, value2_new, power))
	elif action == '/':
		if value2_new != 0:
			division = (value1_new / value2_new)
			print(text.format(value1_new, action, value2_new, division))
		else:
			print('Division by zero is not allowed')

elif action == '**2':
	while True:
		value1 = input('Type number: ')
		try:
			float_value1 = float(value1)
		except ValueError:
			print('Please enter a number correctly!')
		else:
			print(value1)
			break
	fv1 = float(value1) #float value1
	iv1 = int(float(value1)) #integer value1
	if iv1 != 0:
		intORfloat1 = iv1 / fv1
		if intORfloat1 == 1.0:	
			value1_new = int(value1)
			print(value1_new)
		else:
			value1_new = float(value1)
			print(value1_new)
	else:
		value1_new = float(value1)
		square = value1_new ** 2.
		print(square)
		print(text2.format(value1_new, action, square))		

else:
	print('Choose an action correctly!')