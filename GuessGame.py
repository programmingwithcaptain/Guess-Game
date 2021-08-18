# Guess the computer secret number
import random

secret_number = random.randint(1, 5)
for i in range(0, 3):
    user = int(input("Enter the Guess: "))
    if user == secret_number:
        print(f"Congratulations! You've Guessed the number right its {secret_number}")
        break
if user != secret_number:
    print(f"Your Guesses are incorrect the number is {secret_number}")
