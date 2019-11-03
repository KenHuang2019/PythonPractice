# When quote in strings:
print("I am 'tall\" ") # escape double-quote inside string
print('I am \'tall" ') # escape single-quote inside string
# Use different type quote or add a "\"

tabby_cat = "\tI'm tabbed in." # Horizontal tab
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)