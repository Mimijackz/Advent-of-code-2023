from collections import Counter

def CheckFiveOfAKind(freq):
    return freq[0] == 5
def CheckFourOfAKind(freq):
    return freq[0] == 4
def CheckFullHouse(freq):
    return freq[0] == 3 and freq[1] == 2
def CheckThreeOfAKind(freq):
    return freq[0] == 3
def CheckTwoPair(freq):
    return freq[0] == 2 and freq[1] == 2
def CheckOnePair(freq):
    return freq[0] == 2
def CheckHighCard(freq):
    return True


def GetHandType(cards):
    counter = Counter([*cards])
    common = counter.most_common()

    frequencies = [0] * 5
    offset = 0
    for i in range(len(common)):
        if (common[i][0] == "J"):
            jokervalue = common[i][1]
            offset -= 1
            frequencies[0] += jokervalue
        else:
            frequencies[i + offset] += common[i][1]
    print(frequencies)
    print(common)

    handtypes = [CheckHighCard,CheckOnePair,CheckTwoPair,CheckThreeOfAKind,CheckFullHouse,CheckFourOfAKind,CheckFiveOfAKind]

    for i in range(len(handtypes) - 1, -1, -1):
        if handtypes[i](frequencies):
            return i
    return -1

def CardsToNumber(cards):
    key = "J23456789TQKA"
    translator = {}
    for i in range(len(key)):
        translator[key[i]] = i
    reversecards = cards[::-1]
    base = len(key)
    value = 0
    for i in range(len(reversecards)):
        value += pow(base, i + 1) * translator[reversecards[i]]
    return value


f = open("7/input.txt", "r")

lines = f.readlines()

types = [[],[],[],[],[],[],[]]

for hand in lines:
    split = hand.split(" ")
    cards = split[0]
    bid = int(split[1])
    handtype = GetHandType(cards)
    number = CardsToNumber(cards)
    types[handtype].append([cards, bid, number])

for type in types:
    type.sort(key=lambda card : card[2])

cards = []
winnings = []
for type in types:
    for card in type:
        cards.append(card)
        winnings.append(len(cards) * card[1])


print(sum(winnings))