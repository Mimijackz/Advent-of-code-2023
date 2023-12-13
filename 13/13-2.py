import math

def GetMirrorVertical(lines):
    for i in range(1, len(lines[0])):
        #print(i)
        ispossible = True
        errors = 0
        for line in lines:
            reversedpattern = line[:i][::-1]
            mirrorpattern = line[i:]
            #print(reversedpattern)
            #print(mirrorpattern)
            if len(reversedpattern) < len(mirrorpattern):
                (reversedpattern, mirrorpattern) = (mirrorpattern, reversedpattern)
            currenterrors = CompareStrings(mirrorpattern, reversedpattern)
            if currenterrors == 0:
                ispossible &= True
            else:
                ispossible &= False
                errors += currenterrors
        if errors == 1:
            #print(str(i) + " possible")
            return i
    
    return -1
      
        
def GetMirrorHorizontal(lines):
    for i in range(1, len(lines)):
        #print(i)
        ispossible = True
        errors = 0
        for j in range(len(lines[0])):
            reversedpattern = [line[j] for line in lines[:i]]
            reversedpattern.reverse()
            mirrorpattern = [line[j] for line in lines[i:]]
            #print(reversedpattern)
            #print(mirrorpattern)
            currenterrors = CompareLists(mirrorpattern, reversedpattern)
            if currenterrors == 0:
                ispossible &= True
            else:
                ispossible &= False
                errors += currenterrors
        if errors == 1:
            #print(str(i) + " possible")
            return i
        
    return -1
        
def CompareLists(shortlist, longlist):
    output = 0
    if len(shortlist) > len(longlist):
        (shortlist,longlist) = (longlist,shortlist)
    for i in range(len(shortlist)):
        if shortlist[i] != longlist[i]:
            output += 1
    return output

def CompareStrings(shortstring, longstring):
    output = 0
    for i in range(len(shortstring)):
        if shortstring[i] != longstring[i]:
            output += 1
    return output

f = open("13/input.txt", "r")

input = f.read()

input = input.split("\n\n")

#print(input)

total = 0
for pattern in input:
    lines = pattern.split("\n")
    #print(lines)
    horizontalmirror = GetMirrorHorizontal(lines)
    verticalmirror = GetMirrorVertical(lines)
    #print(horizontalmirror)
    #print(verticalmirror)
    #print("____")

    if horizontalmirror != -1:
        total += 100 * horizontalmirror
    elif verticalmirror != -1:
        total += verticalmirror
    else:
        print(lines)

print(total)