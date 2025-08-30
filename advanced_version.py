# to_do_list.py

class ToDoList:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """loads the tasks from the file. (if already saved)."""
        try:
            with open(self.filename, "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        """saves the current tasks in the file"""
        with open(self.filename, "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def add_task(self, task):
        """adds the new task."""
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_number):
        """deletes the task by index number"""
        if 0 <= task_number < len(self.tasks):
            removed = self.tasks.pop(task_number)
            self.save_tasks()
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")

    def show_tasks(self):
        """prints all the tasks"""
        if not self.tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")


def main():
    todo = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            todo.show_tasks()
        elif choice == "2":
            task = input("Enter task: ")
            todo.add_task(task)
            print("Task Added!")
        elif choice == "3":
            todo.show_tasks()
            try:
                num = int(input("Enter task number to remove: "))
                todo.remove_task(num)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
