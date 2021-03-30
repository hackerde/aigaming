botName='somecoolbotname'

import random
import json
from random import randint

# =============================================================================
# This calculateMove() function is where you need to write your code. When it
# is first loaded, it will play a complete game for you using the Helper
# functions that are defined below. The Helper functions give great example
# code that shows you how to manipulate the data you receive and the move
# that you have to return.
#

def calculateMove(gameState):
    ret = dict()
    pos = randomGuesser(gameState)
    print('My move is '+str(pos))
    ret['Position'] = pos
    return ret

def randomGuesser(gameState): #Randomly guesses a position
    move = randint(0,8) #Random guess
    while(gameState["Board"][move] != " "): #If taken...
        move = randint(0,8) #... keep random guessing until found one
    return move