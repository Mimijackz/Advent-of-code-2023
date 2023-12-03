def IsValid(line, index, input):
    valid = False
    for x in range(-1, 2):
        for y in range(-1, 2):
            char = input[max(min(line + y, len(input) - 1), 0)][max(min(index + x, len(input[line]) - 1), 0)]
            if ((not str.isdigit(char)) and (char != ".")):
                valid = True
    return valid



f = open("3/input.txt", "r")

input = f.read().splitlines()
validinput = input.copy()
#print(input)
sum = 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if (str.isdigit(input[i][j])):
            valid = False
            end = j
            while (end < len(input[i]) and str.isdigit(input[i][end])):
                if IsValid(i, end, input):
                    valid = True
                    #print(input[i][end])
                end += 1
            
            if not valid:
                validinput[i] = validinput[i][:j] + ("." * (end - j)) + validinput[i][end:]
            else:
                sum += int(validinput[i][j:end])

            input[i] = input[i][:j] + ("." * (end - j)) + input[i][end:]
            #print(input)

        #if (str.isdigit(input[i][j]) and not IsValid(i, j, input)):
        #    input[i] = input[i][:j] + "." + input[i][j + 1:]

output = ""
for line in validinput:
    output += line + "\n"
print(output)
print(sum)
