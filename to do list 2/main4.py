import time

class TaskStoring:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_tasks(self):
        tasks = {}
        try:
            with open(self.file_path, 'r') as file:
                for line in file:

                    # Handle lines with '::' separator
                    if '::' in line:
                        task, timestamp = line.strip().split("::")
                        tasks[task] = timestamp
                    # Handle lines with space separator
                    elif ' ' in line:
                         parts = line.strip().split(" ", 1)
                         if len(parts) == 2:
                             task, timestamp = parts
                             tasks[task] = timestamp

        except FileNotFoundError:
            print("Task file not found. A new file will be created upon saving.")
        return tasks

class Save_Tasks:

    def save_tasks(self, tasks, file_path):
        
        if not isinstance(tasks, dict):
             print("Error: Tasks to be saved must be in a dictionary format.")
             return

        with open(file_path, 'w') as file:
            for task, timestamp in tasks.items():
                file.write(f"{task} {timestamp}\n")

class AddTask:

    def add_task(self):
        task = input("Enter a task: ")
        if task in self.tasks:
            print(f"Task '{task}' already exists. Do you want to edit it?")
            choice = input("Enter Yes / No: ")
            if choice.lower() == "yes":
                new_task = input("Enter the new task : ")
            
                self.tasks[new_task] = self.tasks.pop(task)

                
                self.save_manager.save_tasks(self.tasks, self.store.file_path)
                print(f"Task '{task}' updated to '{new_task}'.")
            else:
                print("No changes made.")
        else:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            self.tasks[task] = timestamp

            
            self.save_manager.save_tasks(self.tasks, self.store.file_path)
            print(f"Task '{task}' added at {timestamp}.")

class RemoveTask:
    def remove_task(self):
        task = input("Enter task to remove: ")
        if task in self.tasks:
            del self.tasks[task]

            self.save_manager.save_tasks(self.tasks, self.store.file_path)
            print(f"Task '{task}' removed.")
        else:
            print("Task not found.")

class ShowTasks:
    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nYour Tasks:")
        for task, timestamp in self.tasks.items():
            print(f"- {task} (Added on {timestamp})")


class All_Tasks(AddTask, RemoveTask, ShowTasks):
    def __init__(self, tasks, store, save_manager):
        self.store = store
        self.tasks = tasks
       
        self.save_manager = save_manager

class Run:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        while True:
            print("\n--- TO-DO LIST ---")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Show All Tasks")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                self.manager.add_task()
            elif choice == "2":
                self.manager.remove_task()
            elif choice == "3":
                self.manager.show_tasks()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter 1-4.")

file_path =r"D:\junior_assigments\to do list 2\to_do_list.txt"
s= TaskStoring(file_path)
tasks = s.load_tasks()

save = Save_Tasks()


alltasks = All_Tasks(tasks, s, save)
run = Run(alltasks)
run.run()