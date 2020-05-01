def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDEING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age : {age}, Heigt: {height}, Weight: {weight}, IQ : {iq}")


print("Here is a pulzzle.")

waht = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That become:", waht, "Can you do it by hand?")

#def what(age,height,weight,iq):
#    print(f"What {age} + ({height} - ({weight} * ({iq} / 2)))")
#    return age + (height - (weight * (iq / 2)))
#print("Here is the result from upon new formel:", what)

def what(a,b,c,d):
    print(f"NEW RESULT {a} + ({b} - ({c} * ({d} / 2)))")
    return a + (b - (c * (d / 2)))
new_result = what(age,74,weight,50)
print("Here is the result from upon new formel:", new_result)
