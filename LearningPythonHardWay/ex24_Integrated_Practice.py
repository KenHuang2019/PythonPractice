print("Let's practice everything.")
print('You\'d need to know \'bout escaoes with\\ that do \n newline and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend an explanation
\n \t\twhere there is none.
"""

print("_________________________")
print(poem)
print("_________________________")

five = 10 - 2 + 3 - 6
print("This should be five: {}".format(five)) # format for python3

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print('With a starting point of: %d' % start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(beans, jars, crates)) # format for python3

# start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates" % secret_formula(start_point / 10)) # format for python2