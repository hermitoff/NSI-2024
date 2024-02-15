# a) Création de la liste de tâches
todo_list = {
    "Faire les courses": True,
    "Ranger le garage": False,
    "Compléter l'exercice 4": False
}

# b) Fonction pour compter les tâches non complétées
def count_incomplete_tasks(todo_list):
    incomplete_tasks = sum(1 for task in todo_list.values() if not task)
    print("Nombre de tâches non complétées :", incomplete_tasks)
    return incomplete_tasks

# c) Fonction pour gérer la liste de tâches
def print_tasks(todo_list):
    for i, (task, done) in enumerate(todo_list.items(), start=1):
        status = "v" if done else " "
        print(f"{i}. [{status}] {task}")

def manage_tasks():
    while True:
        print("\n--- Liste de tâches ---")
        print_tasks(todo_list)
        command = input("\nEntrez votre commande (+/-/v/?) : ").strip()

        if command == '+':
            task_name = input("Entrez le nom de la nouvelle tâche : ")
            todo_list[task_name] = False
        elif command.startswith('-'):
            try:
                task_index = int(command[1:]) - 1
                task_to_remove = list(todo_list.keys())[task_index]
                del todo_list[task_to_remove]
            except (IndexError, ValueError):
                print("Numéro de tâche invalide.")
        elif command.startswith('v'):
            try:
                task_index = int(command[1:]) - 1
                task_to_update = list(todo_list.keys())[task_index]
                todo_list[task_to_update] = not todo_list[task_to_update]
            except (IndexError, ValueError):
                print("Numéro de tâche invalide.")
        elif command == '?':
            print("\n--- Tâches restant à faire ---")
            remaining_tasks = {task: done for task, done in todo_list.items() if not done}
            print_tasks(remaining_tasks)
        else:
            print("Commande invalide.")

# Appel des fonctions
if __name__ == "__main__":
    manage_tasks()
    #count_incomplete_tasks(todo_list)