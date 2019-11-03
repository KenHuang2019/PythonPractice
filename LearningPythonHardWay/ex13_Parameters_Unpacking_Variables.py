from sys import argv
"""
script = sys.argv[0]
first = sys.argv[1]
second = sys.argv[2]
third = sys.argv[3]
"""
script, first, second, third = argv # unpack
print("The script is called:", script)
print("The first is called:", first)
print("The second is called:", second)
print("The third is called:", third)