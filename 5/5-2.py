def ConvertLocation(location, translator):
    for code in translator:
        if code[1] <= location < code[1] + code[2]:
            return location + code[0] - code[1]
    return location

def ReverseLocation(destination, translator):
    for code in translator:
        if code[0] <= destination < code[0] + code[2]:
            return destination + code[1] - code[0]
    return destination

def ConvertLocationRange(locationrange, numbers):
    output = [[],[]]

    locstart = locationrange[0]
    locoffset = len(locationrange)
    locend = locstart + locoffset

    numstart = numbers[1]
    numoffset = numbers[2]
    numend = numstart + numoffset

    start = max(numstart, locstart)
    end = min(numend, locend)
    #print([numstart, numoffset, numend])
    if start < end:
        if locstart < start:
            output[0].append(range(locstart, start))
        if start < end:
            offset = numbers[0] - numbers[1]
            output[1].append(range(start + offset, end + offset))
        if end < locend:
            output[0].append(range(end, locend))
    else:
        output[0].append(range(locstart,locend))
    #print(output)
    return output

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

seedrange = list(map(int, input[len("seeds: "):input.find("\n")].split(" ")))

seeds = []

for i in range(0, len(seedrange), 2):
    start = seedrange[i]
    number = seedrange[i + 1]
    seeds.append(range(start, start + number))

translators = []

translators.append(GetCategoryNumbers("seed-to-soil", input))
translators.append(GetCategoryNumbers("soil-to-fertilizer", input))
translators.append(GetCategoryNumbers("fertilizer-to-water", input))
translators.append(GetCategoryNumbers("water-to-light", input))
translators.append(GetCategoryNumbers("light-to-temperature", input))
translators.append(GetCategoryNumbers("temperature-to-humidity", input))
translators.append(GetCategoryNumbers("humidity-to-location", input))
#print(translators)
#translators.reverse()

print(str(seeds) + " seeds")
print(str(translators) + " translators")

currentrange = seeds.copy()


for translator in translators:
    nextrange = []
    for numbers in translator:
        newrange = []
        for seed in currentrange:
            #print(str(seed) + " seed")
            locations = (ConvertLocationRange(seed, numbers))
            print(str(locations) + " location")
            for location in locations[1]:
                nextrange.append(location)
            for location in locations[0]:
                newrange.append(location)
        currentrange = newrange
    for location in newrange:
        nextrange.append(location)

    currentrange = list(dict.fromkeys(nextrange))
    print(str(currentrange) + " ranges")
print("current range:")
print(currentrange)
rangevalues = []

for range in currentrange:
    rangevalues.append(range[0])
print(rangevalues)
print(min(rangevalues))
