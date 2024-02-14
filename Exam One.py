#Coded by Asa Whitman

PlayerName = str(input("Greetings, player. Enter your name: "))
print("Okay,",PlayerName, ", here are the rules. I'm thinking of a nondecimal number between 1 and 20. You have 5 attempts to guess the correct number. I will tell you if your previous guess is too high or too low. If you guess the correct number by the fifth attempt, you win.")
PlayerReady = str(input('Type "yes" If you are ready to play: '))
if PlayerReady in ['yes']:
    from random import randint
    Answer = randint(1,20)
    Attempts = 5
    Guesses = 0
    PlayerGuess = int(input("Okay, "+ PlayerName +", You have 5 guesses. Guess a number between 1 and 20: "))
    while Attempts > 1:
        if PlayerGuess < 1 or PlayerGuess > 20:
            PlayerGuess = int(input("That is not a valid guess. Please guess a number between 1 and 20: "))
        elif PlayerGuess > Answer:
            Attempts -= 1
            Guesses += 1
            if Attempts == 1:
                print("Too high.",Attempts,"guess left.")
                PlayerGuess = int(input("Guess again: "))
            else:
                print("Too high.",Attempts,"guesses left.")
                PlayerGuess = int(input("Guess again: "))
        elif PlayerGuess < Answer:
            Attempts -= 1
            Guesses += 1
            if Attempts == 1:
                print("Too low.",Attempts,"guess left.")
                PlayerGuess = int(input("Guess again: "))
            else:
                print("Too low.",Attempts,"guesses left.")
                PlayerGuess = int(input("Guess again: "))
        elif PlayerGuess == Answer:
            Guesses += 1
            if Guesses == 1:
                print(Answer,"is correct! Congratuations, "+ PlayerName +"! You guessed the correct number in only",Guesses,"attempt! Lucky you.")
            else:
                print(Answer,"is correct! Congratuations, "+ PlayerName +"! You guessed the correct number in",Guesses,"attempts.")
            break
    else:
        print("Sorry, "+ PlayerName+ ", but it looks like I've won. The correct answer was",Answer)