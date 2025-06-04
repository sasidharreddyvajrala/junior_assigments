import os
import sys
from abc import ABC, abstractmethod

class Task:
    def __init__(self,title:str,description):
        self.title= title
        self.description = description
        self.status = "pending"

    def to_dict(self):
        return {
            "Title":self.title,
            "Description":self.description,
            "Status": self.status
        }
    def mark_complete(self):
        self.status = "complete"

class TaskList:
    def __init__(self):
        self.tasks = []

class Operation(ABC):
    def __init__(self,task_list:TaskList):
        self.task_list = task_list
    
    @abstractmethod
    def execute(self):
        pass

    def find_task(self,title:str):
        for task in self.task_list.tasks:
            if task.title == title:
                return task
        return None
    
class AddTask(Operation):
    def __init__(self,task_list:TaskList):
        self.task_list = task_list
    def execute(self):
        title = input("Enter title: ")
        desc = input("Enter description: ")
        task = self.find_task(title)
        if task:
            print(f"Task '{title}' already exists.")
            return
        new_task = Task(title, desc)
        self.task_list.tasks.append(new_task)
        print(f"Task '{title}' added.")

class DeleteTask(Operation):
    def __init__(self,task_list:TaskList):
        self.task_list = task_list
    def execute(self):
        title = input("Enter title: ")
        task = self.find_task(title)
        if task:
            self.task_list.tasks.remove(task)
            print(f"Task '{title}' deleted.")
        else:
            print("Task not found.")

class CompleteTask(Operation):
    def __init__(self,task_list:TaskList):
        self.task_list = task_list
    def execute(self):
        title = input("Enter title: ")
        task = self.find_task(title)
        if task:
            task.mark_complete()
            return
        print("Task not found")

class ShowTasks(Operation):
    def __init__(self, task_list):
        super().__init__(task_list)

    def execute(self):
        if not self.task_list.tasks:
            print("Task list is empty.")
            return
        print("\n--- TASK LIST ---")
        for i, task in enumerate(self.task_list.tasks):
            print(f"{i+1}. {task.title}  | {task.description} | {task.status}")

class TaskLoader:
    def __init__(self,filepath):
        self.filepath = filepath
    def load_tasks(self,task_list):
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                pass
            print(f"No file found. Created new file at '{self.filepath}'.")
            return
        with open(self.filepath,'r') as file:
            for line in file:
                parts = line.strip().split('|')
                
                if len(parts) == 3:
                    title, description, status = [p.strip() for p in parts]
                    task = Task(title, description)
                    task.status = status
                    task_list.tasks.append(task)
        print(f"Tasks loaded from '{self.filepath}'.")

class TaskSaver(Operation):
    def __init__(self, task_list, filepath):
        super().__init__(task_list)
        self.filepath = filepath

    def execute(self):
        with open(self.filepath, 'w') as file:
            for task in self.task_list.tasks:
                file.write(f'{task.title} | {task.description} | {task.status}\n')
        print(f"Tasks saved to {self.filepath}")


def display_menu(operations):
        print("\n--- TO-DO LIST MENU ---")
        for key, (label, _) in operations.items():
            print(f"{key}. {label}")
def main():
    filepath = "task_list.txt"
    task_list = TaskList()

    loader = TaskLoader(filepath)
    loader.load_tasks(task_list)
    
    operations  = {
        1:("Add Task",AddTask(task_list)),
        2:("Show Tasks",ShowTasks(task_list)),
        3:("Delete Task",DeleteTask(task_list)),
        4:("Complete Task",CompleteTask(task_list)),
        5:("Save Tasks",TaskSaver(task_list,filepath)),
        6:("Exit",None)
    }
    while True:
        display_menu(operations)
        choice = int(input("Enter choice: "))
        action = operations.get(choice)

        if not action:
            print("Invalid input.")
            continue

        label, operation = action
        if operation is None:
            print("Exiting...")
            break

        operation.execute()

if __name__ == "__main__":
    main()