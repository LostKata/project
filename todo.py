import json


class Task:
    def __init__(self, description, due_date, completed = False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} (Due: {self.due_date}) - {status}"


class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)
        self.save_tasks()


    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
    
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([t.__dict__ for t in self.tasks], file)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_dict = json.load(file)
                return [Task(**t) for t in tasks_dict]
        except FileNotFoundError:
            return []

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose and option: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(description, due_date)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
