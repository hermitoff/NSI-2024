# Importer les modules
from animalclass import Animal
from animalerieclass import Menagerie
from chienclass import Chien


# Définir la ménagerie
spa = Menagerie()

# Ajouter les animaux
merlin = Animal("Merlin", "chat")
louna = Animal("Louna", "Chat")

# perdita = Chien("Perdita","pie","dalmatien",50)
kusco = Chien("Kusco", "bleu", "Chien Bleu", 35)
gulli = Chien("Gulli", "Noir", "Cocker", 20)


# Les faire arriver pour pouvoir travailler avec
spa.arriver(merlin)
spa.arriver(louna)

spa.arriver(kusco)
spa.arriver(gulli)

# Présenter la ménagerie
spa.presenter()
