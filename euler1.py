my_total = 0

for i in range(1, 1000):
	if(i % 3 == 0 or i % 5 == 0):
		my_total += i


print(my_total)