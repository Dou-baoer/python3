print("How old are you?")
age = input()
print("How tall are you?", end='')
height = input()
print("How much do you weight?", end='')
weight = input()

#h = int(input(height))
#w = int(input(weight))
#h_w = h + w

h_w =int(height) + int(weight)

print(f"so, you are {age} old, {height} tall and {weight} heavy.")
print(f"your height + weight = {h_w}")
