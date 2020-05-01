#from sys import argv

#script, filename = argv

#txt = open(filename)

#print(f"Here's your file {filename}:")
#print(txt.read())

print("give me the filename:")

filename = input("< ")

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
