def Decalibrate(input):
    numFirst = None
    numLast = None

    for char in input:
        if str.isdigit(char):
            if numFirst == None:
                numFirst = char
            numLast = char

    output = numFirst + numLast
    return output

f = open("1-1/input.txt", "r")

inputs = f.readlines()
sum = 0

for i in range(0, len(inputs)):
    sum += int(Decalibrate(inputs[i]))


print(sum)