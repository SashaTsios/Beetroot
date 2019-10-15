fibo_list = [0, 0]
i = 0
for i in range(21):
	if i == 0:
		fibo_list[i] = 0
		fibo_list.append(fibo_list[i])
	elif i == 1:
		fibo_list[i] = 1
		fibo_list.append(fibo_list[i])
	else:
		fibo_list[i] = fibo_list[i - 1] + fibo_list[i - 2]
		fibo_list.append(fibo_list[i])
		print(fibo_list)


listnew = []
for i in range(1, 101):
	listnew.append(i * i)
	i += 1
print(listnew)

carlist =[]
while True:
	carname = input('Enter a car name or type \'q\' to quit: ')
	if carname != 'q':
		carlist.append(carname)
		print(carlist)
	else:
		print(carlist)
		break

reverse_list11 = []
list11 = ['A', 'B', 'C', 444, 555, 666, [777, 'Seven'], 'August', 'September', 'October', 'November']
# for i in range(-1, (-len(list11) - 1), -1):
for i in range((len(list11) - 1), -1, -1):
	reverse_list11.append(list11[i])
print(reverse_list11)