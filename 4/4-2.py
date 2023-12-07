def StringToIntArray(stringarray):
    intarray = []
    for i in range(len(stringarray)):
        if (str.isdigit(stringarray[i])):
            intarray.append(int(stringarray[i]))
    return intarray

def GetCardNumbers(winners, scratches):
    numbers = []
    for winner in winners:
        for scratch in scratches:
            if winner is scratch:
                numbers.append(winner)
                print(winner)
    numbers = list(dict.fromkeys(numbers))
    return len(numbers)
    


f = open("4/input.txt", "r")

lines = f.read().splitlines()
cardamounts = [1] * len(lines)

for i in range(len(lines)):
    lines[i] = lines[i].split(": ")
    numbers = lines[i][1].split(" | ")
    print(numbers)
    winners = StringToIntArray(numbers[0].split(" "))
    scratches = StringToIntArray(numbers[1].split(" "))
    print(winners)
    print(scratches)

    matches = GetCardNumbers(winners, scratches)
    amount = cardamounts[i]
    for j in range(1, matches + 1):
        cardamounts[i + j] += amount
    

sum = 0
for card in cardamounts:
    sum += card
print(sum)