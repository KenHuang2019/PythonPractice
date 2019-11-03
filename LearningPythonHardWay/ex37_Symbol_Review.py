### Symbol review
## Keywords

# del
list = [1,2,3,4]
del list[1] # del = delete the variable
print(list)

a = 1
b = a
c = b
del a # del Just for variable, not for the data
print(b) # So, still work
print(c)
# del
#--------------------------------------------------
# with
# context manager
with open('ex37_with_1.txt', 'w') as file_1, open('ex37_with_2.txt', 'w') as file_2: # Method of opne files 
	# It will open a new file, or overwrite the old one.
	file_1.write("Hi, this is a test about 'with' in file_1")
	file_2.write("Hi, this is a test about 'with' in file_2")
	# It will automatically close the file
print(open('ex37_with_1.txt', 'r').read())
print(open('ex37_with_2.txt', 'r').read())
# with
#--------------------------------------------------
# assert
# assert statement helps detect problems
assert True # Nothing happen
# assert False, "Assertion faled, it will cause error the print is message"
# assert
#--------------------------------------------------
# yield
# To understand what yield does, you must understand what generators are. And before generators come iterables.
list = [1,2,3]
for i in list:
	print(i) # This is iteration, it store all values in memory and this is not always what you want.

test_string = "This is for iter"
iter_test = iter(test_string)

print(next(iter_test),
	next(iter_test),
	next(iter_test),
	next(iter_test))

# yield is used like return, except the function will return a generator
def y():
	yield
def r():
	return
print("y()=", y()) # generator is an object
print("r()=", r())
"""
The keyword 'return' returns a value from a function,
at which time the function then loses its local state.
Thus, the next time we call that function,
it starts over from its first statement.

On the other hand,
yield maintains the state between function calls,
and resumes from where it left off when we call the next() method again.

So if yield is called in the generator,
then the next time the same generator is called we'll pick right back up after the last yield statement.
"""
def y_test():
	for i in range(10):
		X = yield i
		print(str(X))
	
# When the yield comes out, it is a generator.

test = y_test() # Create a generator
next(test) # the function will be excuted untill "yield", so the shell will print only "1"

print(str(test.send(30))) # Then, the code will continue start with last next(), and give the yield a value by .send(value)
print(str(test.send(40)))
# yield
#--------------------------------------------------
# try & finally
def numberGenerator2(n):
	print("Start try...")
	try:
		number = 0
		while number < n:
			yield number
			number += 1
	finally:
		yield n
	print("Finally end here")

for i in numberGenerator2(5):
	print(i)
# try & finally
#--------------------------------------------------
# break
def break_test():
	for i in range(10):
		print(i)
		if i == 5:
			print('close the loop')
			break
break_test()
# break
#--------------------------------------------------
# except
def except_test(x):
	try:
		print("Please input a number")
		print("Input value:", int(x))
		print("Good!, It's a number.")
	except ValueError:
		print("Please input a 'number'!")
	except:
		print("Unknow reason")
except_test(1)
except_test("one") # input string will casuse error, then code will jump to except to run
# except
#--------------------------------------------------
# class
class Animal():
	variable = "This is an animal" # every variable belong to this class will have this value
	__subclass = "This naming method will avoid name collisions" # "__" naming method is to avoid conflict, and called out by usually way
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color
# class is a collection
a = Animal("dog", "5", "black")# asign values to a variable, then call out by class defination
b = Animal("cat", "2", "white")
print(a.name, a.age, a.color, a.variable, a._Animal__subclass) # "_classname__subclassname" is the method to call out "__"subclass
print(b.name, b.age, b.color, b.variable, b._Animal__subclass)
class Animal_2(Animal):
	variable = "This variable already change."
	__subclass = "Try to change __subclass..."
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color

test_Animal = Animal_2("Hi", "12", "color")
print("Change Animal_2 variable: ", test_Animal.variable)
print("Change Animal_2 __subclass: ", test_Animal._Animal_2__subclass) # "_classname__subclassname" is the method to call out "__"subclass
# class
#--------------------------------------------------
# eval
# run the value as code, but "eval" is an expression for caculation
a = 3
b = 4
eval("print(a, b)") 
# eval("a = 1") # This line would be an error
# eval
#--------------------------------------------------
# exec
# run the value as code, but "evec" is a statement supports dynamic execution of Python code
exec("a = 1")
exec("print(a + b)")
# exec
#--------------------------------------------------
# raise
# raise BaseException("test_raise") # all exception must inherit from BaseException, BaseException("Value could be a message to user")
# raise
#--------------------------------------------------
# lambda
# anonymous variable, usually used in funtion as parameter
lambda_list = [1,2,5,8,13,15,20]
for i in filter(lambda x : x < 10, lambda_list):
	print(i)
# another usage : in map(deal with serial element in a corresponding way)
for i in map(lambda x : x * 2, lambda_list):
	print(i)
# lambda


# String Escape Sequences
print("String Escape practice\aString Escape practice") # ring the bell
print("String Escape practice\bString Escape practice") # like "backspace" on keyboard
print("String Escape practice\fString Escape practice") # Formfeed : advance one full page or the start of the next page
print("String Escape practice\rString Escape practice") # Carriage Return : back to the head of this line and rewrite it
print("String Escape practice\tString Escape practice") # TAB
print("String Escape practice\vString Escape practice") # Vertical TAB

# String Formats
print("String Formats %d" % 12) # Signed integer decimal or %i
print("String Formats %u" % 12) # Obsolete type – it is identical to 'd'
print("String Formats %o" % 12) # Signed octal value
print("String Formats %x" % 12) # Signed hexadecimal (lowercase)
print("String Formats %X" % 12) # Signed hexadecimal (uppercase)
print("String Formats %e" % 12) # Floating point exponential format (lowercase)
print("String Formats %E" % 12) # Floating point exponential format (uppercase)
print("String Formats %f" % 12) # Floating point decimal format
print("String Formats %F" % 12) # Floating point decimal format
print("String Formats %g" % 12) # Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise
print("String Formats %G" % 12) # Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise
print("String Formats %c" % c) # Single character (accepts integer or single character string)
print("String Formats %r" % 12) # String (converts any Python object using repr())

# Operators
import numpy as np
matrix1 = np.matrix([[1 , 2],[3 , 4]])
matrix2 = np.matrix([[1 , 2],[3 , 4]])
a = 10
b = 3

c = a // b # Quotient
print("1:", c)
#print(O <> o)
d = 100
d *= 15
print("2:", d)
e = 100
e /= 15
print("3:", e)
f = 100
f //= 15
print("4:", f)
g_1 = 10 % 3 # Remainder
print("5-1:", g_1)
g = 100
g %= 15 # Remainder
print("5:", g)
h = 2
h **= 4
print("6:", h)
m = matrix1 @ matrix2
print(m) # floordiv(a, b)