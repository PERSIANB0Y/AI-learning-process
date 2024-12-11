import keyboard
import time
import copy

maze = [
    [7,1,4],
    [0,3,2],
    [5,8,6],
    ["",0,0]
]
mazeTarget = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]
mazeState = copy.copy(maze)
path, T = [], []
directions = ["R", "L", "U", "D"]
spaceNextLocation, spaceLocation, subjectLocation = [0,0], [0,0], [0,0]
availableR, availableL, availableD, availableU = True, True, True, True
totalMoves, stateRow, stateColumn = 0, 0, 0
num1,num2,num3,num4,num5,num6,num7,num8 = 0,0,0,0,0,0,0,0

def searchLocation(subject):
    global stateColumn, subjectLocation, spaceLocation
    for i in range(3):
        for ii in mazeState[i]:
            if ii == subject:
                if subject == 0 :
                    spaceLocation = [i, stateColumn]
                else:
                    subjectLocation = [i, stateColumn]
            stateColumn+=1
        stateColumn = 0
    print(f"subjectLocation : {subjectLocation}")

# searchLocation(int(input("enter the thing youre looking for...:")))




def availableDirections():
    global availableL,availableR,availableU,availableD, spaceLocation

    availableR = True
    availableL = True
    availableU = True
    availableD = True

    if spaceLocation[1] == 2:
        availableR = False
    if spaceLocation[1] == 0:
        availableL = False
    if spaceLocation[0] == 2:
        availableD = False
    if spaceLocation[0] == 0:
        availableU = False


def move(direction):
    if direction=="R":
        doRight()
    if direction=="L":
        doLeft()
    if direction=="U":
        doUp()
    if direction=="D":
        doDown()
    

def doRight():
    global mazeState, totalMoves
    if availableR:
        mazeState[spaceLocation[0]][spaceLocation[1]] = mazeState[spaceLocation[0]][spaceLocation[1]+1]
        mazeState[spaceLocation[0]][spaceLocation[1]+1] = 0
        mazeState[3][0] = "R"
        mazeState[3][1] = totalMoves
        mazeState[3][2] = len(path)

        spaceLocation[1] += 1
        availableDirections()
        T.append(copy.deepcopy(mazeState))
    else: print("direction is not available")
    render(mazeState)
    totalMoves += 1

def doLeft():
    global mazeState, totalMoves
    if availableL:
        mazeState[spaceLocation[0]][spaceLocation[1]] = mazeState[spaceLocation[0]][spaceLocation[1]-1]
        mazeState[spaceLocation[0]][spaceLocation[1]-1] = 0
        mazeState[3][0] = "L"
        mazeState[3][1] = totalMoves
        mazeState[3][2] = len(path)
        
        spaceLocation[1] -= 1
        availableDirections()
        T.append(copy.deepcopy(mazeState))
    else: print("direction is not available")
    render(mazeState)
    totalMoves += 1

def doUp():
    global mazeState, totalMoves
    if availableU:
        mazeState[spaceLocation[0]][spaceLocation[1]] = mazeState[spaceLocation[0]-1][spaceLocation[1]]
        mazeState[spaceLocation[0]-1][spaceLocation[1]] = 0
        mazeState[3][0] = "U"
        mazeState[3][1] = totalMoves
        mazeState[3][2] = len(path)
        
        spaceLocation[0] -= 1
        availableDirections()
        T.append(copy.deepcopy(mazeState))
    else: print("direction is not available")
    render(mazeState)
    totalMoves += 1

def doDown():
    global mazeState, totalMoves
    if availableD:
        mazeState[spaceLocation[0]][spaceLocation[1]] = mazeState[spaceLocation[0]+1][spaceLocation[1]]
        mazeState[spaceLocation[0]+1][spaceLocation[1]] = 0
        mazeState[3][0] = "D"
        mazeState[3][2] = len(path)
        mazeState[3][1] = totalMoves
        
        spaceLocation[0] += 1
        availableDirections()
        T.append(copy.deepcopy(mazeState))
    else: print("direction is not available")
    render(mazeState)
    totalMoves += 1


def render(maze):
    print("render output:")
    for i in maze:
        print(i)
    print(f"spaceLocation : {spaceLocation}")
    print()

def checkTarget():
    global mazeState
    if mazeTarget in mazeState:
        print("your puzzle is done")
        print(f"total moves need to solve the puzzle : {len(totalMoves)}")
        print(f"minimum moves need to solve the puzzle : {len(path)}")
        print(f"best path to solve the puzzle : {path}")
    # else:
        # time.sleep(1)
        # checkTarget()


def orderer():
    searchLocation(0)
    if mazeState[0][0] != 1:
        print("one is not in corect position")
        searchLocation(1)
        if subjectLocation[0] == 0: print("the 1 is in a correct row")
        else:
            # for i in range(subjectLocation[0]-1):
            print("the 1 is not in a correct row")
            print(f"it has to go {-subjectLocation[0]} vertically")
        if subjectLocation[1] == 0: print("the 1 is in a correct column")
        else: 
            print("the 1 is not in a correct column")
            print(f"it has to go {-subjectLocation[1]} horizontaly")
        

orderer()
checkTarget()
searchLocation(0)
availableDirections()
render(mazeState)



def temp():render(T)
keyboard.add_hotkey("left", doLeft)
keyboard.add_hotkey("right", doRight)
keyboard.add_hotkey("up", doUp)
keyboard.add_hotkey("down", doDown)
keyboard.add_hotkey("0", temp)

keyboard.wait()