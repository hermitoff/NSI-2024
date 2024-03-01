# Question 15

class Oiseau:
    def __init__(self,unNom,uneEspece,unPays):
        self._nom=unNom
        self._espece=uneEspece
        self._pays=unPays
    def getNom(self):
        return self._nom
    def setNom(self,unNom):
        self.__nom=unNom
    def getEspece(self):
        return self._espece
    def setEspece(self,uneEspece):
        self._espece=uneEspece
    def getPays(self,unPays):
        return self._pays
    def sePresenter(self):
        print("Je me presente : ",self._nom," ",self._espece)
        if(self._nom == "Maurice"):
            print("... Il parait que je pousse le bouchon un peu trop loin ...!!!")
    def dormir(self):
        print("     Zzz Zzz Zzz.... (",self._nom," s'est endormi(e))")
    def parler(self,leCri):
        for i in range(4):
           print(leCri," !! ",end='')
    def manger(self):
        print("     J ai si faim... Donne-moi un biscuit !")
    def voler(self):
        print("     L'oiseau s'envole vers d'autre cieux !")