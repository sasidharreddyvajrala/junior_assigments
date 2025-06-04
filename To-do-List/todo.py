from datetime import date
import sys
class task:
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

    
class task_list:
    def __init__(self):
        self.tasks = []

    def add_task(self,new_task:task):
        for task in self.tasks:
            if new_task.title == task.title:
                print('task already exists')
                return
        self.tasks.append(new_task)
        print(f'Task {new_task.title} added')
    def show_list(self):
        if not self.tasks:
            print("List is empty")
            return
        
        print("\n----TASKS----")
        for i,task in enumerate(self.tasks):
            print(f'{i+1} {task.title} {task.status}')
    def delete_task(self,title:str):
        task_found = False
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                task_found = True
                print("task deleted")
                break
        if not task_found:
            print("Task not found")
    def mark_as_completed(self,title:str):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        print("Task not found")
        return False
    



    

class CLI:
    def __init__(self, my_tasks:task_list):
        self.my_tasks = task_list
    def display_menu(self):
        print('---To-Do-List---\n')
        print('1.Add Task')
        print('2.Show list')
        print('3.Delete Task')
        print('4.Mark as Complete')
        print('5.Exit')
    def run(self):
        
        while True:
            self.display_menu()
            choice = int(input("Enter your choice:"))
            if choice == 1:
                print("---Add Task---\n")
                title = input("Enter title: ")
                description = input("Enter description: ")
                new_task = task(title,description)
                self.my_tasks.add_task(new_task)
            elif choice == 2:
                self.my_tasks.show_list()
            elif choice == 3:
                title = input("Enter title :")
                self.my_tasks.delete_task(title)
            elif choice == 4:
                title = input("Enter title: ")
                self.my_tasks.mark_as_completed(title)
            elif choice == 5:
                print("Exiting")
                sys.exit()
            else:
                print("Invalid choice")
    


if __name__ == '__main__':
    my_tasks = task_list()
    cli = CLI(my_tasks)
    cli.run()