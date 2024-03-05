from lievreClass import Lievre
from lievreTortueClass import LievreTortue
import time
import random

tortue = Lievre()
lievre = LievreTortue(tortue.turtle.position())

#print("Vers quelles coordonnées x aller ?\n")
#cordsx = float(input("> "))
#print("Vers quelles coordonnées y aller ?\n")
#cordsy = float(input("> "))

#print(cordsx, cordsy)


# c)
def turtle_move():
    tortue.aller_vers(random.randint(1,20), random.randint(1,20))
    print("DEBUG", tortue.turtle.pos())

def lievre_move():
    lievre.forward(random.randint(1,5))

#for i in range(random.randint(10,30)):

# Exécuter les deux fonctions pour réplacer les elements sur le GUI
while True:
    turtle_move()
    lievre_move()