from math import lcm

def FindLocation(key, locations):
    for i in range(len(locations)):
        if locations[i][0:3] == key:
            return i
    return -1

def IsFinished(ghostlocations):
    for i in range(len(ghostlocations)):
        if ghostlocations[i][0] == 0:
            return False
    return True

def FindLoop(startlocation, locations, instructions):
    offset = -1
    looptime = 0
    currentinstruction = 0
    done = False
    instructionlength = len(instructions)
    currentlocation = startlocation.copy()

    while not done:
        direction = instructions[currentinstruction % instructionlength]
        location = currentlocation
        location = locations[location[direction + 1] + location[3]]
        currentlocation = location
        if (location[0] == 1):
            if offset == -1:
                offset = currentinstruction
            else:
                looptime = currentinstruction - offset
                done = True
        currentinstruction += 1
    return [offset, looptime]

f = open("8/input.txt")

lines = f.read().splitlines()

instructions = [*(lines[0])]
for i in range(len(instructions)):
    instructions[i] = int(instructions[i].replace("L", "0").replace("R", "1"))

locationstrings = lines[2:]
startlocations = []
locations = locationstrings.copy()
for i in range(len(locations)):
    locationstring = locationstrings[i]
    locations[i] = [0,0,0,0]
    lastkey = locationstring[2]
    if (lastkey == "Z"):
        locations[i][0] = 1
    else:
        locations[i][0] = 0
    locations[i][1] = FindLocation(locationstring[7:10], locationstrings) - i
    locations[i][2] = FindLocation(locationstring[12:15], locationstrings) - i
    locations[i][3] = i

    if (lastkey == "A"):
        startlocations.append(locations[i])

print(instructions)
print(len(instructions))
print(locations)

loops = []

for i in range(len(startlocations)):
    loop = FindLoop(startlocations[i], locations, instructions)
    loops.append(loop[1])

print(loops)
print(lcm(*loops))