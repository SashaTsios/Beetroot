import json
from random import randint

def read_from_file():
    with open('questions.json') as questions_file:
        data = questions_file.read()
        questions = json.loads(data)
        return questions

def get_random_question():
    i = randint(0, (len(QUESTIONS)-1))
    question_data = QUESTIONS[i]
    return Question(question_data)

class Question():
    """Prints random question and variants of answers are with letter and number indexes. 
    
    def all_question was created to save random question in memory and propose to show it again if the answer was not True.
    """
    def __init__(self, question_to_show):
        self.question_to_show = question_to_show

    def all_question(self):
        return self.question_to_show    
        
    def display(self):
        print('Question:')
        print('========\n')
        print(self.question_to_show['content'])
        print('\nAnswers:')
        print('========\n')
        for choices in self.question_to_show['choices']:
            print(str(int(choices['id']) + 1) + ' or ' + choices['content'])

QUESTIONS = read_from_file()