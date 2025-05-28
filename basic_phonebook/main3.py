class College:
    def __init__(self, name, id, college_name, department, joining_year):
        self.name = name
        self.id = id
        self.college_name = college_name
        self.department = department
        self.joining_year = joining_year
        self.semesters = {} 

    def add_semester_result(self, semester_number, status):
        self.semesters[semester_number] = status

    def calculate_percentage(self):
        if not self.semesters:
            return 0
        total = len(self.semesters)
        passed = sum(1 for result in self.semesters.values() if result)
        return (passed / total) * 100

    def view_details(self):
        print("\n--- Student Details ---")
        print(f"Name        : {self.name}")
        print(f"ID          : {self.id}")
        print(f"College     : {self.college_name}")
        print(f"Department  : {self.department}")
        print(f"Joining Year: {self.joining_year}")

        choice=input("enter ")

