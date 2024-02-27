# Vecteur creux

# a) Ecrire une fonction qui prend un tableau et le représente comme un vecteur creux : v = [0,0,4,0,0,0,5,6] sera représenté par [(2,4),(6,5),(7,6)]

def faire_creux(plein):
    v = []
    for (i, x) in enumerate(plein):
        if x != 0.:
            v.append((i + 1, x))
    return v

# Utilisation
print("--- Ex a ---")

l = [0, 10, 0, 0, 0, 0, 0, -2.5, 0, 0., 0.]
v = faire_creux(l)
print(v)


# b) Coder un encodage analogue pour les matrices, mais cette fois sous forme d'un dictionnaire : m = [[0,4],[5,6]] sera représenté par {(0,1):4, (1,0):5,(1,1):6}

def matrix_to_dict(matrix):
    result = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[(i, j)] = matrix[i][j]
    return result

def dict_to_matrix(dictionary):
    max_i = max([coord[0] for coord in dictionary.keys()])
    max_j = max([coord[1] for coord in dictionary.keys()])
    result = [[0] * (max_j + 1) for _ in range(max_i + 1)]
    for coord, value in dictionary.items():
        result[coord[0]][coord[1]] = value
    return result

# Exemple
m = [[0, 4], [5, 6]]
d = matrix_to_dict(m)
print("Matrice originale:", m)
print("Dictionnaire représentant la matrice:", d)
print("Matrice reconstruite à partir du dictionnaire:", dict_to_matrix(d))