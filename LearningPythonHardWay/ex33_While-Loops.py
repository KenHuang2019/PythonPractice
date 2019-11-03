"""
i = 0
numbers = []

while i < 6: # The end condition is important, and this is the difference between for-loop & while loop
	print("At the top i is %d" % i)
	numbers.append(i)

	i = i + 1
	print("Numbers now:", numbers)
	print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
	print(num)
"""
def while_loop(i):
	function_list = []
	end_condition = 10
	while i < end_condition:
		print("This is a loop in a function. Current number: %d" % i)
		function_list.append(i)

		i = i + 1
		print("Numbers now:", function_list)

function_test = -5
while_loop(function_test)