
import random
from random import randint

#virtual dice web page test

#First import  flask and SQLalquimist for framework
#import Radom Randint ->>



##############################################################
def dice_roll(dice_num, dice_face):
    result = []
    int(dice_num)
    int(dice_face)
    for _ in range(0, dice_num):
        result.append(random.randint(1, dice_face))
    return result
        #DICE FUNCTION CODE ###################

# user_input =dice_roll(int(input('number of dice?')),int(input('dice faces?')))
# print(user_input)

test = dice_roll(2,20)
print(sum(test))
print(test)


