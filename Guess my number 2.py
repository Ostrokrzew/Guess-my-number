# Biésów Smãtk
# kòmpùter zgadiwô Twojã lëczbã, wëbróną z zôkresë òd 0 do 100.

import random #jimpòrt mòdułë

print("Witôj w jigrze \"Jakô to lëczba?\"!")
print("Wëbiérze dowòlną lëczbã òd 0 do 100.")
print("Kòmpùter mdze miôł starã jã wëzdgadnąc jak nôrëchli.")
print("Mô leno 10 próbów.")
print("Żlë lëczba pòdónô bez kòmpùter je za môłô, wpisze \"too low\"")
print("Żlë lëczba pòdónô bez kòmpùter je za wiôlgô, wpisze \"too high\"")
print("\nPòdôj swojã lëczbã")
# nôdpisë dlô gracza
a = 1
b = 100 #zôkres wëzgôdczi
chosen = int(input()) # pòbranié lëczbë òd gracza
choose = ""
tries = 1
number = random.randint(a,b) #pierszi strzél kòmpùtera
print()
print(number)
while not number == chosen: #pòwtórziwanié strzélów bez kòmpùter
    choose = input()
    if choose == ("too low"):
        a = number + 1
    elif choose == ("too high"):
        b = number - 1
    else:
        print("pòwtórzë wpis")
        continue
    tries += 1
    if b < a: #warënk pòwtórzeniô, jeżlë chcesz oszëkac
        print("Jes próbòwôł òcëganic kòmpùter, zaczinô òn òd zôczątkù.\n")
        a = 1
        b = 100
        tries = 1
    number = random.randint(a,b) 
    print(number)
    if tries >= 10: #warënk przegraniô
        break
if tries < 10:
    print("Kòmpùter wëzdgôdnął Twojã lëczbã w", tries,"pòdeńscach")
else:
    print("Kòmpùter nie wëzgôdł w 10 próbach. Jes dobëł")
input("\nWcëskôj Enter, żebë skùńczëc.")
