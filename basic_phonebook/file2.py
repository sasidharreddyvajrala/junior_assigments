class Student:
    def __init__(self, name, rollno, department, college, joining_year, semesters):
        self.name = name
        self.rollno = rollno
        self.department = department
        self.college = college
        self.joining_year = joining_year
        self.semesters = semesters

    def graduated(self):
        return all(s.lower() == "pass" for s in self.semesters)

    def to_line(self):
        return f"{self.name},{self.rollno},{self.department},{self.college},{self.joining_year},{';'.join(self.semesters)}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(",")
        name, rollno, department, college, joining_year, sem_data = parts
        semesters = sem_data.split(";")
        return Student(name, rollno, department, college, joining_year, semesters)


FILENAME = "students.txt"

def create_student():
    name = input("Enter name: ")
    
    rollno = input("Enter roll number: ")
    department = input("Enter department: ")
    college = input("Enter college: ")
    joining_year = input("Enter joining year: ")
    n = int(input("Number of semesters completed: "))
    semesters = [input(f"Result of semester {i+1} (pass/fail): ") for i in range(n)]
    student = Student(name, rollno, department, college, joining_year, semesters)
    print('student added')
    with open(FILENAME, "a") as f:
        f.write(student.to_line())
    #print("Student added.\n")
  


def view_student():
    rollno = input("Enter roll number to view: ")
    found = False
    with open(FILENAME, "r") as f:
        for line in f:
            student = Student.from_line(line)
            if student.rollno == rollno:
                print(f"\nName: {student.name}")
                print(f"Roll No: {student.rollno}")
                print(f"Department: {student.department}")
                print(f"College: {student.college}")
                print(f"Joining Year: {student.joining_year}")
                print(f"Semesters: {student.semesters}")

                print(f"Status: {'Graduated' if student.is_graduated() else 'Not Graduated'}\n")
                found = True
                break
    if not found:
        print(" Student not found.\n")

 


  
# Main menu
while True:
    print("----- Student Management -----")
    print("1. Create Student")
    print("2. View Student")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice.\n")