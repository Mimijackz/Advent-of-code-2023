def GetGearRatio(line, index, input):
    amount = 0
    ratio = 1
    input = input.copy()
    for x in range(-1, 2):
        for y in range(-1, 2):
            char = input[max(min(line + y, len(input) - 1), 0)][max(min(index + x, len(input[line + y]) - 1), 0)]

            if (str.isdigit(char)):
                current = index + x
                start = current
                end = current
                while (0 <= current < len(input[line + y]) and str.isdigit(input[line + y][current])):
                    start = current
                    current -= 1
                current = index + x
                while (0 <= current < len(input[line + y]) and str.isdigit(input[line + y][current])):
                    end = current
                    current += 1
                
                ratio *= int(input[line+y][start:end + 1])
                amount += 1
                input[line + y] = input[line + y][:start] + ("." * (end - start + 1)) + input[line + y][end + 1:]
    if (amount != 2):
        ratio = 0
    return ratio


f = open("3/input.txt", "r")

input = f.read().splitlines()
#print(input)
sum = 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if (input[i][j] == "*"):
            sum += GetGearRatio(i, j, input)

output = ""
for line in input:
    output += line + "\n"
print(output)
print(sum)
