# II Index alphabétique

def ajoute(mot, index):
    initiale = mot[0]
    if initiale not in index:
        index[initiale] = [mot]
    else:
        index[initiale].append(mot)

def retire(mot, index):
    initiale = mot[0]
    if initiale in index:
        index[initiale].remove(mot)
        if len(index[initiale]) == 0:
            del index[initiale]

def build(liste_mots):
    index = {}
    for mot in liste_mots:
        ajoute(mot, index)
    return index

liste_mots = ["arbre", "androïde", "martien", "concept", "bleu", "but", "abri", "bateau", "art"]

index = build(liste_mots)
print("Index initial:", index)

ajoute("uwu", index)
retire("androïde", index)
print("Index après retrait de 'androïde':", index)
