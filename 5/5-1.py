def ConvertLocation(location, translator):
    for code in translator:
        if code[1] <= location < code[1] + code[2]:
            return location + code[0] - code[1]
    return location

def GetCategoryNumbers(category, input):
    salt = " map:\n"
    startindex = input.find(category + salt) + len(category + salt)
    numbers = input[startindex:].split("\n")
    if not "" in numbers:
        endindex = -1
    else:
        endindex = numbers.index("")
    numbers = numbers[:endindex]
    for i in range(len(numbers)):
        numbers[i] = list(map(int, numbers[i].split(" ")))

    return numbers



f = open("5/input.txt", "r")

input = f.read()

seeds = list(map(int, input[len("seeds: "):input.find("\n")].split(" ")))
print(seeds)

translators = []

translators.append(GetCategoryNumbers("seed-to-soil", input))
translators.append(GetCategoryNumbers("soil-to-fertilizer", input))
translators.append(GetCategoryNumbers("fertilizer-to-water", input))
translators.append(GetCategoryNumbers("water-to-light", input))
translators.append(GetCategoryNumbers("light-to-temperature", input))
translators.append(GetCategoryNumbers("temperature-to-humidity", input))
translators.append(GetCategoryNumbers("humidity-to-location", input))
print(translators)

seedlocations = []

for seed in seeds:
    currentlocation = seed
    #print("seed " + str(seed) + ":")
    for translator in translators:
        currentlocation = ConvertLocation(currentlocation, translator)
        #print(currentlocation)
    seedlocations.append(currentlocation)
print(seedlocations)

print(min(seedlocations))