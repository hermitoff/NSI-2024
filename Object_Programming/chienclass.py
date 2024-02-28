from animalclass import Animal
# Représente un Chien de race (hérite de la classe Animal)
class Chien(Animal):
        # Constructeur
        # Initialise une nouvelle instance de la classe Chien
        def __init__(self,sonNom, saCouleur, saRace, saTaille):
            Animal.__init__(self,sonNom,"Chien") 
            self.__race = saRace
            self.__taille = saTaille
            self.setTaille(self.__taille)
        
        # Obtient la race du chien
        def getRace(self):
            return self.__race
        
        # Obtient ou modifie la taille du chien
        def getTaille(self):
            return self.__taille
        def setTaille(self,value):
            if(value > 10):
                self.__taille = value
            else:
                self.__taille = 10        
        # Méthodes
        # Fait aboyer le chien (en fonction de sa taille)
        def aboyer(self):
            print(self._nom," aboie : ")
            if(self.__taille > 60):
                self.parler("Grrr")
            else:
                if(self.__taille > 20):
                    self.parler("Wouaf")
                else:
                    self.parler("Kaii")
        # Méthodes
        # Fait se présenter le chien
        def sePresenter(self):
            print("Je me presente : ",self._espece," ",self._nom)
            print("Comme je suis CHIEN, je montre que je peux etre mechant")
            print("Attention je suis un ",self.__race," et je mesure ",self.__taille," cms")
