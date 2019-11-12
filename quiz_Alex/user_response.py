def way_to_go(True_answer):
    """Action after users input.  

    If the answer was correct we propose to get new question or to quit.
    Else we propose all the same and ability to answer again.
    """
    if True_answer:  # If last answer was True
        while True:
            user_continue = input('Press [w or ц] to "Walk" to another question or anything else to Quit: ')
            if user_continue.lower() == 'w' or user_continue.lower() == 'ц':
                result = 'new_round'  # run_quiz()
                break
            else:
                print('Bye-bye')
                result = 'way_to_exit'
                break
    elif not True_answer:
        while True:
            user_continue = input('Press [w or ц] to "Walk" to another question, [e or у] to "Enter" another answer on this question, to quit press [q or й or 0]: ')
            if user_continue.lower() == 'e' or user_continue.lower() == 'у':
                result = True
                break
            elif user_continue.lower() == 'w' or user_continue.lower() == 'ц':
                result = 'new_round'  # run_quiz()
                break
            elif user_continue.lower() == 'q' or user_continue.lower() == 'й' or user_continue.lower() == '0':
                print('Bye-bye')
                result = 'way_to_exit'
                break
            else:
                print('Wrong choice')
    return result