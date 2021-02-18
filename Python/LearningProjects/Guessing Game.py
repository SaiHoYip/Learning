SecretWord = "Goat"
UserGuess = ""
Limit = 5
Try = 0
LimitReached = False

while UserGuess != SecretWord and LimitReached == False:
    if (Try < Limit):
        UserGuess = input("Enter a Guess: ")
        Try +=1
    else:
        LimitReached = True
if LimitReached == True:
    print("You ran out of guesses. Better luck next time!")
else:
    print("Congrats you guessed the word! Good job.")

