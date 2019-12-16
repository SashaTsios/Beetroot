initial_data = {
    "foo": {"bar": {"value": 25}, "bar2": {"value": 36}, "serhii": 15,},
    "foo2": 30,
    "ira": 20,
}

final_dict = {}


def my(diction):
    def run(val, k, name1):
        if type(val) is str or type(val) is int:
            final_dict[name1] = val
            return final_dict
        else:
            for kk, vv in val.items():
                name2 = name1 + "." + kk
                run(vv, kk, name2)

    for k, v in diction.items():
        name1 = k
        run(v, k, name1)

    print(final_dict)
    return final_dict


dict_w_dot = my(initial_data)


print(":::::::::::::::::::::::::::::::::::::::\n")

"""Make a function that takes an integer i as parameter, then return a list of numbers in the fibonacci sequence all the way to the ith element in the sequence. 

1 2 3 4 5 6 7 8  9  10
0 1 1 2 3 5 8 13 21 34
"""

RESULTS = {
    1: 0,
    2: 1,
}


def fib_rec(num_index):
    if num_index in RESULTS:
        return RESULTS[num_index]
    value = fib_rec(num_index - 1) + fib_rec(num_index - 2)
    RESULTS[num_index] = value
    return value

x = int(input('Enter Fibo index: '))
def start(x):
    var = fib_rec(x)
    total_list = []
    for k, v in RESULTS.items():
        if v == var:
            for element in range(1, k + 1):
                total_list.append(RESULTS[element])
    print(f"Fibonacci sequence to the {len(total_list)} index is: {total_list}")
start(x)
print(":::::::::::::::::::::::::::::::::::::::\n")

"""Make a function that takes an integer (in decimal form) and convert it to a binary form using recursion"""


def converter(num):
    div_list = []
    binary_number = ""
    div_list.append(num)

    def second_converter(number):
        z = number // 2
        if z >= 1:
            # print(f'{number} // 2 = {z}')
            div_list.insert(0, z)
            second_converter(z)
            return second_converter

    second_converter(num)

    for element in div_list:
        if element % 2 == 0:
            binary_number += "0"
        else:
            binary_number += "1"
    print(f"Binary number of {num} is {binary_number}")
    return binary_number


converter(13)
