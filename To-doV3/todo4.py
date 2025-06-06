import os

def load_tasks(filepath):
    tasks = []
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
        return tasks, f"No file found. Created new file at '{filepath}'."
    
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 3:
                title, description, status = [p.strip() for p in parts]
                task = {"title": title, "description": description, "status": status}
                tasks.append(task)
    return tasks, f"Tasks loaded from '{filepath}'."

def save_tasks(filepath, tasks):
    with open(filepath, 'w') as file:
        for task in tasks:
            file.write(f"{task['title']} | {task['description']} | {task['status']}\n")
    return f"Tasks saved to {filepath}"

def find_title(title, tasks):
    for task in tasks:
        if task["title"] == title:
            return task 
    return None

def add_task(tasks):
    title = input("Enter title to add: ")
    desc = input("Enter description: ")
    if find_title(title, tasks):
        return f"Task '{title}' already exists."
    tasks.append({"title": title, "description": desc, "status": "pending"})
    return f"Task '{title}' added."

def delete_task(tasks):
    title = input("Enter title to delete: ")
    task = find_title(title, tasks)
    if task:
        tasks.remove(task)
        return f"Task '{title}' deleted."
    return "Task not found."

def complete_task(tasks):
    title = input("Enter title to mark as complete: ")
    task = find_title(title, tasks)
    if task:
        task["status"] = "complete"
        return f"Task '{title}' marked complete."
    return "Task not found."

def show_tasks(tasks):
    if not tasks:
        return "Task list is empty."
    output = "\n--- TASK LIST ---\n"
    for i, task in enumerate(tasks, 1):
        output += f"{i}. {task['title']} | {task['description']} | {task['status']}\n"
    return output.strip()

def display_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Complete Task")
    print("5. Save Tasks")
    print("6. Exit")

def main():
    filepath = r".\task_list.txt"
    tasks, msg = load_tasks(filepath)
    print(msg)

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            print(add_task(tasks))
        elif choice == 2:
            print(show_tasks(tasks))
        elif choice == 3:
            print(delete_task(tasks))
        elif choice == 4:
            print(complete_task(tasks))
        elif choice == 5:
            print(save_tasks(filepath, tasks))
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
