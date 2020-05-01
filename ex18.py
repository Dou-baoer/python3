# this on is like your scripts with argv
# def is "define"
def print_two(*args):
    arg1, arg2 = args
    print(f"argl:{arg1}, arg2:{arg2}")

# this is same like the up one. it' not nessery umpack the "args"
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothing.")

print_two("Jin", "Xie")
print_two_again("Jin", "xie")
print_one("First")
print_none()
