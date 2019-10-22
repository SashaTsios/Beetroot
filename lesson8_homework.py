# I won't use comprehension until i understood it enough.

'''Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def lower_upper(string):
	count_L = 0
	count_U = 0
	for i in range(0, (len(string))):
		if string[i].isupper() is True:
			count_U += 1
		elif string[i].islower() is True:
			count_L += 1
	return (f'''Sample String: {string}
No. of Upper case characters : {count_U}
No. of Lower case characters : {count_L}''')

print(lower_upper(input('Enter your string: ')))

'''Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''

def unique(sample_list):
	unique_list = []
	for element in sample_list:
		if element not in unique_list:
			unique_list.append(element)
	return f'from sample list {sample_list} unique elements are: {unique_list}'

sample_list = [1,2,3,3,3,3,4,5]
print(unique(sample_list))

'''Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
'''

def even(sample_list):
	even_list = []
	for number in sample_list:
		if number % 2 == 0:
			even_list.append(number)
	return even_list

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even(sample_list))

'''Write a Python function to check whether a string is a pangram or not. Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
'''

def pangram(string0):
	import string
	abc_string = string.ascii_lowercase 
	letters_from_list = ''
	for i in range(0, len(string0)):
		if string0[i].isalpha() is True:
			letters_from_list += string0[i].lower()
			
	sorted_letters = (''.join(sorted(set(letters_from_list))))
	# print(f'SOrted list from string is: {sorted_letters}')
	if sorted_letters == abc_string:
		result1 = f'{string0} -  is a pangram!'
	else: 
		result1 = f'{string0} - is NOT a pangram!'
	return result1

string5 = "The quick brown,! fox jumps over the lazy doz zzzzz"
print(pangram(string5))


'''Creating a dictionary:
Create a function called make_country, which takes in a country’s name and capital as parameters. 
Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys. 
Make the function print out the values of the dictionary to make sure that it works as intended. 
'''

def make_country(input_country, input_capital):
	country_capital = {}
	country_capital['Name'] = input_country
	country_name = country_capital['Name']
	country_capital['Capital'] = input_capital
	country_cap = country_capital['Capital']
	return(f'The capital of {country_name} is {country_cap}')

print(make_country('Ukraine', 'Kyiv'))
print(make_country('France', 'Paris'))

'''A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.
For example: the call make_operation(‘+’, 7, 7, 2) should return 16
The call make_operation(‘-’, 5, 5, -10, -20) should return 30
The call make_operation(‘*’, 7, 6) should return 42
'''

def make_operation(action, *x):
	total = 0
	tot = 0
	total_mult = 1
	action_dict = {'+': 'addition', '-': 'subtraction', '*': 'multiplication'}
	print(f'You want to make {action_dict[action]} for these numbers: {x}')
	if action == '+':
		for i in x:
			total += i
	if action == '-':
		for i in range(1, len(x)): #divided *x argument in x[0] and other to avoid mistake when x[0] < 0 (example -1) and it count as tot = tot --1
			tot = tot - x[i]	#added new
		total = x[0] + tot
	if action == '*':
		for i in x:
			total_mult *= i
			total = total_mult
	return ('Final resuls is {}'.format(total))

print(make_operation('*', -5, -5, 10, -20))