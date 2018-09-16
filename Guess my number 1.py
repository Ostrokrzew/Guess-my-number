# Biésów Smãtk
# Kòmpùtr wëbiérô losowò lëczbã z zôkresë òd 1 do 100.
# Gracz próbuje jã wëzgôdnąc, a kòmpùter gò jinformùje, czë pòdónô bez niegò lëczba je za wiôlgô, za môłô abò richtich.

import random #jimpòrt mòdułë

print("\tWitój w jigrze \"Jakô to lëczba\"!")
print("\nMóm na mëszlë pewną lëczbã z zôkresë òd 1 do 100.")
print("Spróbùje jã wëzgôdnąc w jak nômiészi lëczbie próbów.\n")
print("Môsz jejich blós 10!\n")

# ùstawi zôczątkòwé wôrtnotë
number = random.randint(1, 100)
guess = int(input("Ta lëczba to: "))
tries = 1

# pãtla zgadiwaniô
while guess != number:
    if guess > number:
        print("Za wiôlgô...")
    else:
        print("Za môłô...")
            
    guess = int(input("Ta lëczba to: "))
    tries += 1
    if tries >= 10: #warënk przegraniô
        break
if tries < 10:
    print("Jes wëzgôdł! Ta lëczba to", number)
    print("Do dobëcé jes brëkòwôł blós", tries, "próbów!\n")
else:
    print("Môsz przegróné, nie wëzgôdł jes w 10 próbach.")    
  
input("\nWcëskô Enter, żebë skùńczëc.")
