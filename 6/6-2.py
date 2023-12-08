import math

def GetTotalWinPossibilities(time, distance):
    # the fact that i am actually using this...
    d = pow(time,2)+(4*-1*distance)
    if d < 0:
        return 0
    droot = math.sqrt(d)
    r1 = (time+droot)/2
    r2 = (time-droot)/2

    roundedr1 = math.ceil(r1) - 1
    roundedr2 = math.floor(r2) + 1
    diff = abs(roundedr1-roundedr2)
    return math.floor(diff) + 1

f = open("6/input.txt", "r")

lines = f.read().splitlines()

time = lines[0][len("Time: "):]
time = time.replace(" ", "")

distance = lines[1][len("Distance: "):]
distance = distance.replace(" ", "")

print(time)
print(distance)

wins = GetTotalWinPossibilities(int(time), int(distance))

print(wins)
