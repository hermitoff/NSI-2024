from datetime import datetime

todo_list = {}

def ajouter_tache(intitule, date_limite, priorite):
    if not isinstance(intitule, str):
        return "L'intitulé de la tâche doit être une chaîne de caractères."
    if not isinstance(date_limite, str):
        return "La date limite doit être une chaîne de caractères au format 'jj/mm/aaaa'."
    if not isinstance(priorite, int) or priorite < 1 or priorite > 5:
        return "La priorité doit être un entier compris entre 1 et 5."

    try:
        datetime.strptime(date_limite, '%d/%m/%Y')
    except ValueError:
        return "La date limite doit être au format 'jj/mm/aaaa'."

    todo_list[intitule] = (False, date_limite, priorite)
    return f"Tâche '{intitule}' ajoutée avec succès."

def decrire_tache(intitule):
    if intitule not in todo_list:
        return f"La tâche '{intitule}' n'existe pas dans la liste des tâches."
    
    done = "a été" if todo_list[intitule][0] else "n'a pas été"
    return f"La tâche '{intitule}' de priorité {todo_list[intitule][2]}, et à compléter au plus tard le {todo_list[intitule][1]} {done} effectuée."

def trop_tard(date_limite):
    try:
        date_limite = datetime.strptime(date_limite, '%d/%m/%Y')
    except ValueError:
        return "La date doit être au format 'jj/mm/aaaa'."

    overdue_tasks = [tache for tache, (effectue, date, priorite) in todo_list.items() if not effectue and datetime.strptime(date, '%d/%m/%Y') < date_limite]
    if overdue_tasks:
        return f"Tâches non effectuées avec une limite antérieure au {date_limite.strftime('%d/%m/%Y')} : {', '.join(overdue_tasks)}"
    else:
        return "Aucune tâche non effectuée avec une limite antérieure à cette date."

def importantes(niveau_priorite):
    if not isinstance(niveau_priorite, int) or niveau_priorite < 1 or niveau_priorite > 5:
        return "Le niveau de priorité doit être un entier compris entre 1 et 5."

    high_priority_tasks = [tache for tache, (effectue, date, priorite) in todo_list.items() if not effectue and priorite >= niveau_priorite]
    if high_priority_tasks:
        return f"Tâches non effectuées d'un niveau de priorité au moins aussi important que {niveau_priorite} : {', '.join(high_priority_tasks)}"
    else:
        return f"Aucune tâche non effectuée d'un niveau de priorité au moins aussi important que {niveau_priorite}."

# b) Ajouter la tâche << Coiffeur >>, de priorité 2, à effectuer au plus tard le 29/2/2024.
print(ajouter_tache("Coiffeur", "29/02/2024", 2))

# Test de la fonction ajouter_tache avec diverses valeurs incorrectes pour ses paramètres
print(ajouter_tache(123, "29/02/2024", 2))  # intitulé invalide
print(ajouter_tache("Coiffeur", "31/02/2024", 2))  # date invalide
print(ajouter_tache("Dentiste", "29/02/2024", 6))  # priorité invalide

# Exemple de la fonction decrire_tache
print(decrire_tache("Coiffeur"))

# Exemple de la fonction trop_tard
print(trop_tard("01/02/2024"))

# Exemple de la fonction importantes
print(importantes(3))