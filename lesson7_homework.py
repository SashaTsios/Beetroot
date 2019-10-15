# First homework - don't know how to do it.
'''
dict comprehension exercise.
Make a program that given a whole sentence (a string) will make a dict
containing all unique words as keys and the number of occurrences as
values. 
'''

b = []
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in a:
	if i % 2 != 0:
		b.append(i)
		i += 1
print(b)

# Or: 

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_a = [i for i in a if i % 2 != 0]
print(new_a)

i = tuple(range(1, 11))
print(i)
i2 = []
for element in list(i):
	element = element * element
	i2.append(element)
j = tuple(i2)
print(i2)

# Or: 

i = tuple(range(1, 11))
print(i)
i2 = ()
for element in list(i):
	element = element * element
	i2 = (*i2, element)
print(i2)