class Parent(object): # Base class

	def implictict(self): # Behavior
		print("PARENT implictict()")
	def override(self):
		print("PARENT override()")
	def altered(self):
		print("PARENT altered()")

class Child(Parent): # Subclass

	# def implictict(self):
	# 	print("CHILD implictict()")
	def override(self):
		print("CHILD override()")
	def altered(self):
		print("CHILD, BEFORE altered()")
		super(Child, self).altered() # call parent's function
		print("CHILD, AFTER altered()")
	def composition(self):
		self.Other.override() # composition

class Other(object):

	def implictict(self):
		print("OTHER implictict()")
	def override(self):
		print("OTHER override()")
	def altered(self):
		print("OTHER altered()")

class Child_2(object):

	def __init__(self):
		self.other = Other() # composition
	def implictict(self):
		self.other.implictict()
	def override(self):
		self.other.override()
	def altered(self):
		self.other.altered()

dad = Parent()
son = Child()
son_2 = Child_2()

dad.implictict()
son.implictict() # Inheritance
print("-------------")
dad.override()
son.override() # override
print("-------------")
dad.altered()
son.altered() # altered
print("-------------")
son_2.implictict() # composition
son_2.override() # composition
son_2.altered() # composition