i = 0
# [] is list
numbers = []
u = 1
while i < 6:
	print(f"at the top i is {i}")
	numbers.append(i)

#	i = i + 1
	i += 1
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")


print("The numbers:")

for num in numbers:
	print(num)
