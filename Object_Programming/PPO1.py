from animalerieclass import Menagerie
from chienclass import Chien

#les chiens prennent vie
medor = Chien("Médor","noir","batard",19)
saucisse = Chien("Saucisse","roux","teckel",9)
pongo = Chien("Pongo","pie","dalmatien",70)
perdita = Chien("Perdita","pie","dalmatien",50)

#Les chiens aboient quand
print(" La caravane passe ..")
medor.aboyer()
saucisse.aboyer()
print("Quelle est la taille de Saucisse ? ",saucisse.getTaille()," cm")
pongo.aboyer()
perdita.aboyer()

#Les chiens sont en pension au chenil
leChenil = Menagerie()
leChenil.arriver(medor)
leChenil.arriver(saucisse)
leChenil.arriver(pongo)
leChenil.arriver(perdita)

#Le chenil présente ses pensionnaires
leChenil.presenter()