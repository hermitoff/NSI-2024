# Represente une menagerie, laquelle peut "heberger" un certain nombre d'animaux
class Menagerie:
       def __init__(self):
               self.animaux=[]
       def get(self,indice):
              if(indice in range(self.count())):
                     return self.animaux[indice]
              else:
                     return False
       def getall(self):
              return self.animaux   
       def arriver(self,animal):
              self.animaux.append(animal)
       def presenter(self):
              if(self.count()==0):
                     print("La ménagerie ne possède aucun animal !")
              else:
                     print("*****  PRESENTATION DE LA MENAGERIE  *****")
                     for curranimal in self.animaux:
                            curranimal.sePresenter()
       def count(self):
              return len(self.animaux)
       def partir(self,animal):
              self.animaux.remove(animal)
