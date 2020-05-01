# existe
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copy from {from_file} to {to_file}")

#in_file = open(from_file)
#indate = in_file.read()

#open the file "from_file" then read this file as "indate"
indate = open(from_file).read()
print(f"the input file is {len(indate)} bytes long")
#"len" say the lange of the "indate"

# exitst wll kown, wether here ist ture or flase
print(f"Does the output file exist?{exists(to_file)}")
print("ready, hit RETURN to continue, CTRL-C to abort.")
input()

#out_file = open(to_file, 'w')
#out_file.write(indate)
open(to_file,'w').write(indate)
#open the file "to_file" then write "indate" into "to_file"

print("Alright, all done.")

#out_file.close()
#in_file.close()
