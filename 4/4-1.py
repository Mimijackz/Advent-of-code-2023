def StringToIntArray(stringarray):
    intarray = []
    for i in range(len(stringarray)):
        if (str.isdigit(stringarray[i])):
            intarray.append(int(stringarray[i]))
    return intarray

def GetCardPoints(winners, scratches):
    numbers = []
    for winner in winners:
        for scratch in scratches:
            if winner is scratch:
                numbers.append(winner)
                print(winner)
    numbers = list(dict.fromkeys(numbers))
    points = 0
    if (len(numbers) > 0):
        points = pow(2, len(numbers) - 1)
    return points
    


f = open("4/input.txt", "r")

lines = f.read().splitlines()

sum = 0
for card in lines:
    card = card.split(": ")
    numbers = card[1].split(" | ")
    print(numbers)
    winners = StringToIntArray(numbers[0].split(" "))
    scratches = StringToIntArray(numbers[1].split(" "))
    print(winners)
    print(scratches)

    points = GetCardPoints(winners, scratches)
    sum += points
    print(points)
print(sum)