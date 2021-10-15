import random

roll = random.randint(1,6)
print("computer rolled a " + str(roll))

guess = int(input("guess the computed rolled?"))

if guess == roll:
    print("Correct!! They rolled a " + str(roll))
else:
    print("Wrong!! They rolled a " + str(roll))