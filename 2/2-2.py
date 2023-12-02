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
            
f = open("2/input.txt", "r")

inputs = f.readlines()

powers = []

for game in inputs:
    game = game.split(": ")
    id = int(game[0][len("Game "):])

    data = GetGameData(game[1])
    maxvalues = [0] * 3
    for set in data:
        for i in range(0, len(maxvalues)):
            maxvalues[i] = max(maxvalues[i], set[i])
    power = 1
    for value in maxvalues:
        power *= value
    powers.append(power)


sum = 0
for id in powers:
    sum += id
print(sum)