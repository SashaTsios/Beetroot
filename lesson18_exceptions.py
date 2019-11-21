def two_numbers():
    while True:
        try: 
            a = float(input('Enter first number: '))
        except ValueError:
            print('First number is not a digit')
        else:
            break
    while True:
        try:    
            b = float(input('Enter second number: '))
        except ValueError:
            print('Second number is not a digit')
        else:
            break
    while True:
        try:
            result = a*a/b
            returned_value = result
        except ZeroDivisionError:
            result = 'Not allowed to divide by 0'
            print(result)
            returned_value = None
        finally:
            print(f'{a} * {a} / {b} = {result}')
            break
    return returned_value

any_var = two_numbers()
print(f'Returned value: {any_var}')