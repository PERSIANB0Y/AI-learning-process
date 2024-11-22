import keyboard

maze = [
    [7,8,4],
    [0,3,2],
    [5,1,6],
    ["",0,0]
]
mazeState = maze.copy()

T = []

spaceLocation = [0,0]
availableR = True
availableL = True
availableU = True
availableD = True

stateRow = 0
stateColumn = 0

def spaceFinder():
    global maze, stateRow, stateColumn, spaceLocation
    for i in range(3):
        for ii in maze[i]:
            if ii == 0:
                spaceLocation = [i, stateColumn]
            stateColumn+=1
        stateColumn = 0
    stateRow = 0

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

def moveSpace(direction):
    if direction=="left":
        doLeft()
    if direction=="left":
        doLeft()
    if direction=="left":
        doLeft()
    if direction=="left":
        doLeft()

def appendT(data, T):
    T.append(data)
    

def doRight():
    global mazeState
    if availableR:
        mazeState[spaceLocation[0]][spaceLocation[1]] = mazeState[spaceLocation[0]][spaceLocation[1]+1]
        mazeState[spaceLocation[0]][spaceLocation[1]+1] = 0
        
        spaceLocation[1] += 1
        availableDirections()
        appendT(mazeState, T)


    else: print("direction is not available")
    print()
    print("Maze state:")
    render(mazeState)
    print()
    print("Temp:")
    render(T)
    print()
    print()

def render(maze):
    for i in maze:
        print(i)

def doLeft():
    print("left")
def doUp():
    print("up")
def doDown():
    print("down")


spaceFinder()
availableDirections()


keyboard.add_hotkey("left", doLeft)
keyboard.add_hotkey("right", doRight)
keyboard.add_hotkey("up", doUp)
keyboard.add_hotkey("down", doDown)

keyboard.wait()