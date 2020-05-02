class Dice(object):
    def __init__(self, object):
        self.dice_name = object
        self.min_roll = 1
        self.max_roll = 6
    
    def roll_dice(self, rolled = True):
        self.rolled = rolled

    
dice_1 = Dice('dice_1')
dice_2 = Dice('dice_2')

print(dice_1.__dict__)
print(dice_2.__dict__)
print(dice_1.max_roll)