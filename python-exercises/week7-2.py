import random
import math
import game


def test(a=100, b=200, c=300):
    print(a)
    
test(500)

print("")

def summation(*nums):
    
    sumnum = 0
    for num in nums:
        sumnum += num

    return sumnum
    
print(summation(6,3,9,22))


    
print(game.rollDice())