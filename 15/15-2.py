def Hash(string):
    hash = 0
    for char in string:
        hash += ord(char)
        hash *= 17
        hash %= 256
    return hash

def LocateLens(box, label):
    for i in range(len(box)):
        if box[i][0] == label:
            return i
    return -1

def AddLens(box, label, length):
    index = LocateLens(box, label)
    lens = [label, length]

    newbox = box.copy()
    if index == -1:
        newbox.append(lens)
    else:
        newbox[index] = lens
    
    return newbox

def RemoveLens(box, label):
    index = LocateLens(box, label)

    newbox = box.copy()
    if index != -1:
        del newbox[index]
    
    return newbox

def CountFocusingPower(boxes):
    totalpower = 0
    for i in range(1, len(boxes) + 1):
        for j in range(1, len(boxes[i-1]) + 1):
            currentpower = i * j * boxes[i-1][j-1][1]
            #print(currentpower)
            totalpower += currentpower
    return totalpower

f = open("15/input.txt", "r")

boxes = [[] for i in range(256)]
#print(boxes)

for input in f.read().split(","):
    isremove = "-" in input
    values = input.split("-" if isremove else "=")
    #print(values)
    label = values[0]
    boxindex = Hash(label)

    if isremove:
        boxes[boxindex] = RemoveLens(boxes[boxindex], label)
    else:
        focallength = int(values[1])
        boxes[boxindex] = AddLens(boxes[boxindex], label, focallength)

#print(boxes)
print(CountFocusingPower(boxes))
