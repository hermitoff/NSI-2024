# Créé par Administrateur, le 13/07/2022 en Python 3.7
class Animal:
    def __init__(self,unNom,uneEspece):
        self._nom=unNom
        self._espece=uneEspece
    def getNom(self):
        return self._nom
    def setNom(self,unNom):
        self.__nom=unNom
    def getEspece(self):
        return self._espece
    def setEspece(self,uneEspece):
        self._espece=uneEspece
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