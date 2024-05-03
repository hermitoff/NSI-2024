# Modèle relationnel : Exercice

## Exercice 1

### Q1
La relation voiture contient `6` attributs.

### Q2
Son nombre d'enregistrement est à `3`.

### Q3
Le domaine de l'attribut est une clé étrangère, il faut que chaque identifiant soit unique afin d'éviter les conflits.

### Q4
C'est une clé primaire

### Q5
La clé primaire de la relation agence est `id_agence`.

### Q6
La clé primaire est `id_voiture`.

### Q7
La clé étrangère est `id_agence`.

### Q8
Le schéma relationnel de la relation `Voiture` est une relation qui contient un ID unique, la `marque`, `modèle`, `couleur` (protégé par un domaine pour ne pas pouvoir mettre n'importe quoi), un `kilométrage` (ne peut pas être négatif) et la clé étrangère id_agence.

## Exercice 2

### Q1
Ce schéma relationnel définit quatre tables : `Equipe`, `Coureur`, `Etape`, et `Temps`. Chaque table a ses propres colonnes et types de données appropriés. Les relations entre les tables sont établies par l'utilisation de clés étrangères dans les tables `Coureur` et `Temps`, qui référencent les tables `Equipe` et `Etape`.


### Q2
Le temps réalisé par `Guillaume MARTIN` (121) sur l'étape `Sisteron` (4) est de `04:07:47`.

### Q3
A `Privas` (5), `ROGLIC Primoz` est arrivé en même temps que l'autre coureur

### Q4


## Exercice 3
Dans la table `Hotel`, `Chambre` le champ `nom_hotel` sont en doublon et il n'y a pas de clé primaire ce qui rendra difficile les mises à jour

## Exercice 4

### Q1
Non, il aurait fallu associer a chaque sandwich un identifiant unique et faire de ce champ une clé primaire, pour en stocker plusieurs dans le champ `nom_sandwich` de la table `Commandes` car dans notre cas il ne peut avoir qu'un type de sandwich par commande.

### Q2

Les clés primaires des deux tables sont :
- Pour la table `Client` la clé primaire est `numero_client`
- Pour la table `Sandwich` la clé primaire est `nom_sandwich`

### Q3

Non, aucun attribut pourrait servir de clé primaire, car une clé primaire doit être unique est c'est le cas d'aucun champ non clé étrangère.

### Q4

Non il y'a certains problème, comme dit dans la question 1, il faudrait que la table `Sandwich` contienne un ID unique associé au nom d'un sandwich et a son prix, et ne pas utiliser `nom_sandwich` comme clé primaire

## Exercice 5

- Nous aurons besoin d'une table `student` avec les colonnes nom (type `Char`) & id (type `Varchar`) id est clé primaire
- La table `matiere` avec une colonne qui contient toute les matière ainis qu'une colonne qui contient un identifiant (type `numauto`) pour désigner chaque matière. ID est clé primaire
- Une table `note` contenant les note assigné a un ID clé primaire
- Et enfin une table `bulletin` qui contient toute les clé étrangère des ID : de `student`, `matiere` et `note`.

## Exercice 6

### Q1
Le schéma relationnel de la base de données :

```
Eleve(nom, prenom, date_naissance, classe, option1, option2, option3)
```
### Q2

Ici le problème majeur dans cette table c'est la redondance des data.

Comme vu plus haut il faudrait séparer en deux table : `options` qui contient les options associé a un `ID unique` qui serait clé primaire, et `eleve` qui contient les attributs `nom`, `prenom`, `date_naissance` et `classe`. Ainsi on pourrait afficher les data sans écrire plusieurs fois les noms des options, ce qui rend également les mises à jour plus facile si on souhaite par exemple modifier le nom d'une option.

### Q3

Eleve(nom, prenom, date_naissance, classe)


|nom         | prenom  | date_naissance | classe|
|------------|---------|----------------|--------|
|Armand      | Léa     | 12/02/05       | 1G1|
|Joulain     | Marie   | 13/01/06       | 2de3|
|Marchand    | Anthony | 12/12/05       | 1G1|
|Marchand    | Sophie  | 06/04/04       | TG2|

Option(eleve_nom, option)

|eleve_nom   | option      |
-------------|-------------|
|Armand      | Maths       |
|Armand      | NSI         |
|Armand      | LLCE Anglais|
|Joulain     | DNL Anglais |
|Marchand    | HGGSP       |
|Marchand    | SES         |
|Marchand    | Maths       |
|Marchand    | Physique    |
