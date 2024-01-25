import random

print("Let's play a game")
print("you only get three trials")
choice = input("can you guess what I'm thinking (yes/no): ")
number = random.choice(list(range(1, 10)))
number_of_guesses = 0

while True:
    if choice.lower() == 'yes':
        while number_of_guesses < 3:
            guessed = int(input("Guess a number 1-10: "))
            if guessed != number:
                print("Sorry try again")
                number_of_guesses += 1
            elif guessed == number:
                print("Hurray you won!")
                break
            elif number_of_guesses == 3:
                print("you have exceeded maximum guesses")
                break
    else:
        print("okay")
        break

    play_again = input("Do you wish to play again (yes/no): ")
    if play_again.lower() != 'yes':
        break
