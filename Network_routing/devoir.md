# Protocoles de routage

## Exercice 3
### Q1
#### Table de routage R1

| Destination | Prochain hit     | Coût |
|---------------------|--------------|-----------|
| 192.168.10.0/24     | Direct       | 0         |
| 192.168.20.0/24     | Direct       | 0         |
| 192.168.30.0/24     | 192.168.20.2 | 1         |
| 192.168.40.0/24     | 192.168.20.2 | 2         |
| 192.168.50.0/24     | 192.168.20.2 | 3         |

#### Table de routage R4

| Destination | Prochain hit     | Coût |
|---------------------|--------------|-----------|
| 192.168.40.0/24     | Direct       | 0         |
| 192.168.50.0/24     | Direct       | 0         |
| 192.168.30.0/24     | 192.168.40.1 | 1         |
| 192.168.20.0/24     | 192.168.40.1 | 2         |
| 192.168.10.0/24     | 192.168.40.1 | 3         |
### Q2
#### Table de routage R5

| Destination | Prochain hit       | Coût |
|---------------------|----------------|-----------|
| 192.168.60.0/24     | Direct         | 0         |
| 192.168.70.0/24     | Direct         | 0         |
| 192.168.10.0/24     | 192.168.60.2   | 1         |
| 192.168.20.0/24     | 192.168.60.2   | 1         |
| 192.168.30.0/24     | 192.168.60.2   | 2         |
| 192.168.40.0/24     | 192.168.70.2   | 1         |
| 192.168.50.0/24     | 192.168.70.2   | 2         |

### Q3
#### Table de routage R1
| Destination | Prochain hit       | Coût |
|---------------------|--------------|-----------|
| 192.168.10.0/24     | Direct       | 0         |
| 192.168.20.0/24     | Direct       | 0         |
| 192.168.30.0/24     | 192.168.20.2 | 1         |
| 192.168.40.0/24     | 192.168.20.2 | 2         |
| 192.168.50.0/24     | 192.168.20.2 | 3         |
| 192.168.60.0/24     | Direct       | 0         |
| 192.168.70.0/24     | 192.168.60.1 | 1         |

#### Table de routage R4
| Destination | Prochain hit       | Coût |
|---------------------|--------------|-----------|
| 192.168.40.0/24     | Direct       | 0         |
| 192.168.50.0/24     | Direct       | 0         |
| 192.168.30.0/24     | 192.168.40.1 | 1         |
| 192.168.20.0/24     | 192.168.40.1 | 2         |
| 192.168.10.0/24     | 192.168.40.1 | 3         |
| 192.168.70.0/24     | Direct       | 0         |
| 192.168.60.0/24     | 192.168.70.1 | 1         |
### Q4
> Après avoir mis à jour leurs tables, R1 envoie ses informations de routage à R2 et R5, et R4 les envoie à R3 et R5.
>
>Les autres routeurs doivent actualiser leurs tables s'ils reçoivent un chemin plus court vers un réseau. Dans RIP, chaque routeur partage régulièrement sa table de routage avec ses voisins pour garantir que le réseau reste optimisé et convergent.

## Exercice 4
1. 
| Liaison | Débit      | Coût |
|---------|------------|------|
| R1-R2   | 10 Gbps    | 1    |
| R1-R3   | 1 Gbps     | 10   |
| R2-R4   | 1 Gbps     | 10   |
| R3-R5   | 10 Gbps    | 1    |
| R4-R5   | 10 Gbps    |  10  |
| R5-R6   | 1 Gbps     | 10   |
| R5-R7   | 100 Mbps   | 100  |
| R6-R7   | 1 Gbps     | 10   |
2. 
| Liaison | Coût |
|---------|------|
| R1-R2   | 1    |
| R1-R3   | 10   |
| R2-R4   | 10   |
| R3-R5   | 1    |
| R4-R5   | 10   |
| R5-R6   | 10   |
| R5-R7   | 100  |
| R6-R7   | 10   |
3. 
| Destination | En passant par | Coût total |
|-------------|----------------|------------|
| R2          | Direct (R2)    | 1          |
| R3          | Direct (R3)    | 10         |
| R4          | R2             | 11         |
| R5          | R3             | 11         |
| R6          | R3 puis R5     | 21         |
| R7          | R3 puis R5     | 111        |

## Exercice 5
### Q1
1. R1-R2-R3-R5-R4-R6-R7
2. R1-R3-R5-R7
### Q2
1. E-D-A-C-B-F (70)
### Q3
1. A-B-F-H (32)
## Exercices 6
| Cherche à atteindre | Moyen de l'atteindre | Métrique RIP | Métrique OSPF |
|-------------|----------------|----------|-----|
| R1          | eth0           | N        | N   |
| B           | eth1           | N        | N   |
| D           | eth2           | N        | N   |
| R2          | B              | 1        |     |
| R2          | D              | 20       |     |
| R3          | B              | 10       |     |
| R3          | D              | 10       |     |
| R4          | D              | 1        |     |
| R4          | B              | 3        |     |

## Exercices 7
### Q1
1. Le trajet sera `A C E G` ou `A C F G`
2. 
| Table de routage du routeur G            |||
|-------------|-----------------|----------|
| Destination | Routeur suivant | Distance |
| A | E | 3 |
| B | E | 3 |
| C | E | 2 |
| D | E | 2 |
| E | E | 1 |
| F | F | 1 |
### Q2
| Table de routage du routeur A (défaillance)|||
|-------------|-----------------|----------|
| Destination | Routeur suivant | Distance |
| B | B | 1 |
| C | D | 3 |
| D | D | 1 |
| E | D | 2 |
| F | D | 4 |
| G | D | 3 |