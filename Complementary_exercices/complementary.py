# I Inverser un dictionnaire

dico_capitales = {"AFGHANISTAN":"KABOUL",
    "AFRIQUE DU SUD":"PRƒTORIA",
    "ZIMBABWƒ":"HARARƒ",
    "Pétélo":"Squat"}

#for key in dico_capitales:
#	print(dico_capitales[key]," est la capitale de ",key)

def invert_dict(dictionnaire):
    dictionnaire_inverse = {}
    for key, v in dictionnaire.items():
        dictionnaire_inverse[v] = key
    return dictionnaire_inverse

# Question c
def question_c():
    if invert_dict(dico_capitales) == invert_dict(invert_dict(dico_capitales)):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    print(invert_dict(dico_capitales))
    question_c()