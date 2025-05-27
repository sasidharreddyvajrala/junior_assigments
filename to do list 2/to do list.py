import time

TASK_FILE = r"C:\Users\SPSOFT\OneDrive\Desktop\to do list 2\to_do_list.txt"

def load_tasks():
    tasks = {}
    try:
        with open(TASK_FILE, 'r') as file:
            for line in file:
                if '::' in line:
                    task, timestamp = line.strip().split('::')
                    tasks[task] = timestamp
    except FileNotFoundError:
        print("File not found. Creating a new task file...")
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task, timestamp in tasks.items():
        
            file.write(f"{task}  {timestamp}\n")  

def add_task(tasks):
    task = input("Enter task to add: ").strip()
    
    if task in tasks:
        print(f"Task '{task}' already exists. Do you want to edit it?")
        a = input("Enter Yes / No: ").strip().lower()

        if a == "yes":
            new_task = input("Enter the new task description: ").strip()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            del tasks[task]  
            tasks[new_task] = timestamp  
            save_tasks(tasks)
            print(f"Task '{new_task}' updated at {timestamp}.")
        else:
            print("No changes made.")
    else:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        tasks[task] = timestamp  
        save_tasks(tasks)
        print(f"Task '{task}' added at {timestamp}.")

def remove_task(tasks):
    task = input("Enter task to remove: ").strip()
    if task in tasks:
        del tasks[task]  
        save_tasks(tasks)
        print(f"Task '{task}' removed.")
    else:
        print("Task not found.")

def show_all_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for task, timestamp in tasks.items():
            print(f"- {task} (Added on {timestamp})")
    else:
        print("No tasks found.")

def check():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. Remove Task")  
        print("3. Show All Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            add_task(tasks) 
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            show_all_tasks(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

check()
