class Student:
    def __init__(self, name, rollno, department, college, joining_year, year_status):
        self.name = name
        self.rollno = rollno
        self.department = department
        self.college = college
        self.joining_year = int(joining_year)
        self.year_status = year_status  # list of 4 strings: "pass"/"fail"

    def graduated(self):
        return all(y.lower() == "pass" for y in self.year_status)

    def to_line(self):
        return f"{self.name},{self.rollno},{self.department},{self.college},{self.joining_year},{';'.join(self.year_status)}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(",")
        name, rollno, department, college, joining_year, year_data = parts
        year_status = year_data.split(";")
        return Student(name, rollno, department, college, joining_year, year_status)


FILENAME = "students.txt"

def create_student():
    name = input("Enter name: ")
    rollno = input("Enter roll number: ")
    department = input("Enter department: ")
    college = input("Enter college: ")
    joining_year = input("Enter joining year: ")

    print("Enter result for each academic year (pass/fail):")
    year_status = []
    for i in range(4):
        status = input(f"Year {i + 1} ({int(joining_year) + i}): ")
        year_status.append(status)

    student = Student(name, rollno, department, college, joining_year, year_status)
    with open(FILENAME, "a") as f:
        f.write(student.to_line())
    print("Student added.\n")


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
                for i, status in enumerate(student.year_status):
                    print(f"Year {i + 1} ({student.joining_year + i}): {status}")
                print(f"Status: {'Graduated' if student.graduated() else 'Not Graduated'}\n")
                found = True
                break
    if not found:
        print("Student not found.\n")


# Main menu
if __name__ == "__main__":
    for _ in range(4):
        create_student()  # Collect 4 students first

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
