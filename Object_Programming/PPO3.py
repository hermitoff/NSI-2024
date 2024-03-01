# Question 15

from oiseauclass import Oiseau
from animalerieclass import Menagerie

hell = Menagerie()

pewpew = Oiseau("Pew pew", "Wazo", "Russie")

hell.arriver(pewpew)

# Afficher la ménagerie
hell.presenter()

# Action demandée
pewpew.voler()

# Question 16 et 17

# Définir les oiseaux
# Pewpew est déjà défini(e)
pawpaw = Oiseau("Paw Paw", "Wazo", "Ukraine")
puwpuw = Oiseau("Puw Puw", "Wazo", "France")


# Petite fonction pour ne pas répéter le code à chaque fois
def presenter_menagerie():
     voliere.presenter()

voliere = Menagerie()

presenter_menagerie()

# Faire arriver les oiseaux
print("\nArrivée de pewpew et de pawpaw\n")
voliere.arriver(pewpew)
voliere.arriver(pawpaw)

presenter_menagerie()

print("\npewpew part et puwpuw arrive\n")
voliere.partir(pewpew)
voliere.arriver(puwpuw)

presenter_menagerie()