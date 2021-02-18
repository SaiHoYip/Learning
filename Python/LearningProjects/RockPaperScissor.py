import random, sys
Player = True
while (Player == True):
    PlayerChoice = input('Type Rock Paper Or Scissor: ')
    ComputerChoose = random.randint(1,3)
    if ComputerChoose == 1:
        computerMove = 'Rock'
        print("Computer chose Rock")
    elif ComputerChoose == 2:
        computerMove = 'Paper'
        print("Computer chose Scissor")
    elif ComputerChoose == 3:
        computerMove = 'Scissor'
        print("Computer chose scissor")
    if PlayerChoice == computerMove:
        print("You Tied!")
    elif PlayerChoice == 'Rock' and computerMove == 'Scissor':
        print("You Won!")
    elif PlayerChoice == 'Rock' and computerMove == 'Paper':
        print("You Lost. Better Luck Next Time!")
    elif PlayerChoice == 'Paper' and computerMove == 'Scissor':
        print("You Lost. Better Luck Next Time!")
    elif PlayerChoice == 'Paper' and computerMove == 'Rock':
        print("You Won!")
    elif PlayerChoice == 'Scissor' and computerMove == 'Rock':
        print("You Lost. Better Luck Next Time!")
    elif PlayerChoice == 'Paper' and computerMove == 'Paper':
        print("You Won!")
    Continue = input("Do you want to keep playing? (Type Y or N): ")
    if Continue == "Y":
        Player = True
    elif Continue == "N":
        Player = False
