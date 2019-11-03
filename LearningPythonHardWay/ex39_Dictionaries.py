states = {'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'}

cities = {
'CA': 'San Fracisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
print("Michigan abbreviation is: ", states['Michigan'])
print("Florida abbreviation is: ", states['Florida'])

print('-' * 10)
for state, abbrev in states.items():
	print("{} is abbreviation {}".format(state, abbrev))

print('-' * 10)
for abbrev, city in cities.items():
	print("{} has the city {}".format(abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
	print("{} states is abbreviated {} and has city {}".format(state, abbrev, cities[abbrev]))

print('-' * 10)
state = states.get('Texas', None)
if not state:
	print("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: {}".format(city))