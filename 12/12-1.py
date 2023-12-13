def GetNumbers(springs):
    consecutivesprings = 0
    order = []
    for spring in springs:
        if (spring == "#"):
            consecutivesprings += 1
        elif consecutivesprings > 0:
            order.append(consecutivesprings)
            consecutivesprings = 0
    if consecutivesprings > 0:
        order.append(consecutivesprings)
    
    
    return order

f = open("12/input.txt","r")

lines = f.read().splitlines()
print(lines)

sum = 0
currentline = 0
for line in lines:
    game = line.split(" ")
    game[1] = list(map(int, game[1].split(",")))
    #print(game)
    
    secrets = []
    for i in range(len(game[0])):
        if game[0][i] == "?":
            secrets.append(i)
    #print(secrets)

    possiblearrangements = []
    for i in range(pow(2, len(secrets))):
        arrangement = bin(i)[len('0b'):].zfill(len(secrets)).replace("0",".").replace("1","#")
        springs = game[0]
        for j in range(len(secrets)):
            index = secrets[j]
            #print(springs)
            #print(index)
            springs = springs[:index] + arrangement[j] + springs[index + 1:]
        #print(springs)
        numbers = GetNumbers(springs)
        #print(numbers)
        if numbers == game[1]:
            #print("A")
            possiblearrangements.append(arrangement)
        
    currentline += 1
    print(str(currentline) + ": " + str(len(possiblearrangements)))
    sum += len(possiblearrangements)

print("sum " + str(sum))
