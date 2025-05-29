class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.semesters = {}  # key = sem number, value = list of subject results (True for pass, False for fail)

    def add_semester_results(self, sem_number, results):
        self.semesters[sem_number] = results

    def is_semester_passed(self, sem_number):
        if sem_number in self.semesters:
            return all(self.semesters[sem_number])
        return False

    def has_graduated(self):
        for sem in range(1, 9):
            if sem not in self.semesters or not all(self.semesters[sem]):
                return False
        return True

    def can_promote(self):
        current_sem = len(self.semesters)
        if current_sem == 0:
            return True
        return self.is_semester_passed(current_sem)

    def update_result(self, sem_number, new_results):
        self.semesters[sem_number] = new_results

    def display_details(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")
        for sem, results in self.semesters.items():
            status = "Passed" if all(results) else "Failed"
            print(f"  Semester {sem}: {status}")
        if self.has_graduated():
            print("Status: Graduated")
        elif self.can_promote():
            print("Status: Promoted to Next Semester")
        else:
            print("Status: Reappear in Current Semester")

    def get_details_text(self):
        text = f"Name: {self.name}, Roll No: {self.roll_no}\n"
        for sem, results in self.semesters.items():
            status = "Passed" if all(results) else "Failed"
            text += f"  Semester {sem}: {status}\n"
        if self.has_graduated():
            text += "Status: Graduated\n"
        elif self.can_promote():
            text += "Status: Promoted to Next Semester\n"
        else:
            text += "Status: Reappear in Current Semester\n"
        return text


# Input 4 students
students = []

for i in range(4):
    name = input(f"Enter name of student {i+1}: ")
    roll_no = input(f"Enter roll number of student {i+1}: ")
    student = Student(name, roll_no)

    num_sems = int(input(f"Enter number of semesters completed by {name}: "))
    for s in range(1, num_sems + 1):
        subjects = int(input(f"  Enter number of subjects in Semester {s}: "))
        results = []
        for subj in range(subjects):
            res = input(f"    Subject {subj+1} (pass/fail): ").lower()
            results.append(res == "pass")
        student.add_semester_results(s, results)

    students.append(student)

# Save output to text file
with open("student_results.txt", "w") as f:
    for student in students:
        f.write(student.get_details_text() + "\n")

print("\n--- Student Details Saved in 'student_results.txt' ---\n")

# View and Update Menu
def view_update_menu():
    while True:
        choice = input("\nOptions: [1] View Details [2] Update Results [3] Exit: ")
        if choice == "1":
            for student in students:
                print("\n------------------")
                student.display_details()
        elif choice == "2":
            roll_no = input("Enter roll number to update: ")
            for student in students:
                if student.roll_no == roll_no:
                    sem = int(input("Enter semester number to update: "))
                    num_sub = int(input("Enter number of subjects: "))
                    new_results = []
                    for n in range(num_sub):
                        result = input(f"  Subject {n+1} result (pass/fail): ").lower()
                        new_results.append(result == "pass")
                    student.update_result(sem, new_results)
                    print("Updated successfully.")
                    break
            else:
                print("Student not found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

view_update_menu()
