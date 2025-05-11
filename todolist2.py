import json

class TodoList:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = task
        self.save_tasks()
        print(f"Tâche ajoutée avec l'ID {task_id}")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.save_tasks()
            print(f"Tâche {task_id} supprimée")
        else:
            print("ID non trouvé")

    def modify_task(self, task_id, new_task):
        if task_id in self.tasks:
            self.tasks[task_id] = new_task
            self.save_tasks()
            print(f"Tâche {task_id} modifiée")
        else:
            print("ID non trouvé")

    def search_task(self, task_id):
        return self.tasks.get(task_id, "Tâche non trouvée")


# Exemple d'utilisation
todo = TodoList()
todo.add_task("Acheter du lait")
todo.add_task("Réviser Python")
print(todo.search_task(1))  # Recherche de la tâche avec ID 1
todo.modify_task(2, "Apprendre Django")  # Modification de la tâche avec ID 2
todo.remove_task(1)  # Suppression de la tâche avec ID 1