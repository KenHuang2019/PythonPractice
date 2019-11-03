def add(a, b):
	print("ADDING %d + %d" % (a, b))
	return a + b

def subtract(a, b):
	print("SUBTRACTING %d - %d" % (a, b))
	return a - b

def multiply(a, b):
	print("MULTIPLYING %d * %d" % (a, b))
	return a * b

def divide(a, b):
	print("DIVIDING %d - %d" % (a, b))
	return a / b

print("Let;s do some math with just functions!")

age = add(23, 5)
height = subtract(172, 2)
weight = multiply(100, 10)
IQ = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, IQ))

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(IQ, 2))))

print("That become: ", what, "Can you do it by hand?")