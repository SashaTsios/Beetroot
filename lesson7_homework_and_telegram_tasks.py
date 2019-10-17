# Count
first = ([1, 2, 1, 1, 5, 1, 6, 6, 7, 7, 7, 7, 7, 8, 9], 1)
sequence = []
item = ''
count = 0
final_text = 'item {} occurs in the list {}: {} times'
for element in first:
	if type(element) is list:
		sequence = element
		print(sequence)
		continue
	if type(element) is int:
		item = element
		print(item)
		for i in sequence:
			if i == item:
				count += 1
print(final_text.format(item, sequence, count))

# Remove duplicates
remove_duplicates = [1,1,2,2, 3, 3, 3, 3, 4]
removed_list = []
for element in range(0, len(remove_duplicates)):
	if remove_duplicates[element] not in removed_list:
		removed_list.append(remove_duplicates[element])
print(str(remove_duplicates) + ' after removing elements looks like: ' + str(removed_list))

# Digits sum
digit_n = int(input('Number: '))
digit_sum = 0
digit_n_str = str(digit_n)
for i in digit_n_str:
	digit_sum += int(i)
	print(digit_sum)
print('For ' + str(digit_n) + ' sum of numbers: ' + str(digit_sum))

# Factorial
integer = 6
factorial = 1
for i in range(1, integer + 1):
	factorial *= i
print(factorial)

# Homework (to do before lesson)
# Dict comprehension exercise
string1 = 'like like after removing elements looks like sum sum sum of numbers like like occurs in the list of'
string_list = string1.split(' ')
print(string_list)
dict = {}
for element in string_list:
	if element not in dict:
		dict[element] = 1
	else:
		num_of_occurrences = dict[element]
		dict[element] = num_of_occurrences + 1
print(dict)

# List comprehension exercise I
list_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list_b = [element for element in list_a if element % 2 != 0]
print(list_b)

# List comprehension exercise II
list_i = list(range(1, 11))
print(list_i)
list_j = []
for element in list_i:
	element2 = element * element
	list_j.append(element2)
print(list_j)
list_w_tuples = [tuple(list_i), tuple(list_j)]
print(list_w_tuples)