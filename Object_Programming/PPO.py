#Importation des modules nécessaires
from animalclass import Animal
from animalerieclass import Menagerie



#Création d'une ménagerie
zoo = Menagerie()
zoo.presenter()
#Création de 3 animaux
nemo = Animal("Nemo","Poisson")
felix = Animal("Felix","Chat")
pistache= Animal("Pistache","Perruche")

tortue = Animal("Tortue","espece")
#Enregistrement des animaux qui arrivent dans la ménagerie
zoo.arriver(nemo)
zoo.arriver(felix)
zoo.arriver(pistache)

zoo.arriver(tortue)

#Présentation de la ménagerie ainsi constituée
print("Le zoo comporte ", len(zoo.animaux)," animaux")
zoo.presenter()
zoo.partir(felix)

# Modification de l'espèce (question 5)
Animal.setEspece(tortue, "nouvelle_espèce")

#Présentation de la ménagerie ainsi constituée
print("Le zoo comporte ", len(zoo.animaux)," animaux")
zoo.presenter()
