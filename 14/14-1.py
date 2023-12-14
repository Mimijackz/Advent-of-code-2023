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

def CountRockWeights(formation):
    totalweight = 0
    for i in range(len(formation)):
        for char in formation[i]:
            if char == "O":
                totalweight += len(formation) - i
    return totalweight

f = open("14/input.txt", "r")

lines = f.read().splitlines()

print("\n".join(lines))


pushedformation = PushRocksNorth(lines)
print("____")
print("\n".join(pushedformation))

weight = CountRockWeights(pushedformation)
print(weight)