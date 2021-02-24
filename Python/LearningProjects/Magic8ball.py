#everytime this program is run it will grab a random index from the list
import random
magicball = [
    "Yes", "No", "Undoubtedly", "For Sure", "Ask again", "Maybe", "Ask again later", "Doubt it"
]

print(magicball[random.randint(0, len(magicball) -1)])