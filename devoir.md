# BACCALAURÉAT GÉNÉRAL - NUMÉRIQUE ET SCIENCES INFORMATIQUES

> [!NOTE]  
> Il est conseillé de visionner ce document avec Visual Studio Code ou [via la version en ligne](https://vscode.dev) car il contient des expressions mathématiques mal affiché par GitHub.

## Exercice 1

### Question 1
- Un attribut de la classe `Chemin` est `itineraire`.
- Une méthode de la classe `Chemin` est `remplir_grille`.

### Question 2
- Lorsque l'on exécute `chemin_1 = Chemin("DDBDBBDDDDB")`, la méthode `__init__` (le constructeur) calcule la longueur et la largeur de l'itinéraire.
- La variable a correspond à `chemin_1.largeur` et la variable `b` correspond à `chemin_1.longueur`.
- Pour l'itinéraire `"DDBDBBDDDDB"`, il y a 7 déplacements vers la droite (D) et 4 déplacements vers le bas (B).
- Par conséquent, les valeurs contenues dans les variables sont :
    ```python
    a = 4 #(largeur)
    b = 7 #(longueur)
    ```
### Question 3
Méthode `remplir_grille` :
```python
def remplir_grille(self):
    i, j = 0, 0  # Position initiale
    self.grille[0][0] = 'S'  # Case de départ marquée d'un S
    for direction in self.itineraire:
        if direction == 'D':
            j += 1  # Déplacement vers la droite
        elif direction == 'B':
            i += 1  # Déplacement vers le bas
        self.grille[i][j] = '*'  # Marquer le chemin avec '*'
    self.grille[self.largeur][self.longueur] = 'E'  # Case d'arrivée marquée d'un E
```
### Question 4
```python
def get_dimensions(self):
    return (self.longueur, self.largeur)
```
### Question 5
```python
def tracer_chemin(self):
    self.remplir_grille()  # Remplir la grille avec le chemin
    for ligne in self.grille:
        print(' '.join(ligne))
```
### Question 6
```python
from random import choice

def itineraire_aleatoire(m, n):
    itineraire = ''
    i, j = 0, 0
    while i != m and j != n:
        direction = choice(['D', 'B'])  # Tirer au sort une direction
        itineraire += direction
        if direction == 'D':
            j += 1  # Incrémenter la colonne si déplacement vers la droite
        elif direction == 'B':
            i += 1  # Incrémenter la ligne si déplacement vers le bas

    if i == m:
        itineraire += 'D' * (n - j)  # Compléter avec des 'D' jusqu'à la fin
    if j == n:
        itineraire += 'B' * (m - i)  # Compléter avec des 'B' jusqu'à la fin

    return itineraire
```

## Exercice 2

### Question 1
```bash
ls ./documents
```
### Question 2
Le repertoire `multimédia` va après l'exécution de la commande se trouver dans le **repertoire** `/home/documents`

### Question 3
Le code ne permet pas de modéliser l'arborescence de fichiers représentée par l'arbre car il utilise une structure binaire.

### Question 4
Le programme réalise un parcours en profondeur préfixe :

- Affiche d'abord le nom du nœud courant `(print(self.nom))`.
- Puis elle explore récursivement le sous-arbre gauche.
- Enfin, elle explore récursivement le sous-arbre droit.

### Question 5
```plain
. (home)
multimedia
documents
video
images
cours
administratif
personnel
films
```
### Question 6
```python
class Dossier:
    def __init__(self, nom, liste):
        self.nom = nom
        self.fils = liste  # liste d'objets de la classe Dossier

    def est_vide(self):
        return len(self.fils) == 0
```

### Question 7
```python
# Instancier les sous-dossiers
var_films = Dossier("films", [])
var_video = Dossier("video", [var_films])
var_images = Dossier("images", [])

# Instancier le dossier multimedia avec ses sous-dossiers
var_multimedia = Dossier("multimedia", [var_video, var_images])
```
### Question 8
```python
def parcours(self):
    print(self.nom)
    for f in self.fils:
        f.parcours()
```
### Question 9
La méthode `parcours` termine toujours sur une arborescence de fichiers parce qu'elle suit un processus de récursion finie. À chaque appel récursif, la méthode `parcours` est invoquée sur un sous-dossier de la liste `fils`. Comme la liste `fils` est finie (même si elle est vide), la récursion s'arrête dès qu'il n'y a plus de sous-dossiers à parcourir. De plus, il n'y a pas de condition de récursion infinie car chaque appel traite un sous-ensemble strictement plus petit que le précédent.

### Question 10
```python
def parcours(self):
    for f in self.fils:
        f.parcours()
    print(self.nom)
```
### Question 11
La méthode parcours de la classe Dossier affiche les noms des dossiers en suivant un ordre spécifique (préfixe ou suffixe), et elle explore récursivement tous les sous-dossiers.

La commande UNIX ls, en revanche, liste uniquement le contenu immédiat d'un répertoire donné, sans explorer récursivement les sous-répertoires (à moins que l'option -r ne soit utilisée).

