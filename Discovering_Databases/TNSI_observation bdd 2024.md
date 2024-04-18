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
1. Requête facturation

   Dans la première ligne on importe de la base CLIENT NumCli, NomCli et on fait la somme de la quantité par le prix de production, tout sa dans la variable Montant_Achat.
   2ème ligne : Depuis la base CLIENT, COMMANDE, CONTENIR et PRODUIT
   3ème ligne : La commande `WHERE` permet de filtrer...

   Globalement ces requêtes SQL permettent d'obtenir le montant total des achats effectué par les clients

2. Requête 1
   
   Premièrement, on obtient les data des Tables et on les affiches, ici on obtient les numéro de commandes et le nom du client associé.

3. Requête 2
   
   On obtient les data, mais cette fois on peux imaginer que cette requête est utile pour les employés qui ont besoin du prix de fabrication des produits car à la fin de la ligne 3 on peut voir que le prix de production est importé.

4. Requête 3
   
   Cette requête permet d'obtenir les date des commandes qui ont été effectué dans le magasin.

5. Requête 4
   
   Cette requête permet d'obtenir les numéros de clients et leur noms ainsi que cette fois le montant de leur achat et dans une nouvelle colonne le montant de leur remise.

6. Requête 5
   
   Cette requête permet d'obtenir une liste des identifiants de clients `(NumCli)` qui ont passé au moins une commande, en se basant sur les données de la table `COMMANDE` et en les associant aux clients de la table `CLIENT` par l'intermédiaire de la jointure.