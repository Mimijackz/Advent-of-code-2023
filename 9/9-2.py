def GetPreviousValue(values):
    differences = [0] * (len(values) - 1)
    for i in range(0, len(values) - 1):
        differences[i] = values[i + 1] - values[i]
    
    #print(differences)
    if all(x == differences[0] for x in differences):
        prevdiff = differences[0]
    else:
        prevdiff = GetPreviousValue(differences)

    #print(prevdiff)
    return values[0] - prevdiff



f = open("9/input.txt", "r")

lines = f.read().splitlines()

nextvalues = []

for line in lines:
    values = line.split(" ")
    values = list(map(int, values))
    nextvalue = GetPreviousValue(values)
    nextvalues.append(nextvalue)
    print(nextvalue)

print("sum: " + str(sum(nextvalues)))