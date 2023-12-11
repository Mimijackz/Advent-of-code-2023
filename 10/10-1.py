def GetPipeDirections(location):
    if not (0 <= location[0] < len(pipes) and 0 <= location[1] < len(pipes[location[0]])):
        return [0,0,0,0]

    char = pipes[location[0]][location[1]]
    print(char)
    pipetranslator = {
        "|":[1,1,0,0],
        "-":[0,0,1,1],
        "L":[1,0,1,0],
        "J":[1,0,0,1],
        "7":[0,1,0,1],
        "F":[0,1,1,0],
        ".":[0,0,0,0],
        "S":[1,1,1,1],
    }
    return pipetranslator[char]

def MoveLocation(location, direction):
    offset = [direction[1] - direction[0],direction[2] - direction[3]]
    return [location[0] + offset[0], location[1] + offset[1]]

def ReverseDirection(direction):
    if direction == 0:
        return 1
    if direction == 1:
        return 0
    if direction == 2:
        return 3
    if direction == 3:
        return 2

f = open("10/input.txt", "r")

pipes = f.read().splitlines()

for i in range(len(pipes)):
    pipes[i] = [*pipes[i]]

print(pipes)

startlocation = [-1,-1]
for y in range(len(pipes)):
    for x in range(len(pipes[y])):
        if pipes[y][x] == "S":
            startlocation = [y, x]

currentlocation = startlocation.copy()
startdirections = [
    GetPipeDirections([startlocation[0] - 1,startlocation[1]])[1],
    GetPipeDirections([startlocation[0] + 1,startlocation[1]])[0],
    GetPipeDirections([startlocation[0],startlocation[1] + 1])[3],
    GetPipeDirections([startlocation[0],startlocation[1] - 1])[2],
]

foundDir = False
for i in range(len(startdirections)):
    if startdirections[i] == 1:
        if foundDir:
            startdirections[i] = 0
        else:
            foundDir = True
            lastdirection = i
currentlocation = MoveLocation(startlocation, startdirections)

step = 1
while not (currentlocation == startlocation and step > 1):
    directions = GetPipeDirections(currentlocation)
    directions[ReverseDirection(lastdirection)] = 0
    
    currentlocation = MoveLocation(currentlocation, directions)
    lastdirection = directions.index(1)
    step += 1
    print(currentlocation)
print(int(step / 2))