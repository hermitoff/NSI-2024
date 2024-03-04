from lievreClass import Lievre
import time

tortue = Lievre()
lievre = Lievre()

print("\n\n------\n\n")

print("Vers quelles coordonnées x aller ?\n")
cordsx = float(input("> "))
print("Vers quelles coordonnées y aller ?\n")
cordsy = float(input("> "))

#print(cordsx, cordsy)

# Utilisez la méthode aller_vers de l'objet Lievre
# Exemple
for i in range(10):
    tortue.aller_vers(cordsx, cordsy)

print("Position de la tortue")
print(tortue.turtle.pos())

# Code pour la seconde tortue qui va la suivre
lievre

# Garder la fenêtre ouverte 5 secondes pour voir le résultat
time.sleep(5)