# TP Observation base de donnée

## Q1
La base contient 5 tables.

## Q2
Un champ est une information éléméntaire de base de donnée.

## Q3
Un nuplet est une ligne dans un tableau qui contient un ensemble de données liées.

## Q4
|Nom de la table|Nom du champ|Type et taille du champ|Clé primaire|
|---|---|---|---|
|FOURNISSEUR|NumFour|Entier long|Oui|
||NomFour|Entier (30)|Non|
||AdresFour|Entier (50)|Non|
|PRODUIT|NumProd|Entier long & Nombre|Oui|
||LibelleProd|Chaine de caractère|Non|
||PrixProd|Monétaire Nombre|Non|
||NumFour|Entier long|Non|
|CLIENT|NumCli|Entier Long|Oui|
||NomCli|Nombre (30)|Non|
||AdresCli|Texte court|Non|
|COMMANDE|NumCom|Entier Long|Oui|
||DateCom|Date (abrégé)|Non|
||NumCli|Entier Long|Non|
|CONTENIR|NumProd|Entier long|Oui|
||NumCom|Entier long|Oui|
||Qté|Entier long|Non|

## Q5
Une clé primaire est un champ ou un ensemble de champs de table qui contient des valeurs uniques. Elle permet d'identifier chaque ligne de manière unique dans une table et elle ne peut jamais être vide ou contenir la valeur Null.

## Q6
Une clé étrangère est un ou plusieurs champs dans une base de données qui est lié à la colonne de clé primaire d'une autre table.

## Q7
Non, pas entièrement en tout car les clés primaires ou étrangère peuvent les lié entre elles

## Q8
Les relations entre les tables sont établies en utilisant des clés primaires et étrangères. Une clé primaire dans une table peut être référencée par une clé étrangère dans une autre table, ce qui crée une relation entre les deux tables.

## Q9
Il s'agit d'un système important qui garantit la cohérence et la validité des relations entre les données

## Q10
Il s'agit d'un autre système de sécurité qui permet de vérifier que toutes les entrée d'une colonne sont cohérentes et respecte des règles de validité (par exemple un prix ne peut pas être négatif, alors ce mecanisme empêchera l'insersion d'un nombre négatif)

## Q11
1. Vrai
2. Faux
3. Faux
4. Faux
5. Vrai

## Q12
