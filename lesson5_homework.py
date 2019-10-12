a = range(1, 101)
print(*a)
i = 0
abc = []
for i in a:
	if i % 7 == 0 and i % 5 != 0 and i < 101:
		abc.append(i)
	else:
		i += 1
print('List of numbers that are divisible by 7 but not a multiple of 5:')
print(abc)