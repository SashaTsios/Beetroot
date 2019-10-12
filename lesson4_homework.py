name = input('Your name is: ')
age = int(input('Your age is: '))
age1 = age + 1
text = 'Hello {}, on your next birthday you\'ll be {} years'
print(text.format(name, age1))

import random
random_n = random.randint(1, 10)
player_n = int(input('Let\'s check your luck. Type your number: '))
if player_n in range(1, 11):
	if player_n == random_n:
		print('Awesome! You guess')
	else:
		print('You not guessed')
		print('A random number was: ' + str(random_n))
else:
	print('Wrong input')