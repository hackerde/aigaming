botName='somecoolbotname'

import random
import json
from random import randint
from math import inf as infinity

# =============================================================================
# This calculateMove() function is where you need to write your code. When it
# is first loaded, it will play a OPPlete game for you using the Helper
# functions that are defined below. The Helper functions give great example
# code that shows you how to manipulate the data you receive and the move
# that you have to return.

# Credits: https://github.com/Cledersonbc/tic-tac-toe-minimax/blob/master/py_version/minimax.py

OPP = -1
SELF = +1

def empty_cells(state):

    cells = []

    for c in range(len(state)):
        if state[c] == 0:
            cells.append(c)

    return cells

def calculateMove(gameState):
    ret = dict()
    
    state = list(gameState["Board"])
    for cell in range(len(state)):
        if state[cell] == gameState["Role"]:
            state[cell] = SELF
        elif state[cell] == " ":
            state[cell] = 0
        else:
            state[cell] = OPP

    depth = len(empty_cells(state))
    if depth == 9:
        move = random.choice(list(range(0,9)))
        print('My move is '+str(move))
        ret['Position'] = move
    else:
        move = minimax(state, depth, SELF)
        print('My move is '+str(move[0]))
        ret['Position'] = move[0]

    return ret

def evaluate(state):

    if wins(state, SELF):
        score = +1
    elif wins(state, OPP):
        score = -1
    else:
        score = 0

    return score

def wins(state, player):

    win_state = [
        [state[0], state[1], state[2]],
        [state[3], state[4], state[5]],
        [state[6], state[7], state[8]],
        [state[0], state[3], state[6]],
        [state[1], state[4], state[7]],
        [state[2], state[5], state[8]],
        [state[0], state[4], state[8]],
        [state[6], state[4], state[2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def game_over(state):

    return wins(state, SELF) or wins(state, OPP)

def minimax(state, depth, player):

    if player == SELF:
        best = [-1, -infinity]
    else:
        best = [-1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, score]

    for cell in empty_cells(state):
        state[cell] = player
        score = minimax(state, depth - 1, -player)
        state[cell] = 0
        score[0] = cell

        if player == SELF:
            if score[1] > best[1]:
                best = score  # max value
        else:
            if score[1] < best[1]:
                best = score  # min value

    return best