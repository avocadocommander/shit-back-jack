import random
import sys


class Card:
    def __init__(self, id, suite):
        self.id = id
        self.suite = suite

    def printMe(self):
        print(str(self.id) + " " + self.suite)

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


runs = 52
min = 0
max = 13

print("initalizing stuff")

#suite = [FAIL+"\u2666"+ENDC, FAIL+"\u2665"+ENDC, "\u2663", "\u2660"]
suite = ["\u2666", "\u2665", "\u2663", "\u2660"]

print("For loop about to start")

deck = []
x=0
for i in range(0 , 12 + 1):
    for s in range(0, 3 + 1):
        x = x + 1
        newCard = Card(i+1, suite[s])
        deck.append(newCard)


print("\n\n-------------- CARD AT DECK INDEX ------------------")
deck[random.randrange(0, 52)].printMe()
deck[random.randrange(0, 52)].printMe()
print("----------------------------------\n\n")

print("For loop end")
