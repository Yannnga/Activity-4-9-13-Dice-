#import part
from random import randint

#Creat class
class Dice():
    def __init__(self, side = 6):
        self.__sides = side

    def roll_dice(self):
        random_number = randint(1, self.__sides)
        print(random_number)
#Creat 6 side dice
dice = Dice()

#roll 10 times
roll_time = 0
while roll_time < 10:
    dice.roll_dice()
    roll_time += 1
