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



f = open("16/input.txt", "r")

lines = f.read().splitlines()

rays = [[[False] * 4 for _ in line] for line in lines]


rays = GetRay([0,0], 2, lines, rays)

output = ""
total = 0
for i in range(len(rays)):
    for j in range(len(rays[i])):
        indexes = [dir for dir in range(len(rays[i][j])) if rays[i][j][dir]]
        if len(indexes) > 1:
            output += str(len(indexes))
            total += 1
        elif len(indexes) == 1:
            translator = {
                0: "^",
                1: "V",
                2: ">",
                3: "<",
            }
            output += translator[indexes[0]]
            total += 1
        else:
            output += "."
    output += "\n"
print(output)
print("total: " + str(total))