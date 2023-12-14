def PushRocksNorth(formation):
    newformation = formation.copy()
    for line in range(len(formation)):
        for char in range(len(formation[line])):
            if (formation[line][char] == "O"):
                newpos = line
                newformation[line] = newformation[line][:char] + "." + newformation[line][char + 1:]
                #print("rock at " + str(line) + ":" + str(char))
                for i in range(line, -1, -1):
                    #print(i)
                    #print(newformation[i][char])
                    if newformation[i][char] == "O" or newformation[i][char] == "#":
                        #print("break")
                        break
                    newpos = i
                newformation[newpos] = newformation[newpos][:char] + "O" + newformation[newpos][char + 1:]
    return newformation

def PushRocksSouth(formation):
    newformation = formation.copy()
    for line in range(len(formation) - 1, -1, -1):
        for char in range(len(formation[line])):
            if (formation[line][char] == "O"):
                newpos = line
                newformation[line] = newformation[line][:char] + "." + newformation[line][char + 1:]
                #print("rock at " + str(line) + ":" + str(char))
                for i in range(line, len(formation[line]), 1):
                    #print(i)
                    #print(newformation[i][char])
                    if newformation[i][char] == "O" or newformation[i][char] == "#":
                        #print("break")
                        break
                    newpos = i
                newformation[newpos] = newformation[newpos][:char] + "O" + newformation[newpos][char + 1:]
    return newformation

def PushRocksWest(formation):
    newformation = formation.copy()
    for line in range(len(formation)):
        for char in range(len(formation[line])):
            if (formation[line][char] == "O"):
                newpos = char
                newformation[line] = newformation[line][:char] + "." + newformation[line][char + 1:]
                for i in range(char, -1, -1):
                    if newformation[line][i] == "O" or newformation[line][i] == "#":
                        break
                    newpos = i
                newformation[line] = newformation[line][:newpos] + "O" + newformation[line][newpos + 1:]
    return newformation

def PushRocksEast(formation):
    newformation = formation.copy()
    for line in range(len(formation)):
        for char in range(len(formation[line]) - 1, -1, -1):
            if (formation[line][char] == "O"):
                newpos = char
                newformation[line] = newformation[line][:char] + "." + newformation[line][char + 1:]
                for i in range(char, len(formation[line]), 1):
                    if newformation[line][i] == "O" or newformation[line][i] == "#":
                        break
                    newpos = i
                newformation[line] = newformation[line][:newpos] + "O" + newformation[line][newpos + 1:]
    return newformation

def PushRocksCycle(formation):
    return PushRocksEast(PushRocksSouth(PushRocksWest(PushRocksNorth(formation))))

def CountRockWeights(formation):
    totalweight = 0
    for i in range(len(formation)):
        for char in formation[i]:
            if char == "O":
                totalweight += len(formation) - i
    return totalweight

f = open("14/input.txt", "r")

lines = f.read().splitlines()

#print("\n".join(lines))

loop = []

formation = lines.copy()
repeated = []
waittime = 0
offset = 0
for i in range(1000000):
    print("Progress: " + str(i), end="\r")
    newformation = PushRocksCycle(formation)
    if not newformation in loop:
        #print("change at " + str(i))
        formation = newformation
        loop.append(newformation)
    else:
        #print("repeat at " + str(loop.index(newformation)) + " after " + str(waittime))
        formation = newformation
        if len(repeated) > 0 and formation == repeated[0]:
            break
        if len(repeated) == 0:
            offset = waittime
            waittime = 0
        repeated.append(formation)
    
    waittime += 1
print("\n")
index = (1000000000-offset) % (waittime) - 1
print(CountRockWeights(repeated[index]))
