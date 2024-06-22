import random
import math

lower = int(input("Enter Lower bound : "))
upper = int(input("Enter Upper bound : "))

chance = round(math.log(upper - lower + 1, 2))

x = random.randint(lower, upper)
print(f"\n\tYou've only {chance} chance to guess the number!\n")

count = 0

while count < chance:
    count+=1

    guess = int(input("Guess a number : "))

    if x == guess:
        print(f"\nCongratulation you did it in {count} try\n")
        break
    elif x > guess:
        print("Too small!")
    elif x < guess:
        print("Too high!")

    if count >= chance:
        print(f"\nThe number is {x}")
        print("Better luck Next time!")