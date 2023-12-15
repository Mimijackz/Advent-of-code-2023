def Hash(string):
    hash = 0
    for char in string:
        hash += ord(char)
        hash *= 17
        hash %= 256
    return hash

f = open("15/input.txt", "r")

total = 0
for input in f.read().split(","):
    hashedinput = Hash(input)
    total += hashedinput
print(total)

