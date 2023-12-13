from itertools import combinations

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

def CreatePossibilities(n_empty, groups, ones):
        res_opts = []
        print(n_empty)
        print(groups)
        print(ones)
        comb = combinations(range(groups+n_empty), groups)
        print(comb)
        print(list(comb))
        
        for p in combinations(range(groups+n_empty), groups):
            selected = [-1]*(groups+n_empty)
            ones_idx = 0
            for val in p:
                selected[val] = ones_idx
                ones_idx += 1
            res_opt = [ones[val]+[-1] if val > -1 else [-1] for val in selected]
            res_opt = [item for sublist in res_opt for item in sublist][:-1]
            print(res_opt)
            res_opts.append(res_opt)
        return res_opts

def RemovePossibilities(possibilities, string):
    invalidIndexes = []
    for i in range(len(possibilities)):
        isValid = True
        for j in range(len(possibilities[i])):
            char = string[j]
            number = possibilities[i][j]
            if char == "?":
                continue
            if (number == -1 and char != ".") or (number == 1 and char != "#"):
                isValid = False
        if not isValid:
            invalidIndexes.append(i)
    print(invalidIndexes)
    return len(possibilities) - len(invalidIndexes)



f = open("12/input.txt","r")

lines = f.read().splitlines()
print(lines)

total = 0
currentline = 0
for line in lines:
    game = line.split(" ")
    game[1] = list(map(int, game[1].split(",")))
    #print(game)
    order = game[1]
    order = order * 5

    string = (game[0] + "?") * 5

    print(order)
    print(string)

    #print(secrets)

    #possiblearrangements = list(combinations(range(len(order) + (len(order) - 1)), len(order)))
    ones = [[1]*x for x in order]
    possiblearrangements = CreatePossibilities(len(string) - sum(order) - (len(order) - 1), len(order), ones)
    
    currentline += 1
    print(str(currentline) + ": " + str(possiblearrangements))
    total += RemovePossibilities(possiblearrangements, string)
    #sum += len(possiblearrangements)

print("sum " + str(total))
