# define the Function "cheese_and_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you habe {boxes_of_crackers} boxes of cracker!")
    print("Man that's enough for a party!")
    print("Get a blankt.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# variables in script and funtion have no connection.
print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 +6)

print("And we can conine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
