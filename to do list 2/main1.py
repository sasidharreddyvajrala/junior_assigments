import time

class Task:
    def __init__(self, tasks):
         self.tasks = tasks
        
         self.file_path=r"D:\junior_assigments\to do list 2\to_do_list.txt"

    def load_tasks(self):
        #tasks = {}
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                  if '::' in line:
                        task, timestamp = line.strip().split('  ', 1)
                        tasks[task] = timestamp
        except FileNotFoundError:
            print("File not found. Creating a new task file...")
        return tasks

    def save_tasks(self, tasks):
        with open(self.file_path, 'w') as file:
            for task, timestamp in tasks.items():
                file.write(f"{task}  {timestamp}\n") 

class AddTask(Task):
    def add_task(self, tasks):
        task = input("enter a task").strip() 
        if task in tasks: 
            print(f"Task '{task}' already exists. Do you want to edit it?")
            a = input("Enter Yes / No: ").strip().lower()
            if a == "yes":
                new_task_desc = input("Enter the new task: ").strip()
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                del tasks[task]
                tasks[new_task_desc] = timestamp
                self.save_tasks(tasks) 
                print(f"Task '{new_task_desc}' updated at {timestamp}.")
            else:
                print("No changes made.")
        else:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            tasks[task] = timestamp
            self.save_tasks(tasks) 
            print(f"Task '{task}' added at {timestamp}.")

class RemoveTask(Task):
    def remove_task(self, tasks):
        task_to_remove = input("Enter task to remove").strip()
        if task_to_remove in tasks:
            del tasks[task_to_remove]
            self.save_tasks(tasks) 
            print(f"Task '{task_to_remove}' removed.")
        else:
            print("Task not found.")

class ShowTasks(Task):
    def show_tasks(self, tasks):
        if tasks: 
            print("\nYour Tasks:")
            for task, timestamp in tasks.items():
                print(f"- {task} (Added on {timestamp})")
        else:
            print("No tasks found.")

class Run(Task):
    def run(self):
        tasks = self.load_tasks() 

        while True:
            print("\n--- TO-DO LIST ---")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Show All Tasks")
            print("4. Exit")
            a = input("Enter your choice (1-4):").strip() 
            if a == "1":
                add_task = AddTask(tasks) 
                add_task.add_task(tasks)
            elif a == "2":
                remove = RemoveTask(tasks) 
                remove.remove_task(tasks)
            elif a == "3":
                show_tasks= ShowTasks(tasks) 
                show_tasks.show_tasks(tasks)
            elif a == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter 1-4.")


tasks = {} 
object= Run(tasks)
object.run()