from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

indata = open(from_file).read()

print("The input file is %r bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit ENTER to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w').write(indata)
# f.write(string) writes the contents of string to the file, returning the "number" of characters written.
# So, don't need to close the file, because it's not a file handler. Just an integer.

print("Alright, all done.")

#out_file.close()
#indata.close()