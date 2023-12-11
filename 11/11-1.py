def ExpandRows(lines):
    newlines = lines.copy()
    expandingrows = []
    for i in range(len(lines)):
        isempty = True
        for char in newlines[i]:
            if char == "#":
                isempty = False
        if isempty:
            expandingrows.append(i)
    
    offset = 0
    for i in range(len(expandingrows)):
        index = expandingrows[i] + offset
        newlines.insert(index, newlines[index])
        offset += 1
    
    return newlines

def ExpandColumns(lines):
    newlines = lines.copy()
    expandingcolumns = []
    for i in range(len(lines[0])):
        isempty = True
        for row in range(len(lines)):
            char = lines[row][i]
            if char == "#":
                isempty = False
        if isempty:
            expandingcolumns.append(i)
    print(expandingcolumns)
    offset = 0
    for i in range(len(expandingcolumns)):
        index = expandingcolumns[i] + offset
        for row in range(len(newlines)):
            newlines[row] = newlines[row][:index] + newlines[row][index] + newlines[row][index:]
        offset += 1
    
    return newlines

f = open("11/input.txt", "r")

lines = f.read().splitlines()

print(lines)
lines = ExpandRows(ExpandColumns(lines))

output = ""
for line in lines:
    output += line + "\n"
print(output)

positions = []

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            positions.append([x, y])
print(positions)

distances = []
startindex = 0
while startindex < len(positions):
    startposition = positions[startindex]
    for i in range(startindex + 1, len(positions)):
        distance = abs(startposition[0] - positions[i][0]) + abs(startposition[1] - positions[i][1])
        distances.append(distance)
    startindex += 1


print(distances)
print(sum(distances))