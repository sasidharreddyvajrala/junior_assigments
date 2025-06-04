class Student:
    def __init__(self, name, department, rollno, joining_year, college_name):
        self.name = name
        self.department = department
        self.rollno = rollno
        self.joining_year = joining_year
        self.college_name = college_name
        self.year_results = {}  # Stores {year: (marks, result)}

    def add_year_result(self, year, marks):
        result = "Pass" if marks >= 40 else "Fail"
        self.year_results[year] = (marks, result)

    def check_graduation_status(self):
        return "You are graduated" if all(res[1] == "Pass" for res in self.year_results.values()) else "You have failed"

    def __str__(self):
        result_lines = [f"Year {year}: Marks = {marks}, Result = {result}"
                        for year, (marks, result) in self.year_results.items()]
        return (
            f"Name: {self.name}\n"
            f"Roll No: {self.rollno}\n"
            f"Department: {self.department}\n"
            f"College: {self.college_name}\n"
            f"Joining Year: {self.joining_year}\n"
            + "\n".join(result_lines) + f"\nFinal Status: {self.check_graduation_status()}\n"
            + "-" * 40
        )


def get_student_details():
    name = input("Enter student name: ")
    department = input("Enter department: ")
    rollno = input("Enter roll number: ")
    joining_year = int(input("Enter college joining year (e.g. 2020): "))
    college_name = input("Enter college name: ")
    return Student(name, department, rollno, joining_year, college_name)


#  all students details first
students = []
num_students = 4

for i in range(num_students):
    print(f"\n--- Enter details for student {i + 1} ---")
    student = get_student_details()
    students.append(student)

# enter marks year-wise for all students, year by year
for year_offset in range(4):  # 0 to  4 years
    print(f"\n--- Enter marks for Year {year_offset + 1} for all students ---")
    for student in students:
        year = student.joining_year + year_offset
        while True:
            try:
                marks = float(input(f"Enter marks for {student.name} (Roll No: {student.rollno}) for year {year} (0-100): "))
                if 0 <= marks <= 100:
                    student.add_year_result(year, marks)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter numeric marks.")


with open("student_results.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

print("\nAll student results with marks have been saved to 'student_results.txt'.")
