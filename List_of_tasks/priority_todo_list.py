from datetime import datetime

todo_list = {}

def ajouter_tache(intitule, date_limite, priorite):
    try:
        date_limite = datetime.strptime(date_limite, "%d/%m/%Y")
    except ValueError:
        print("Date invalide. Utilisez le format JJ/MM/AAAA.")
        return

    if not 1 <= priorite <= 5:
        print("Priorité invalide. Utilisez une priorité entre 1 et 5.")
        return

    todo_list[intitule] = (False, date_limite, priorite)

def decrire_tache(intitule):
    if intitule in todo_list:
        tache = todo_list[intitule]
        status = "a été" if tache[0] else "n'a pas été"
        return f"La tâche '{intitule}' de priorité {tache[2]}, et à compléter au plus tard le {tache[1].strftime('%d/%m/%Y')} {status} effectuée."
    else:
        return "Cette tâche n'existe pas dans la liste."

def trop_tard(date):
    try:
        date = datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
        print("Date invalide. Utilisez le format JJ/MM/AAAA.")
        return

    for tache, details in todo_list.items():
        if not details[0] and details[1] < date:
            print(f"La tâche '{tache}' était à compléter avant le {details[1].strftime('%d/%m/%Y')} et n'a pas été effectuée.")

def important(niveau_priorite):
    for tache, details in todo_list.items():
        if not details[0] and details[2] >= niveau_priorite:
            print(f"Tâche : {tache}, Priorité : {details[2]}, Date limite : {details[1].strftime('%d/%m/%Y')}")

# Test des fonctions
ajouter_tache("Coiffeur", "29/02/2024", 2)

print(decrire_tache("Coiffeur"))
print(decrire_tache("Inconnue"))

trop_tard("01/03/2024")

important(3)