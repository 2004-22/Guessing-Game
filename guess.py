import random


playing = True

while playing:
    print("Let's play a game")
    print("you only get three trials")
    choice = input("can you guess what I'm thinking (yes/no): ")
    number = random.choice(list(range(1, 10)))
    number_of_guesses = 0
    if choice.lower() == 'yes':
        while number_of_guesses < 3:
            guessed = int(input("Guess a number 1-10: "))
            if number_of_guesses == 3:
                break
            elif guessed == number:
                print("Hurray you won!")
                break
            elif guessed != number:
                print("Sorry try again")
                number_of_guesses += 1
    else:
        print("okay")
        break

    if input("Do you wish to play again (yes/no): ").lower() != 'yes':
        playing = False
