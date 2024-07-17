import json

class Node:
    def __init__(self, question=None, animal=None):
        self.question = question
        self.animal = animal
        self.yes = None
        self.no = None

def ask_question(node):
    if node.animal is not None:
        return f"Est-ce que c'est {node.animal} ?"
    else:
        return node.question

def update_tree(node, user_animal, difference):
    new_question = input("Quelle question permet de différencier votre animal de celui proposé ? ")
    animal_leaf = Node(animal=node.animal)
    user_leaf = Node(animal=user_animal)
    
    if input(f"Pour votre animal, la réponse à cette question est-elle 'oui' ou 'non' ? ").strip().lower() == 'oui':
        node.question = new_question
        node.yes = user_leaf
        node.no = animal_leaf
    else:
        node.question = new_question
        node.yes = animal_leaf
        node.no = user_leaf
    node.animal = None

def traverse_tree(node):
    while node.animal is None:
        answer = input(ask_question(node) + " (oui/non) ").strip().lower()
        if answer == 'oui':
            node = node.yes
        else:
            node = node.no
    return node

def play_game(root):
    while True:
        current_node = traverse_tree(root)
        answer = input(ask_question(current_node) + " (oui/non) ").strip().lower()
        if answer == 'oui':
            print("Gagné !")
        else:
            user_animal = input("Quel est le nom de votre animal ? ")
            difference = input(f"Quelle est la différence entre {current_node.animal} et {user_animal} ? ")
            update_tree(current_node, user_animal, difference)
        
        if input("Voulez-vous jouer encore ? (oui/non) ").strip().lower() != 'oui':
            break

def save_tree(node, file_name):
    def serialize(node):
        if node is None:
            return None
        return {
            'question': node.question,
            'animal': node.animal,
            'yes': serialize(node.yes),
            'no': serialize(node.no)
        }
    
    with open(file_name, 'w') as f:
        json.dump(serialize(node), f, indent=4)

def load_tree(file_name):
    def deserialize(data):
        if data is None:
            return None
        node = Node(question=data['question'], animal=data['animal'])
        node.yes = deserialize(data['yes'])
        node.no = deserialize(data['no'])
        return node
    
    with open(file_name, 'r') as f:
        data = json.load(f)
        return deserialize(data)

# Initial tree
root = Node(question="Est-ce que c'est un mammifère ?")
root.yes = Node(animal="chien")
root.no = Node(animal="poisson")

# Play the game
play_game(root)

# Save the tree
save_tree(root, 'animal_tree.json')

# Load the tree (for future use)
# root = load_tree('animal_tree.json')