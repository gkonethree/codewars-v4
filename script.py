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
    
    
    # 1:up
    # 2:right
    # 3:down
    # 4:left

def ActPirate(pirate):
    _id=int(pirate.getID())
    x=int(pirate.getPosition()[0])
    y=int(pirate.getPosition()[1])
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    nw = pirate.investigate_nw()
    ne = pirate.investigate_ne()
    sw = pirate.investigate_sw()
    se = pirate.investigate_se()
    s = pirate.trackPlayers()
    squad=_id%4
    pirate.setSignal(';')
    curr_sig=pirate.getSignal()
    
    island_pos=[[-1,-1],[-1,-1],[-1,-1]]
    
    for i in range(3):
        if island_pos[i][0]!=-1:
            if pirate.trackPlayers()[i]!="myCaptured":
                x=island_pos[i][0]
                y=island_pos[i][1]
                if squad==2:
                    moveTo(x,y,pirate)
    # if island is not captured by us squad[2] will go to the island   

    # scouting captured island
    # def scoutIsland(pirate, islandCenterX, islandCenterY, islandRadius):
        # position = pirate.getPosition()
        # x, y = position
        # if :
        # some condition for pirates which are alloted for scouting
            # moveTo(islandCenterX,islandCenterY,pirate)
            # while True:
                # moveTo(islandCenterX,islandCenterY+1,pirate)
                # moveTo(islandCenterX+1,islandCenterY+1,pirate)
                # moveTo(islandCenterX+1,islandCenterY,pirate)
                # moveTo(islandCenterX+1,islandCenterY-1,pirate)
                # moveTo(islandCenterX,islandCenterY-1,pirate)
                # moveTo(islandCenterX,islandCenterY,pirate)
                # moveTo(islandCenterX,islandCenterY+1,pirate)
                # moveTo(islandCenterX-1,islandCenterY+1,pirate)
                # moveTo(islandCenterX-1,islandCenterY,pirate)
                # moveTo(islandCenterX-1,islandCenterY-1,pirate)
                # moveTo(islandCenterX,islandCenterY-1,pirate)
                # moveTo(islandCenterX,islandCenterY,pirate)        





    if (up==("island1" or "island2" or "island3") and pirate.investigate_up()[1]==("enemy" ) and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
        return 1
    if (down==("island1" or "island2" or "island3") and pirate.investigate_down()[1]==("enemy" ) and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
        return 3
    if (left==("island1" or "island2" or "island3") and pirate.investigate_left()[1]==("enemy" ) and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
        return 4
    if (right==("island1" or "island2" or "island3") and pirate.investigate_right()[1]==("enemy" ) and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
        return 2


#team signalling

    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        sig = up[-1] + str(x) + "," + str(y - 1)+","+str(squad)
        pirate.setTeamSignal(sig)
        if len(curr_sig)==1:
            pirate.setSignal(curr_sig+'s')
        return moveTo(x,y-1,pirate)

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        sig = down[-1] + str(x) + "," + str(y + 1)+","+str(squad)
        pirate.setTeamSignal(sig)
        pirate.setSignal(curr_sig+'s')
        return moveTo(x,y+1,pirate)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        sig = left[-1] + str(x - 1) + "," + str(y)+","+str(squad)
        pirate.setTeamSignal(sig)
        
        pirate.setSignal(curr_sig+'s')
        return moveTo(x-1,y,pirate)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        sig = right[-1] + str(x + 1) + "," + str(y)+","+str(squad)
        pirate.setTeamSignal(sig)
        curr_sig=pirate.getSignal()
        pirate.setSignal(curr_sig+'s')
        return moveTo(x+1,y,pirate)

    if (
        (nw == "island1" and s[0] != "myCaptured")
        or (nw == "island2" and s[1] != "myCaptured")
        or (nw == "island3" and s[2] != "myCaptured")
    ):
        sig = nw[-1] + str(x -1) + "," + str(y-1)+","+str(squad)
        pirate.setTeamSignal(sig)
        pirate.setSignal(curr_sig+'s')
        return moveTo(x-1,y-1,pirate)

    if (
        (se == "island1" and s[0] != "myCaptured")
        or (se == "island2" and s[1] != "myCaptured")
        or (se == "island3" and s[2] != "myCaptured")
    ):
        sig = se[-1] + str(x +1) + "," + str(y+1)+","+str(squad)
        pirate.setTeamSignal(sig)
        pirate.setSignal(curr_sig+'s')
        return moveTo(x+1,y+1,pirate)

    if (
        (ne == "island1" and s[0] != "myCaptured")
        or (ne == "island2" and s[1] != "myCaptured")
        or (ne == "island3" and s[2] != "myCaptured")
    ):
        sig = ne[-1] + str(x+1) + "," + str(y-1)+","+str(squad)
        pirate.setTeamSignal(sig)
        pirate.setSignal(curr_sig+'s')
        return moveTo(x+1,y-1,pirate)

    if (
        (sw == "island1" and s[0] != "myCaptured")
        or (sw == "island2" and s[1] != "myCaptured")
        or (sw == "island3" and s[2] != "myCaptured")
    ):
        sig = sw[-1] + str(x -1) + "," + str(y+1)+","+str(squad)
        pirate.setTeamSignal(sig)
        pirate.setSignal(curr_sig+'s')
        return moveTo(x-1,y+1,pirate)
    
    if len(str(pirate.getSignal))==2 and pirate.getSignal()[1]=='s':
        return
    
    if (up==("island1" or "island2" or "island3") and pirate.investigate_up()[1]==("enemy" or "both") and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
        return 1
    if (down==("island1" or "island2" or "island3") and pirate.investigate_down()[1]==("enemy" or "both") and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
        return 3
    if (left==("island1" or "island2" or "island3") and pirate.investigate_left()[1]==("enemy" or "both") and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
        return 4
    if (right==("island1" or "island2" or "island3") and pirate.investigate_right()[1]==("enemy" or "both") and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
        return 2
    if(squad==3):
        return moveAway(x,y,pirate)

   

    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        i=int(l[0])
        xi = int(l[0][1:])
        yi = int(l[1])
        # if island_pos[i][0] == -1:
        #     island_pos[i][0]=xi
        #     island_pos[i][1]=yi
        if (up==("island1" or "island2" or "island3") and pirate.investigate_up()[1]==("enemy" or "both") and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
            return 1
        if (down==("island1" or "island2" or "island3") and pirate.investigate_down()[1]==("enemy" or "both") and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
            return 3
        if (left==("island1" or "island2" or "island3") and pirate.investigate_left()[1]==("enemy" or "both") and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
            return 4
        if (right==("island1" or "island2" or "island3") and pirate.investigate_right()[1]==("enemy" or "both") and pirate.getTotalGunpowder() >100 and checkIsland(pirate)==True):
            return 2

        asquad=int(l[2])
        if (asquad==0) and squad==asquad:
            return moveTo(x, y, pirate)
        elif(asquad==1) and squad==asquad:
            return moveTo(x,y,pirate)
        elif(asquad==2) and squad==asquad:
            return moveTo(x,y,pirate)
        elif(asquad==3) and squad==2:
            return moveTo(x,y,pirate)
#teams

    if pirate.getSignal() == '':
        pirate.setSignal('988080')
    # if (squad == 2):
    #     return moveAway(x, y, pirate)
    # _id % 4 == 1 vertical                          1   2
    # _id % 4 == 0 horizontal                        4   3
    if _id % 4 == 0 or _id % 4 == 1 or _id%4==2:
        return Direction(pirate)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    
    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")


def Direction(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    if up[0] == 'wall' and left[0] == 'wall':
        signal = pirate.getSignal()
        signal = '1' + signal[1:]
        pirate.setSignal(signal)  # 1   2
    elif up[0] == 'wall' and right[0] == 'wall':  # 4   3
        signal = pirate.getSignal()
        signal = '2' + signal[1:]
        pirate.setSignal(signal)
    elif down[0] == 'wall' and right[0] == 'wall':
        signal = pirate.getSignal()
        signal = '3' + signal[1:]
        pirate.setSignal(signal)
    elif down[0] == 'wall' and left[0] == 'wall':
        signal = pirate.getSignal()
        signal = '4' + signal[1:]
        pirate.setSignal(signal)
    elif up[0] == 'wall':
        signal = pirate.getSignal()
        if pirate.getSignal() == '4':
            signal = '2' + signal[1:]
        else:
            signal = '1' + signal[1:]
        pirate.setSignal(signal)
    elif down[0] == 'wall':
        signal = pirate.getSignal()
        if pirate.getSignal() == '1':
            signal = '4' + signal[1:]
        else:
            signal = '3' + signal[1:]
        pirate.setSignal(signal)
    elif left[0] == 'wall':
        signal = pirate.getSignal()
        if pirate.getSignal() == '2':
            signal = '4' + signal[1:]
        else:
            signal = '1' + signal[1:]
        pirate.setSignal(signal)
    elif right[0] == 'wall':
        signal = pirate.getSignal()
        if pirate.getSignal() == '1':
            signal = '3' + signal[1:]
        else:
            signal = '2' + signal[1:]
        pirate.setSignal(signal)
    dir = pirate.getSignal()[0]
    if int(pirate.getID()) % 4 == 0:
        if dir == '1':
            arr = [3, 3, 3, 2, 2, 2, 2, 2, 2, 2]
            return random.choice(arr)
        if dir == '2':
            arr = [3, 3, 3, 4, 4, 4, 4, 4, 4, 4]
            return random.choice(arr)
        if dir == '3':
            arr = [1, 1, 1, 4, 4, 4, 4, 4, 4, 4]
            return random.choice(arr)
        if dir == '4':
            arr = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
            return random.choice(arr)
    if int(pirate.getID()) % 4 == 1:
        if dir == '1':
            arr = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2]
            return random.choice(arr)
        if dir == '2':
            arr = [3, 3, 3, 3, 3, 3, 3, 4, 4, 4]
            return random.choice(arr)
        if dir == '3':
            arr = [1, 1, 1, 1, 1, 1, 1, 4, 4, 4]
            return random.choice(arr)
        if dir == '4':
            arr = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2]
            return random.choice(arr)
    if int(pirate.getID()) % 4 == 2:
        if dir == '1':
            arr = [3, 3, 3, 3, 2, 2, 2, 2, 1, 4]
            return random.choice(arr)
        if dir == '2':
            arr = [3, 3, 3, 3, 4, 4, 4, 4, 1, 2]
            return random.choice(arr)
        if dir == '3':
            arr = [1, 1, 1, 1, 4, 4, 4, 4, 2, 3]
            return random.choice(arr)
        if dir == '4':
            arr = [1, 1, 1, 1, 2, 2, 2, 2, 4, 3]
            return random.choice(arr)
