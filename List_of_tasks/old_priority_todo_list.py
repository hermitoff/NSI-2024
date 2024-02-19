import datetime

# a) Création de la todo_list
todo_list = {}

# Exemple de contenu de la todo_list
# "Test": (False, "2024-02-28", 3)

def ajouter_tache(intitule, date_limite, priorite):
    global todo_list
    
    # Vérifier si la priorité est valide
    if not 1 <= priorite <= 5:
        print("La priorité doit être comprise entre 1 et 5.")
        return
    
    # Vérifier si la date est valide (vous pouvez ajouter plus de vérifications si nécessaire)
    try:
        datetime.datetime.strptime(date_limite, "%Y-%m-%d")
    except ValueError:
        print("La date limite est invalide. Utilisez le format YYYY-MM-DD.")
        return
    
    # Ajouter la tâche à todo_list
    todo_list[intitule] = (False, date_limite, priorite)
    print("Tâche ajoutée avec succès à la liste.")

