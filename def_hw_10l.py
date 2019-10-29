"""ЗАДАЧА 1:
Написати функцію, яка друкує усі унікальні значення в словнику. 
Приклад вхідних даних: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
"""

list1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

def dict_unique(list_x):
	final_list = []
	for each_dict in list_x:
		for key, value in each_dict.items():
			if [value] not in final_list:
				final_list.append([value])
	print(final_list)

dict_unique(list1)

"""ЗАДАЧА 2:
Написати функцію, яка перетворює рядок в словник, де ключ - буква, а значення - її кількість в рядку.
Наприклад, з вхідними даними : 'beetrootacademy'
"""

ba_str = 'beetrootacademy'

def count_letters(str1):
	final_dict = {}
	for i in sorted(str1):
		final_dict[i] = str1.count(i)
	print(final_dict)
	return final_dict

count_letters(ba_str)

"""ЗАДАЧА 4:
Написати програму-гру, яка вміє загадувати натуральне число від 1 до 100. 
Програма повинна загадати число, та запитувати у користувача 
правильну відповідь, поки він не відгадає, обмеживши 10 спробами. 
На кожній ітерації писати - "Холодно" (Модуль різниці - більший 15), 
"Тепло" (Модуль різниці - від 5 до 15), або "Гаряче" (Модуль різниці - менший 5), 
в залежності від того, на скільки користувач близький до відповіді.
"""

from random import randint

def game(attemps):
	user_attemps = 1
	number_attemps = int(attemps)
	number = randint(1, 100)
	answer = ''
	while user_attemps <= number_attemps:
		print(f'Attemps left {number_attemps - user_attemps + 1}')	
		while True:
			ans = input('Guess a number between 1 and 100: ')
			try: 
				int(ans)
			except ValueError:
				print('Hey, use numbers only!')
			else:
				break
		answer = int(ans)
		if answer == number:
			print('Great! Wonderful! What a choice! How you did that? AAA! Bye!')
			break
		else:
			if abs(answer - number) > 15:
				print('Cold, difference is more than 15')
			elif abs(answer - number) >= 5:
				print('Warm, difference is more than 5 but no more than 15')	
			else:
				print('Hot! Try to catch it nearby +/-4')
			user_attemps += 1	
	if user_attemps > number_attemps:
		print('^_^_^_^_^_^_^_^_^_^_^')
		print(f'The number was: {number}')  	
		print('You tried too many times, bye!')	

game(10)

"""ЗАДАЧА 3:
Розробити функцію counter(a, b),
Яка приймає 2 аргументи -- цілі невід'ємні числа a та b, та повертає число -- кількість різних цифр числа b, які містяться у числі а.
"""

def counter(a, b):
	count = 0
	for digit in set(str(b)):
		if digit in str(a):
			count += 1
	print(count)

counter(12345, 567)
counter(1233211, 12128)
counter(123, 54)
counter(1234567890, 1234567890)

"""Write a Python function that takes two lists and returns True if they have at least one common member."""

list1 = [1, 2, 3, 4, '12', ['123', '321A'], {'k': ['value1', 'value2']}]
list2 = [6, 7, 6, '11', ['123', '321'], {'k': ['value1', 'value2']}]

def two_lists_1(list_x, list_y):
	for i in list_x:
		if i in list_y:
			result =  True	
		else:
			result = False
	return result

def two_lists_2(list_x, list_y):
	result = True if True in [True if i in list_y else False for i in list_x] else False
	return result

print(two_lists_1(list1, list2))
print(two_lists_2(list1, list2))

"""Write a Python function to get first, second best scores from the list. List may contain duplicates."""

list1 = [86,86,85,85,85,83,23,45,84,1,2,0] # => should get 86, 85
list2 = ['as', 'assa', 'assaas']

def max_result(list_x):
	set_x = set(list_x)
	first_max = max(set_x)
	print(f'First best result is: {first_max}')
	set_x.remove(first_max)
	second_max = max(set_x)
	print(f'Second best result is: {second_max}')
	
max_result(list1)
max_result(list2)


"""{'Student': 10, 'student1': 20, 'student3': 30}
Get first and second best scores students
"""

stud_dict1 = {'Student': 10, 'student1': 20, 'student3': 30, 'student4': 98, 'student5': 99}

def students(dictionary, number_best_students):
	z = []
	for i in dictionary.values():
		z.append(i)
	print('Top students are:')
	for k, v in dictionary.items():
		if v >= z[-number_best_students]:
			print(f'{k} has result {v}')

students(stud_dict1, 2)

"""Write a Python function to display products with price less or equal form user input."""

products = {
'SMART WATCH': 550,
'PHONE' : 1000,
'PLAYSTATION': 500,
'LAPTOP' : 1550,
'MUSIC PLAYER' : 600,
'TABLET' : 400
}

def able_to_buy(costs):
	a = products.values()
	for i in a:
		if costs < min(a):
			print(f'Your total sum is {costs} and you can\'t buy anything(')
			exit()
	for key, value in products.items():
		if value <= costs:
			print(f'You can buy {key}')

able_to_buy(400)

"""Write a Python function to shuffle and print a specified list.
row1 = [1, 2, 3, 4, 6] -> [3, 2, 4, 5, 1]
"""

row1 = [1, 2, 3, 4, 6]
def shuffle_row(row1):
	for i in range(len(row1)):
		abc = row1[i]
		del row1[i]
		row1.insert(randint(0, len(row1)-1), abc)	
	print(row1)

shuffle_row(row1)