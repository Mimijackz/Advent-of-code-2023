def MoveLocation(location, direction):
    directiontranslator = {
        0: [-1,0],
        1: [1,0],
        2: [0,1],
        3: [0,-1],
    }
    offset = directiontranslator[direction]
    return [location[0] + offset[0], location[1] + offset[1]]

def GetRay(location, direction, lines, rays):
    currentlocation = location.copy()
    newrays = rays.copy()
    while 0 <= currentlocation[0] < len(lines) and 0 <= currentlocation[1] < len(lines[0]) and not newrays[currentlocation[0]][currentlocation[1]][direction]:
        newrays[currentlocation[0]][currentlocation[1]][direction] = True
        #print("{0},{1},{2}".format(currentlocation[0],currentlocation[1],direction))
        
        char = lines[currentlocation[0]][currentlocation[1]]
        newdirections = BounceRay(direction, char)

        if newdirections[0] == direction:
            currentlocation = MoveLocation(currentlocation, direction)
        else:
            for dir in newdirections:
                newrays = GetRay(MoveLocation(currentlocation, dir), dir, lines, newrays)
            return newrays
    return newrays
        
 

def BounceRay(direction, char):
    newdirections = []
    if char == ".":
        newdirections.append(direction)
    elif char == "|":
        if direction in [0,1]:
            newdirections.append(direction)
        else:
            newdirections.append(0)
            newdirections.append(1)
    elif char == "-":
        if direction in [2,3]:
            newdirections.append(direction)
        else:
            newdirections.append(2)
            newdirections.append(3)
    elif char == "/":
        translator = {
            0:2,
            2:0,
            1:3,
            3:1,
        }
        newdirections.append(translator[direction])
    elif char == "\\":
        translator = {
            0:3,
            3:0,
            1:2,
            2:1,
        }
        newdirections.append(translator[direction])
    return newdirections

def GetEnergizedTiles(start, direction, lines):
    rays = [[[False] * 4 for _ in line] for line in lines]
    rays = GetRay(start, direction, lines, rays)

    total = 0
    for y in range(len(rays)):
        for x in range(len(rays[i])):
            currentray = rays[y][x]
            indexes = [dir for dir in range(len(currentray)) if currentray[dir]]
            if len(indexes) > 0:
                total += 1
    return total


f = open("16/input.txt", "r")

lines = f.read().splitlines()


besttiles = 0
maxy = len(lines) - 1
maxx = len(lines[0]) - 1
for i in range(len(lines)):
    tiles = GetEnergizedTiles([i,0], 2, lines)
    besttiles = max(tiles, besttiles)
for i in range(len(lines[0])):
    tiles = GetEnergizedTiles([0,i], 1, lines)
    besttiles = max(tiles, besttiles)
for i in range(len(lines)):
    tiles = GetEnergizedTiles([i,maxx], 1, lines)
    besttiles = max(tiles, besttiles)
for i in range(len(lines[0])):
    tiles = GetEnergizedTiles([maxy,i], 1, lines)
    besttiles = max(tiles, besttiles)

print(besttiles)