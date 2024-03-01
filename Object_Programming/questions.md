# Découverte de la Programmation Orientée Objet en Python

> [!WARNING]
> Certaines parties du programme ne figurent pas dans ce document texte, il peut être nécessaire d'aller dans les fichiers .py qui sont disponible dans ce dépos Github, en cas de besoin lisez README.md.

## Question 2
Les propriétés de la classe animal sont `sePresenter`, `dormir` `manger` et `setEspece`.

Les méthodes de la classe animalerie sont `get`, `getall`, `arriver`, `presenter`, `count` et `partir`.

## Question 4
Non, il n'existe plus car il est retiré de la ménagère à la ligne 18. Si j'essaye de le présenter une erreur s'affiche.

## Question 5
Oui, il est possible de modifier l'espèce en utilisant `Animal.setEspece(tortue, "nouvelle_espèce")` après l'avoir ajouté au zoo, avant de l'afficher pour que la bonne espèce s'affiche dans la console.

## Question 6
Non, il n'est pas possible d'apporter des modifications car le module `animalerieclass` ne contient pas de fonction pour apporter des modifications.

## Question 7
Saucisse fait 10cm, mais initiallement elle a été définie à 9cm à la ligne 5.
Comme conclusion je dirais que le module chienclass modifie la taille de l'élément comme le confirme la ligne 23, ou si la taille est en dessous de 10 elle est définie à 10.

## Question 8
- Oui, on peut modifier la race du chien après l'avoir crée comme le permet son module `chienclass` avec la méthode `setTaille`.
- Non pas avec n'importe quel valeur, au minimum 10 car une condition modifie la valeur pour l'obligée à être au dessus de 10.
- J'ai pu tester avec `ouaf.setTaille(5)` et `ouaf.sePresenter()` pour afficher.

Voici le résultat :
```
Je me presente :  Chien   Chien
Comme je suis CHIEN, je montre que je peux etre mechant
Attention je suis un  ahouu  et je mesure  14  cms
```
Après l'éxécution de `ouaf.setTaille(5)`
```
Je me presente :  Chien   Chien
Comme je suis CHIEN, je montre que je peux etre mechant
Attention je suis un  ahouu  et je mesure  10  cms
```

## Question 9
Non, il n'est pas possible de changer la race d'un chien car le module ne le supporte pas.

## Question 10
Non ce n'est pas possible car la propriété n'existe pas dans le module en question. Il n'est donc pas possible de récuperer les noms.

## Question 11
Le nom du chien est attribué lors de l'initialisation de la classe Chien. Dans le constructeur de la classe Chien, le nom est passé en paramètre `sonNom`, puis attribué à l'attribut `_nom` de la classe parente `Animal` avec la ligne suivante :
```python
Animal.__init__(self, sonNom, "Chien")
```

## Question 12
Oui il est totalement possible de faire dormir un chien, le faire manger, le faire parler à la place d'aboyer comme le montre l'exemple suivant :
```python
# J'initialise le chien
ouaf = Chien("méchant","blanc","ahouu",14)
leChenil.arriver(ouaf)
# Les actions demandées
ouaf.dormir()
ouaf.manger()
ouaf.parler("UwU")
```
Console :
```
     Zzz Zzz Zzz.... ( méchant  s'est endormi(e))
     J ai si faim... Donne-moi un biscuit !
UwU  !! UwU  !! UwU  !! UwU  !!
```

## Question 13
Oui ils en ont une. L'espèce des chiens est indiqué dans le dernier string lors de leurs ajouts.
```python
saucisse = Chien("Saucisse","roux","teckel",9)
```
Ici la race est `teckel`.

## Question 14
- [x] Je l'ai nommée "spa" et ajouter `merlin`, `louna`, `kosco` et `gulli`.
Les modules sont compatibles entre eux, quand j'éxécute le programme :
```
*****  PRESENTATION DE LA MENAGERIE  *****
Je me presente :  Merlin   chat
Je me presente :  Louna   Chat
Je me presente :  Chien   Kusco
Comme je suis CHIEN, je montre que je peux etre mechant
Attention je suis un  Chien Bleu  et je mesure  35  cms
Je me presente :  Chien   Gulli
Comme je suis CHIEN, je montre que je peux etre mechant
Attention je suis un  Cocker  et je mesure  20  cms
```
Lorsque les animaux se présentent, tout est normal cependant les animaux ajoutés avec le module Chien ajoutent le texte :
```
Comme je suis CHIEN, je montre que je peux etre mechant
```

## Question 15
J'ai réaliser le module [oiseauclass](./oiseauclass.py) assigné à ce fichier pour le test [PPO3.py](./PPO3.py).

Voici la sortie de la console :
```
*****  PRESENTATION DE LA MENAGERIE  *****
Je me presente :  Pew pew   Wazo
     L'oiseau l'envole vers d'autre cieux !
```

## Question 16 et 17
En cas de besoin, voici le [code source](./PPO3.py).
```
*****  PRESENTATION DE LA MENAGERIE  *****
Je me presente :  Pew pew   Wazo
     L'oiseau s'envole vers d'autre cieux !
La ménagerie ne possède aucun animal !

Arrivée de pewpew et de pawpaw

*****  PRESENTATION DE LA MENAGERIE  *****
Je me presente :  Pew pew   Wazo
Je me presente :  Paw Paw   Wazo

pewpew part et puwpuw arrive

*****  PRESENTATION DE LA MENAGERIE  *****
Je me presente :  Paw Paw   Wazo
Je me presente :  Puw Puw   Wazo
```