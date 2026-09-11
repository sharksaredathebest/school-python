import random

number = random.randint(1,21)
print(number)
points = 0
guess = 0
correct = False
for i in range(1,5):
    guess = int(input("Guess the number: "))
    if guess == number:
        points += 1
        correct = True
    elif guess != number:
        guess = int(input("Try again: "))





