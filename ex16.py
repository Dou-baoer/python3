from sys import argv

# script is the name of the script, here is the "en16.py". filename is the 2rd.
# = assigment
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")

# open is must be done before other command.  "read" "write"
#'w' is the write model to add.
target = open(filename, 'w')

print("Truncating the file. Goodbye!")

#cut from here
target.truncate()

print("Now I'm going to ask you for three lines.")

#in shell write something
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these to the file.")

#write into the file
target.write (line1)
#\n is the new line
target.write ("\n")
target.write (line3)
target.write ("\n")
target.write (line3)
target.write ("\n")

#target.write (line1 \n, line2 \n, line3 \n)
#target.write (line1\nline2\nline3\n)

print ("And finally, we close it.")

#when it finished it's must be close 
target.close()
