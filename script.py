import random
import math

name = "script"


def moveTo(x, y, Pirate):
    # move to point(x,y)
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
    # pirate move away from point(x,y) in random motion
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1

def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    # pirate moves in square around point(x,y) with sidelength=2*radius 
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

def investigate_island(pirate):
    # check if nearby in range of 1 tile tile is present
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    sw = pirate.investigate_sw()
    se=pirate.investigate_se()
    nw=pirate.investigate_nw()
    ne=pirate.investigate_ne()
    if ("island" in up[0:-1] or "island" in down[0:-1] or "island" in left[0:-1] or "island" in right[0:-1] or "island" in se[0:-1] or "island" in sw[0:-1] or "island" in nw[0:-1] or "island" in ne[0:-1]):
        return True 
    else:
        return False

def checkIsland(pirate):
    # check if pirate is present on 9 tiles of island
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    sw = pirate.investigate_sw()
    se=pirate.investigate_se()
    nw=pirate.investigate_nw()
    ne=pirate.investigate_ne()
    if ("island" in up[0:1] or "island" in down[0:-1] ) and ("island" in left[0:-1] or "island" in right[0:-1]):
        return True
    else:
        return False


def ActPirate(pirate):

        
    # complete this function
    _id=int(pirate.getID())
    curr_x=pirate.getPosition()[0]
    curr_y=pirate.getPosition()[1]
    if(_id%4==3):
        moveAway()
        
    pass


def ActTeam(team):
    # complete this function
    pass