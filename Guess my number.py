# Kòmpùtr zgadiwô Twojã lëczbã

import random #jimpòrt biblioteczi

print("Witôj w jigrze /"Jakô to lëczba?/"")
print("Wëbiérze dowòlną lëczbã òd 0 do 100.")
print("Kòmpùtr mdze miôł starã jã wëzdgadnąc jak nôrëchli.")
print("Żlë lëczba pòdónô bez kòmpùtr je za môłô, wpisze \"too low\"")
print("Żlë lëczba pòdónô bez kòmpùtr je za wiôlgô, wpisze \"too high\"")
print("\nPòdô swojã lëczbã")
# nôdpisë dlô gracza
a = 1
b = 100 #zôkres wëzgôdczi
chosen = int(input()) # pòbranié lëczbë òd gracza
choose = ""
tries = 1
number = random.randint(a,b) #pierszi strzél kòmpùtra
print()
print(number)
while not number == chosen: #pòwtórziwanié strzélów bez kòmpùtr
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
        print("Jes próbòwôł òcëganic kòmpùtr, zaczinô òd zôczątkù.\n")
        a = 1
        b = 100
        tries = 1
    number = random.randint(a,b) 
    print(number)

print("Kòmpùtr wëzdgôdnął Twojã lëczbã w", tries,"pòdeńscach")
input("\nWcëskô Enter, żebë skùńczëc.")
