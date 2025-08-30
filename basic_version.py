# to_do_list_basic.py
# Simple To-Do List (No File Storage, only memory)

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove!")
        else:
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to remove: "))
                if 0 <= num < len(tasks):
                    removed = tasks.pop(num)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
