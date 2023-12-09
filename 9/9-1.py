def GetNextValue(values):
    differences = [0] * (len(values) - 1)
    for i in range(0, len(values) - 1):
        differences[i] = values[i + 1] - values[i]
    
    if all(x == differences[0] for x in differences):
        nextdiff = differences[0]
    else:
        nextdiff = GetNextValue(differences)

    return values[-1] + nextdiff

f = open("9/input.txt", "r")

lines = f.read().splitlines()

nextvalues = []

for line in lines:
    values = line.split(" ")
    values = list(map(int, values))
    nextvalue = GetNextValue(values)
    nextvalues.append(nextvalue)

print(sum(nextvalues))