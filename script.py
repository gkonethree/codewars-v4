import random
import math

name = "script"


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1

#
def moveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1

def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    position = Pirate.getPosition()
    rx = position[0]
    ry = position[1]
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
    if [rx, ry] not in pos:
        if initial != "abc":
            return moveTo(initial[0], initial[1], Pirate)
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
            y + i for i in range(-1 * radius, radius + 1)
        ]:
            return moveAway(x, y, Pirate)
        else:
            return moveTo(x, y, Pirate)
    else:
        index = pos.index([rx, ry])
        return moveTo(
            pos[(index + (clockwise * 2) - 1) % len(pos)][0],
            pos[(index + (clockwise * 2) - 1) % len(pos)][1],
            Pirate,
        )
    #4 teams : 2 random, 2 horizontal and vertical
def checkIsland(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    nw = pirate.investigate_nw()
    ne = pirate.investigate_ne()
    sw = pirate.investigate_sw()
    se = pirate.investigate_se()
    if (up[0:-1] == "island" or down[0:-1] == "island") and (left[0:-1] == "island" or right[0:-1] == "island"):
        return True
    else:
        return False

def move_horizontal_line(pirate,curr_x,curr_y,direction=1): #1 for right, 0 for left
    if(direction==1):
        if pirate.investigate_right[0]=="wall":
            return 0
        else:
            moveTo(curr_x+1,curr_y)
            return 1
    if (direction==0):
        if pirate.investigate_left[0]=="wall":
            return 0
        else:
            moveTo(curr_x-1,curr_y)
            return 1

def move_vertical_line(pirate,curr_x,curr_y,direction=1): #1 for down, 0 for up
    if(direction==1):
        if pirate.investigate_down[0]=="wall":
            return 0
        else:
            moveTo(curr_x,curr_y+1)
            return 1
    if (direction==0):
        if pirate.investigate_up[0]=="wall":
            return 0
        else:
            moveTo(curr_x,curr_y-1)
            return 1        
        




def ActPirate(pirate):
    # complete this function
    _id=int(pirate.getID())
    curr_x=int(pirate.getPosition()[0])
    curr_y=int(pirate.getPosition()[1])




    #random team 2 and 3
    if(_id%4==3 or _id%4==2):
        return moveAway(curr_x,curr_y,pirate)
    pass


def ActTeam(team):
    # complete this function
    pass