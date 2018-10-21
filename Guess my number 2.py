#Biésów Smãtk
#Computer guesses player's number from 0 to 100.

import random

print("Witôj w jigrze \"Jakô to lëczba?\"!")
print("Wëbiérze dowòlną lëczbã òd 0 do 100.")
print("Kòmpùter mdze miôł starã jã wëzdgadnąc jak nôrëchli.")
print("Mô leno 10 próbów.")
print("Żlë lëczba pòdónô bez kòmpùter je za môłô, wpisze \"too low\"")
print("Żlë lëczba pòdónô bez kòmpùter je za wiôlgô, wpisze \"too high\"")
print("\nPòdôj swojã lëczbã") #instructions for player

a = 1
b = 100 #range of values
chosen = int(input()) #taking number from player
choose = ""
tries = 1
number = random.randint(a,b) #first computer's try
print()
print(number)
while not number == chosen: #next tries
    choose = input()
    if choose == ("too low"):
        a = number + 1
    elif choose == ("too high"):
        b = number - 1
    else:
        print("pòwtórzë wpis")
        continue
    tries += 1
    if b < a: #condition of restart if player tries to cheat
        print("Jes próbòwôł òcëganic kòmpùter, zaczinô òn òd zôczątkù.\n")
        a = 1
        b = 100
        tries = 1
    number = random.randint(a,b)
    print(number)
    if tries >= 10: #failure's condition
        break
if tries < 10:
    print("Kòmpùter wëzdgôdnął Twojã lëczbã w", tries,"pòdeńscach") #computer wins
else:
    print("Kòmpùter nie wëzgôdł w 10 próbach. Jes dobëł") #player wins
input("\nWcëskôj Enter, żebë skùńczëc.")