### Question 12
```python
def mkdir(self, nom_dossier):
    nouveau_dossier = Dossier(nom_dossier, [])
    self.fils.append(nouveau_dossier)
```
### Question 13
```python
def contient(self, nom_dossier):
    if self.nom == nom_dossier:
        return True
    for f in self.fils:
        if f.contient(nom_dossier):
            return True
    return False
```
### Question 14
Pour déterminer le dossier parent d'un dossier donné dans une arborescence, on peut :

- Parcourir l'arborescence de manière récursive.
- Pour chaque dossier, vérifier si l'un des sous-dossiers dans sa liste fils correspond au dossier donné.
- Si c'est le cas, le dossier courant est le parent.
- Si ce n'est pas le cas, continuer la recherche dans les sous-dossiers.

### Question 15
```python
class Dossier:
    def __init__(self, nom, liste, parent=None):
        self.nom = nom
        self.fils = liste  # liste d'objets de la classe Dossier
        self.parent = parent  # référence au dossier parent
        for f in self.fils:
            f.parent = self  # Met à jour le parent de chaque fils
```

## Exercice 3

### Question 1
Équipier : Bit de rang 0 (2^0 = 1)
Chef d’équipe : Bit de rang 1 (2^1 = 2)
Chef d’agrès : Bit de rang 2 (2^2 = 4)
Conducteur : Bit de rang 3 (2^3 = 8)
Le codage décimal 11 s'écrit en binaire comme suit :

$11^{10} = 1011^{2}$
 
En analysant ce codage binaire :

- Le bit de rang 0 est 1 → Équipier
- Le bit de rang 1 est 1 → Chef d’équipe
- Le bit de rang 2 est 0 → Pas de qualification de Chef d’agrès
- Le bit de rang 3 est 1 → Conducteur

    Ainsi, la qualification 11 correspond à un pompier qui est équipier, chef d'équipe, et conducteur, mais pas chef d'agrès. Cela correspond à la description d'un chef d'équipe conducteur.

### Question 2
Pour trouver le codage décimal de la qualification d’un chef d’agrès conducteur, il faut additionner les valeurs binaires correspondantes :

- Équipier : Bit de rang 0 $(2^0 = 1)$
- Chef d’équipe : Bit de rang 1 $(2^1 = 2)$
- Chef d’agrès : Bit de rang 2 $(2^2 = 4)$
- Conducteur : Bit de rang 3 $(2^3 = 8)$

Un chef d’agrès est nécessairement un chef d’équipe et un équipier, donc on a les bits de rangs 0, 1, et 2 qui sont à 1, plus le bit de rang 3 pour la qualification de conducteur :

$1+2+4+8=15$

Donc, la qualification d'un chef d'agrès conducteur est codée par le nombre 15 en décimal.

### Question 3
Un pompier ne peut pas avoir de qualification dont le codage décimal est 4

La valeur décimale 4 correspond au bit de rang 2 $(2^2)$, qui représente la qualification de chef d’agrès. Cependant, un chef d’agrès est nécessairement aussi un chef d’équipe et un équipier. Cela signifie que si un pompier est chef d’agrès, alors les bits de rangs 0 et 1 doivent également être 1. Le codage binaire correspondant serait donc au moins `0111` (en binaire) qui est 7 en décimal. Par conséquent, la valeur décimale 4 (qui en binaire est `0100`) ne peut pas exister, car cela signifierait qu'un pompier est un chef d'agrès sans être équipier ni chef d'équipe.

### Question 4
Un octet comporte 8 bits, et nous utilisons actuellement 4 bits pour coder les aptitudes. Cela laisse 4 bits non utilisés.

Le nombre de nouvelles aptitudes qui peuvent être définies est donc : $2^4=16$

Cependant, chaque nouvelle aptitude prend un bit, donc il est possible de définir jusqu'à 4 nouvelles aptitudes avec les bits restants.

5. Économie mémoire réalisée par le codage sur un entier de 8 bits
Supposons que chaque aptitude soit codée par une chaîne de 10 caractères, où chaque caractère utilise 1 octet (8 bits). Ainsi, chaque aptitude codée de cette manière utiliserait 10 octets.

Si on encode toutes les aptitudes avec un entier de 8 bits, on utilise 1 octet pour coder les 4 aptitudes.

Calcul de l'économie de mémoire :

Codage par chaîne de caractères : 10 octets par aptitude × 4 aptitudes = 40 octets
Codage par un entier de 8 bits : 1 octet
L'économie de mémoire réalisée est donc :

$$
\text{Economie} = \frac{40}{40 - 1} \times 100\% = \frac{39}{40} \times 100\% \approx 97.5\%
$$

L'économie de mémoire réalisée par le codage sur un entier de 8 bits est d'environ 98%.