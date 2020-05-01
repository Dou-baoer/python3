# ex 01
from sys import argv

#define argv
script, input_file = argv

#define new function print_all. f is only a variable.
def print_all(f):
#1st read, then can open
    print(f.read())

def rewind(f):
# seek is a command to go we want to go. 0 is to 0 bit. 1 ist to now position. 2 ist to the end.
    f.seek(0)

def print_a_line(line_count, f):
#readline is the command to read the file one by one.
    print(line_count, f.readline())

#after read can we open.
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
#here is on by one
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
