from random import randint

class Dice(object):
    def __init__(self, object):
        self.dice_name = object
        self.min_roll = 1
        self.max_roll = 6
    
    def roll_dice(self):
        return randint(self.min_roll, self.max_roll)

    
dice_1 = Dice('dice_1')
dice_2 = Dice('dice_2')

total = dice_1.roll_dice() +  dice_2.roll_dice()
print(total)

# user = input(f'What is your name ')
# exit_status = ''

# while exit_status is not 'q':
    
#     print(total)
#     exit_status = input(f'Press any key to continue or')


