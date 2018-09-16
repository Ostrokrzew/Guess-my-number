# Komputr zgadiwô Twoja lëczba

import random #jimport biblioteczi

print("Wëbiérze dowolną lëczba od 0 do 100.")
print("Komputr mdze miôł stara ja wëzdgadnąc jak nôrëchli.")
print("Żlë lëczba podónô bez komputr je za małô, wpisze \"too low\"")
print("Żlë lëczba podónô bez komputr je za wiôlgô, wpisze \"too high\"")
print("\nPodô swoją lëczba")
# nôdpisë dlô gracza
a = 1
b = 100 #zôkres wëzgôdczi
chosen = int(input()) # pobranié lëczbë od gracza
choose = ""
tries = 1
number = random.randint(a,b) #pierszi strzél komputra
print()
print(number)
while not number == chosen: #powtórziwanié strzélów bez komputr
    choose = input()
    if choose == ("too low"):
        a = number + 1
    elif choose == ("too high"):
        b = number - 1
    else:
        print("powtórzë wpis")
        continue
    tries += 1
    if b < a: #warënk powtórzeniô, jeżlë chcesz oszëkac
        print("Jes próbowôł ocëganic komputr, tej on zaczinô od zôczątku.\n")
        a = 1
        b = 100
        tries = 1
    number = random.randint(a,b) 
    print(number)

print("Komputr wëzdgôdnął Twoja lëczba w", tries,"podeńscach")
input("\nWcëskô Enter, żebë skuńczëc.")
