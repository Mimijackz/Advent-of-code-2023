def ExpandRows(lines, positions):
    newpositions = positions.copy()
    expandingrows = []
    for i in range(len(lines)):
        isempty = True
        for char in lines[i]:
            if char == "#":
                isempty = False
        if isempty:
            expandingrows.append(i)
    
    offset = 0
    for i in range(len(expandingrows)):
        index = expandingrows[i] + offset
        for position in newpositions:
            if position[1] > index:
                position[1] += 999999
        offset += 999999
    
    return newpositions

def ExpandColumns(lines, positions):
    newpositions = positions.copy()
    expandingcolumns = []
    for i in range(len(lines[0])):
        isempty = True
        for row in range(len(lines)):
            char = lines[row][i]
            if char == "#":
                isempty = False
        if isempty:
            expandingcolumns.append(i)

    offset = 0
    for i in range(len(expandingcolumns)):
        index = expandingcolumns[i] + offset
        for position in newpositions:
            if position[0] > index:
                position[0] += 999999
        offset += 999999
    
    return newpositions

f = open("11/input.txt", "r")

lines = f.read().splitlines()

positions = []

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            positions.append([x, y])


positions = ExpandRows(lines,ExpandColumns(lines, positions))

output = ""
for line in lines:
    output += line + "\n"



distances = []
startindex = 0
while startindex < len(positions):
    startposition = positions[startindex]
    for i in range(startindex + 1, len(positions)):
        distance = abs(startposition[0] - positions[i][0]) + abs(startposition[1] - positions[i][1])
        distances.append(distance)
    startindex += 1

print(sum(distances))