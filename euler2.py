my_total = 0

last_fib = 1
current_fib = 1

while last_fib + current_fib <= 4000000:
	new_last_fib = current_fib				# Store the current fibonacci number in the new_last_fib variable
	current_fib = last_fib + current_fib	# Compute the next fibonacci number as the sum of the current and prior numbers
	last_fib = new_last_fib					# Reset the last fibonacci number to the new_last_fib
	
	if(current_fib % 2 == 0):
		my_total += current_fib


print(my_total)