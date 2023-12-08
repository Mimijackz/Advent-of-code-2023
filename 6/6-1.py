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

times = lines[0][len("Time: "):]
times = times.split(" ")
while("" in times):
    times.remove("")

distances = lines[1][len("Distance: "):]
distances = distances.split(" ")
while("" in distances):
    distances.remove("")

print(times)
print(distances)

product = 1

for i in range(len(times)):
    wins = GetTotalWinPossibilities(int(times[i]), int(distances[i]))
    product *= wins
    print(wins)
print(product)
