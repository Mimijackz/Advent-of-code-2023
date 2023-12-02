def GetGameData(game):
    sets = game.split("; ")

    data = [[]] * len(sets)
    for i in range(0, len(data)):
        data[i] = [0] * 3

    for i in range(0, len(sets)):
        cubes = sets[i].replace("\n", "").split(", ")
        for cube in cubes:
            cubedata = cube.split(" ")
            if (cubedata[1] == "red"):
                index = 0
            if (cubedata[1] == "green"):
                index = 1
            if (cubedata[1] == "blue"):
                index = 2
            data[i][index] = int(cubedata[0])
    return data
            
possiblevalues = [12, 13, 14]

f = open("2/input.txt", "r")

inputs = f.readlines()

possiblegames = []

for game in inputs:
    game = game.split(": ")
    id = int(game[0][len("Game "):])

    data = GetGameData(game[1])
    maxvalues = [0] * 3
    for set in data:
        for i in range(0, len(maxvalues)):
            maxvalues[i] = max(maxvalues[i], set[i])

    if (maxvalues[0] <= possiblevalues[0] and maxvalues[1] <= possiblevalues[1] and maxvalues[2] <= possiblevalues[2]):
        possiblegames.append(id)

sum = 0
for id in possiblegames:
    sum += id
print(sum)