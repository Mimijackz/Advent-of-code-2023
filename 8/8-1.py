def FindLocation(key, locations):
    for i in range(len(locations)):
        if locations[i][0:3] == key:
            return i
    return -1
        
def GetElements(line):
    elements = line[len("XXX = ("):len("XXX = (XXX,XXX)")].split(", ")
    return elements

f = open("8/input.txt")

lines = f.read().splitlines()

instructions = [*(lines[0])]
locations = lines[2:]

print(instructions)
print(locations)

currentlocation = FindLocation("AAA", locations)
currentkey = "AAA"
currentinstruction = 0
instructionlength = len(instructions)
while currentkey != "ZZZ":
    directions = GetElements(locations[currentlocation])

    if instructions[currentinstruction % instructionlength] == "L":
        direction = 0
    else:
        direction = 1
    currentkey = directions[direction]

    currentlocation = FindLocation(currentkey, locations)
    currentinstruction += 1
    print(currentinstruction)
    print(currentkey)

print(currentkey)
print(currentinstruction)