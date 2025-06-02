class Student:
    def __init__(self, name, roll_no,department,clgname):
        self.name = name
        self.roll_no = roll_no
        self.department=department
        self.clgname=clgname
        self.semesters = {}  # key = sem number, value = list of subject results (True for pass, False for fail)

    def semester_results(self, sem_number, results):
        self.semesters[sem_number] = results

    def semester_passed(self, sem_number):
        if sem_number in self.semesters:
            return all(self.semesters[sem_number])
        return False

    def graduated(self):
        for sem in range(1, 9):
            if sem not in self.semesters or not all(self.semesters[sem]):
                return False
        return True

    def promote(self):
        current_sem = len(self.semesters)
        if current_sem == 0:
            return True
        return self.semester_passed(current_sem)

    def update_result(self, sem_number, new_results):
        self.semesters[sem_number] = new_results
    



    