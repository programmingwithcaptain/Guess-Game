# let the user guess our secret number
secret_number = '7'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_number and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter the Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You LOSE!")
else:
    print("Congratulations! You WIN!")
