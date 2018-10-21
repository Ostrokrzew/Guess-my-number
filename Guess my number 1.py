#Biésów Smãtk
#Computer choose random number from 1 to 100.
#Player tries to guess the number and computer informs him, is his number too low, too high or good.

import random

print("\tWitój w jigrze \"Jakô to lëczba\"!")
print("\nMóm na mëszlë pewną lëczbã z zôkresë òd 1 do 100.")
print("Spróbùje jã wëzgôdnąc w jak nômiészi lëczbie próbów.\n")
print("Môsz jejich blós 10!\n")

#setting start value
number = random.randint(1, 100)
guess = int(input("Ta lëczba to: "))
tries = 1

#guessing loop
while guess != number:
    if guess > number:
        print("Za wiôlgô...")
    else:
        print("Za môłô...")

    guess = int(input("Ta lëczba to: "))
    tries += 1
    if tries >= 10: #condition of failure
        break
if tries < 10:
    print("Jes wëzgôdł! Ta lëczba to", number) #win
    print("Do dobëcégò jes brëkòwôł blós", tries, "próbów!\n")#number of tries
else:
    print("Môsz przegróné, nie wëzgôdł jes w 10 próbach.") #failure

input("\nWcëskôj Enter, żebë skùńczëc.")
