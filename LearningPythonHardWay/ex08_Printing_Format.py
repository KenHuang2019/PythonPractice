formatter = "{} {} {} {}" # Define Variable

print(formatter.format(1, 2, 3, 4))# .format is a "function"
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True)) # Don't need to quote True & False. Python could recognize it.
print(formatter.format(formatter, formatter, formatter, formatter)) # Each {} has four {} (4 * 4 = 16)
print(formatter.format(
    "La La",
    "La",
    "La",
    "La La La"
))