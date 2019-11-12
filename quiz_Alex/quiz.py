from questions import get_random_question
from questions import Question
from answers import Answer
from user_response import way_to_go

def run_quiz():

	print('Ready? \n')
	question_i = get_random_question()  # Instance of class Question
	again = True
	while again:
		question_i.display()  # Show question and variants
		var_answer = Answer(question_i.all_question())
		users_letter = var_answer.user_answer()
		choise_index = var_answer.letter_to_index(users_letter)
		users_result = var_answer.answer_question(choise_index)
		again = way_to_go(users_result)
		if again == 'new_round':
			print('\nNew round starts!\n')
			run_quiz()
		if again == 'way_to_exit':
			exit()

if __name__ == '__main__':
	run_quiz()