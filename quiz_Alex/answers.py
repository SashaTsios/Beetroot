from questions import get_random_question
from questions import Question

class Answer:
    def __init__(self, question):
        self.question = question
        self.choices = self.question['choices']

    def user_answer(self):
        """Get user answer ('а', 'б', 'в', 'г', 'д' or from 1 to last variant), depends on the amount of variants or q or й to quit.
        Check if it is in correct format.
        """
        first_var = (self.choices[0]['content'][1], int(self.choices[0]['id']) + 1)  #(first letter, first number)
        last_var = (self.choices[-1]['content'][1], int(self.choices[-1]['id']) + 1)  #(last letter, last number)
        abc_range = ('а', '1', 'б', '2', 'в', '3', 'г', '4', '5', 'д')
        while True:
            answ = input(f'\nEnter your variant from [{first_var[0]} to {last_var[0]}] or [{first_var[1]} to {last_var[1]}]. If you want to quit press [q or й or 0]: ')
            if answ.lower() == 'q' or answ.lower() == 'й' or answ.lower() == '0':
                result = None
                print('Bye')
                exit()
            elif answ.lower() in abc_range[0 : (self.choices[-1]['id'] + 1)*2]:  # ?????
                result = answ.lower()
                break
            else:
                print('Wrong format of answer, try again')
        return result

    def letter_to_index(self, letter):
        self.letter = letter
        """Transforming ('а', 'б', 'в', 'г', 'д' and from 1 to last variant) into id."""
        dicti = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, '1': 0, '2': 1, '3': 2, '4': 3, '5': 4}
        return dicti[self.letter]
        
    def answer_question(self, choise_index):
        self.choise_index = choise_index
        """Check if user_answer was correct."""
        if self.choices[self.choise_index]['is_correct']:
            result = True
        else:
            result = False 
        print( f'Your answer is {result}')
        return result