from random import randint

questions = [
    {
        "content": "2 + 2 - 4 = ",
        "choices": [
            {"content": "0", "is_correct": True},
            {"content": "24", "is_correct": False},
            {"content": "14", "is_correct": False},
            {"content": "-4", "is_correct": False},
        ],
    },
    {
        "content": "18 / 2 = ",
        "choices": [
            {"content": "5", "is_correct": False},
            {"content": "9", "is_correct": True},
        ],
    },
    {
        "content": "18 / 3 = ",
        "choices": [
            {"content": "1", "is_correct": False},
            {"content": "11", "is_correct": False},
            {"content": "6", "is_correct": True},
        ],
    },
    {
        "content": "18 * 2 = ",
        "choices": [
            {"content": "2", "is_correct": False},
            {"content": "36", "is_correct": True},
            {"content": "100", "is_correct": False},
        ],
    },
]

entry_text = 'Let\'s check your math knowledge: {}'

def random_n(q_list):
	"""Get random number from sequence len() diapason."""
	random_question_number = randint(0, len(q_list) - 1)
	return random_question_number

def beginning(random_question_number):
	"""Shows question[index] + answers, ask users input and checks if the input is in correct form.""" 
	print(entry_text.format(questions[random_question_number]['content']))  
	global q_choices
	q_choices = questions[random_question_number]['choices']
	for num_of_choices in range(0, len(q_choices)):
		list_of_variants = str(num_of_choices + 1) + ' variant: ' + q_choices[num_of_choices]['content']
		print(list_of_variants)

	while True:
		users_a = input('Choose the variant: ')
		try:
			users_a = int(users_a)
		except ValueError:
			print('Please enter a variant correctly!')
		else:
			print(users_a)
			break		
	
	while users_a not in range(1, len(q_choices) + 1):
		print('Answer is out of list_of_variants')
		users_a = int(input('Choose the variant: '))
	else:
		users_ans = users_a
	return users_ans												

def answer_is_wrong(random_question_number, users_answer):
	"""If the answer is wrong - asks to try again or to quit."""
	while q_choices[int(users_answer) - 1]['is_correct'] is False:
		print('Not correct')
		ask = input('To try this question again press \'y\'. To quit \'q\': ')
		if ask.lower() == 'y':
			while True:
				users_a = input('Enter your variant again: ')
				try:
					users_a = int(users_a)
				except ValueError:
					print('Please enter a variant correctly!')
				else:
					break
			while users_a not in range(1, len(q_choices) + 1):
				print('Answer is out of variants, enter again')
				users_a = int(input('Enter your variant again: '))
			else:
				users_answer = users_a	
			return answer_is_wrong(random_question_number, users_answer)
		elif ask.lower() == 'q':
			print('Goodbye looser')
			exit()

def answer_is_correct(random_question_number, users_answer):
	"""If the answer is correct - asks to answer another question or to quit."""
	while q_choices[int(users_answer) - 1]['is_correct'] is True:				    
		print('Correct')
		ask = input('To try another question press \'y\'. To quit press \'q\': ')
		break
	while ask.lower() != 'y' or ask.lower() != 'q':	
		print('Wrong action, press \'y\' to continue or \'q\' to quit only')
		ask = input('To try another question press \'y\'. To quit \'q\': ')
	if ask.lower() == 'q':
		print('Goodbye buddy!')
		exit()
	elif ask.lower() == 'y':
		asks = ask
	return asks
			
def main():
	"""Final function combines all previous functions and runs the calculator."""
	ask = 'y'
	while ask.lower() == 'y':
		random_question_number = random_n(questions)
		users_answer = beginning(random_question_number)
		answer_is_wrong(random_question_number, users_answer)
		ask = answer_is_correct(random_question_number, users_answer)
	else:
		exit()

main()