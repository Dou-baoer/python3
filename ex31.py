print("""You enter a dark room with two doors.
do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("what do you do?")
    print("1.Take the cake.")
    print("2.Scream at the bear.")
    print("3.run away.")

    bear = input(">")

    if bear == "1":
        print("the bear eats your face off. Good job!")
    elif bear == "2":
        print("the bear eats your legs off. Good job!")
    elif bear == "3":
        print("the bear is faster than you. eats your ass. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("you stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">")
    if insanity == "1" or insanity == "2":
        print("Your boby survives powerd by a mind of jello.")
        print("Good job!")
    else:
    	print("The insantiy rots your eyes into a pool of muck.")
    	print("Good job!")

else:
    print("You stumble around and fall on knife and die. Good job!")
