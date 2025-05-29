import time
class Task:
     
 def __init__(self,tasks):
    self.tasks=tasks
    self.file_path=r"D:\junior_assigments\to do list 2\to_do_list.txt"
def load_tasks(self):
        tasks = {}
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    if '::' in line:
                        task, timestamp = line
                        tasks[task] = timestamp
        except FileNotFoundError:
            print("File not found. Creating a new task file...")
        return tasks
def save_tasks(self,tasks):
    with open(self.file_path, 'w') as file:
        for task, timestamp in tasks.items():
        
            file.write(f"{task}  {timestamp}\n")  

def add_task(self,tasks):
    task=input("enter a task")
    if task in self.tasks:
        print(f"Task '{task}' already exists. Do you want to edit it?")
        a = input("Enter Yes / No: ")
        if a == "yes":
            new_task = input("Enter the new task description: ").strip()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            del self.tasks[task]  
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
    
def remove_task(self,tasks):
    task = input("Enter task to remove: ").strip()
    if task in self.tasks:
        del tasks[task]  
        save_tasks(tasks)
        print(f"Task '{task}' removed.")
    else:
        print("Task not found.")
def show_tasks(self,tasks):
    if self.tasks:
        print("\nYour Tasks:")
        for task, timestamp in tasks.items():
            print(f"- {task} (Added on {timestamp})")
    else:
        print("No tasks found.")

def check(self):
        self.tasks =load_tasks()
        
while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. Remove Task")  
        print("3. Show All Tasks")
        print("4. Exit")
        a = input("Enter your choice (1-5):")
        
        if a == "1":
            add_task()
        elif a == "2":
            remove_task()
        elif a == "3":
            show_tasks()
        elif a == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

todolist=Task()
todolist.check()

    