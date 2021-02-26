#activity from https://automatetheboringstuff.com/2e/chapter6/
#try it out!
#import zombiedice
#Don't forget to do pip install zombiedice in console to run this program!
#zombiedice.demo()
import zombiedice
import random
#bot stops after rolling two shotguns
class StopTwoShotguns:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        shotgun = 0
        diceRollResults = zombiedice.roll()  # first roll
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun != 2:
                diceRollResults = zombiedice.roll()
            else:
                break
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
#bot has a 50|50 chance of stopping or continuing after the first roll
class ContinueStop:
    def __init__(self,name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            Active = random.randint(1,2)
            brains += diceRollResults['brains']
            if Active == 1:
                diceRollResults = zombiedice.roll()
                continue
            elif Active == 2:
                break
#bot will stop after rolling two brains
class StopTwoBrain:
    def __init__(self,name):
        self.name = name
    def turn(self,gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    StopTwoShotguns(name='StopTwoShotguns'),
    ContinueStop(name='Continue/Stop'),
    StopTwoBrain(name='Stop at 2 Brains')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)