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

def ConvertToDigits(string):
    keys = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    convertedString = string

    for i in range(0, len(string)):
        for j in range(0, len(keys)):
            if (string.startswith(keys[j], i)):
                convertedString = convertedString[:i] + string[i:].replace(keys[j], values[j], 1)
    return convertedString

f = open("1/input.txt", "r")
#f = open("1-1/test.txt", "r")

inputs = f.readlines()
sum = 0

for i in range(0, len(inputs)):
    input = ConvertToDigits(inputs[i].lower())
    sum += int(Decalibrate(input))

print(sum)