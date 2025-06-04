import sys
import os

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

class AddTask:
    def __init__(self, task_list:TaskList):
        self.task_list = task_list
    def add(self):
        title = input("Enter title: ")
        desc = input("Enter description: ")
        for task in self.task_list.tasks:
            if task.title == title:
                print(f"Task '{title}' already exists.")
                return
        new_task = Task(title, desc)
        self.task_list.tasks.append(new_task)
        print(f"Task '{title}' added.")

class DeleteTask:
    def __init__(self,task_list:TaskList):
        self.task_list = task_list
    def delete(self):
        title = input("Enter title: ")
        for task in self.task_list.tasks:
            if task.title == title:
                self.task_list.tasks.remove(task)
                print(f"Task '{title}' deleted.")
                return
        print("Task not found.")

class CompleteTask:
    def __init__(self,task_list:TaskList):
        self.task_list = task_list
    def complete(self):
        title = input("Enter title: ")
        for task in self.task_list.tasks:
            if task.title == title:
                task.mark_complete()
                return
        
        print("Task not found")


class ShowTasks:
    def __init__(self,task_list:TaskList):
        self.task_list = task_list
    def show(self):
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
            print("no file found at location.")
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


class TaskSaver:
    def __init__(self,filepath):
        self.filepath = filepath
    def save_tasks(self,task_list):
        with open(self.filepath,'w') as file:
            for task in task_list.tasks:
                file.write(f'{task.title} | {task.description} | {task.status}\n')
        print(f"tasks saved to {self.filepath}")


def display_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Mark as Complete")
    print("5. Save Tasks")
    print("6. Exit")

def main():
    task_file = "task_list.txt"
    task_list = TaskList()

    loader = TaskLoader(task_file)
    saver = TaskSaver(task_file)

    loader.load_tasks(task_list)

    add_task = AddTask(task_list)
    delete_task = DeleteTask(task_list)
    complete_task = CompleteTask(task_list)
    show_task = ShowTasks(task_list)

    while True:
        display_menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            add_task.add()
        elif choice == 2:
            show_task.show()
        elif choice == 3:
            delete_task.delete()
        elif choice == 4:
            complete_task.complete()
        elif choice == 5:
            saver.save_tasks(task_list)
        elif choice == 6:
            sys.exit()
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()