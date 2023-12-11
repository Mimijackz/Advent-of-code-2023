import sys

def GetPipeDirections(location):
    if not (0 <= location[0] < len(pipes) and 0 <= location[1] < len(pipes[location[0]])):
        return [0,0,0,0]

    char = pipes[location[0]][location[1]]
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

def DirectionToPipe(directions):
    directiontranslator = {
        (1,1,0,0):"|",
        (0,0,1,1):"-",
        (1,0,1,0):"L",
        (1,0,0,1):"J",
        (0,1,0,1):"7",
        (0,1,1,0):"F",
        (0,0,0,0):".",
    }
    directionkey = (directions[0],directions[1],directions[2],directions[3])
    return directiontranslator[directionkey]

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
    
def FloodFill(start, locations):
    sys.setrecursionlimit(len(locations) * len(locations[0]))
    newlocations = locations.copy()
    for offset in [[1,0],[-1,0],[0,1],[0,-1]]:
        target = [start[0] + offset[0], start[1] + offset[1]]

        if not (0 <= target[0] < len(newlocations) and 0 <= target[1] < len(newlocations[target[0]])):
            continue

        value = newlocations[target[0]][target[1]]
        if value == 0:
            newlocations[target[0]][target[1]] = 2
            newlocations = FloodFill(target,locations)
    return locations
        

def ExpandCharacter(char, location, expandedmap):
    chartranslator = {
        ".": [0,0,0,
              0,0,0,
              0,0,0],
        "|": [0,1,0,
              0,1,0,
              0,1,0],
        "-": [0,0,0,
              1,1,1,
              0,0,0],
        "L": [0,1,0,
              0,1,1,
              0,0,0],
        "J": [0,1,0,
              1,1,0,
              0,0,0],
        "7": [0,0,0,
              1,1,0,
              0,1,0],
        "F": [0,0,0,
              0,1,1,
              0,1,0],
    }
    expandedchar = chartranslator[char]
    index = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            expandedmap[location[0] + yoffset][location[1] + xoffset] = expandedchar[index]
            index += 1
    return expandedmap
    

def ExpandMap(locations):
    newMap = [[]] * (len(locations) * 3)
    size = [len(locations) * 3, len(locations[0] * 3)]
    for i in range(size[0]):
        newMap[i] = [0] * size[1]
    
    for y in range(len(locations)):
        for x in range(len(locations[y])):
            newMap = ExpandCharacter(locations[y][x], [y*3+1,x*3+1], newMap)
    return newMap

def ShrinkMap(locations):
    size = [int(len(locations) / 3), int(len(locations[0]) / 3)]
    newMap = [[]] * size[0]
    for i in range(size[0]):
        newMap[i] = [0] * size[1]

    x2 = 0
    y2 = 0
    for y in range(1, len(locations), 3):
        x2 = 0
        for x in range(1, len(locations[0]), 3):
            newMap[y2][x2] = locations[y][x]
            x2 += 1
        y2 += 1
    return newMap



f = open("10/input.txt", "r")

pipes = f.read().splitlines()

for i in range(len(pipes)):
    pipes[i] = [*pipes[i]]

startlocation = [-1,-1]
for y in range(len(pipes)):
    for x in range(len(pipes[y])):
        if pipes[y][x] == "S":
            startlocation = [y, x]

usefulpipes = [[]] * len(pipes)
for i in range(len(usefulpipes)):
    usefulpipes[i] = ["."] * len(pipes[i])

currentlocation = startlocation.copy()
startdirections = [
    GetPipeDirections([startlocation[0] - 1,startlocation[1]])[1],
    GetPipeDirections([startlocation[0] + 1,startlocation[1]])[0],
    GetPipeDirections([startlocation[0],startlocation[1] + 1])[3],
    GetPipeDirections([startlocation[0],startlocation[1] - 1])[2],
]
usefulpipes[startlocation[0]][startlocation[1]] = DirectionToPipe(startdirections)


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
    usefulpipes[currentlocation[0]][currentlocation[1]] = pipes[currentlocation[0]][currentlocation[1]]
    directions = GetPipeDirections(currentlocation)
    directions[ReverseDirection(lastdirection)] = 0
    
    currentlocation = MoveLocation(currentlocation, directions)
    lastdirection = directions.index(1)
    step += 1

output = ""
for column in usefulpipes:
    for char in column:
        output += char
    output += "\n"
print(output)

bigmap = ShrinkMap(FloodFill([0,0],ExpandMap(usefulpipes)))

output = ""
insideloopamount = 0
for column in bigmap:
    for char in column:
        output += str(char)
        if char == 0:
            insideloopamount += 1
    output += "\n"
print(output)

print(insideloopamount)