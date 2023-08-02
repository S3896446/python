class Course:
    def __init__(self, course_id, teacher_name, max_students, standard_charge):
        self.course_id = course_id
        self.teacher_name = teacher_name
        self.students_enrolled = []
        self.max_students = max_students
        self.standard_charge = standard_charge
        self.income = 0
        self.cost_of_running = 0
        

    def add_student(self, student):
        if len(self.students_enrolled) < self.max_students:
            self.students_enrolled.append(student)
            self.income += self.standard_charge
            return True
        else:
            return False

    def __str__(self):
        return f"Course ID: {self.course_id}, Teacher: {self.teacher_name}, Enrolled Students: {len(self.students_enrolled)}, Max Students: {self.max_students}, Income: ${self.income}"


class CookingCourse(Course):
    def __init__(self, course_id, teacher_name, is_italian_cooking=True):
        if is_italian_cooking:
            standard_charge = 500
        else:
            standard_charge = 700
        super().__init__(course_id, teacher_name, max_students=10, standard_charge=standard_charge)

    def calculate_cost_of_running(self):
        return 1000


class SewingCourse(Course):
    def __init__(self, course_id, teacher_name):
        super().__init__(course_id, teacher_name, max_students=10, standard_charge=300)

    def calculate_cost_of_running(self):
        return len(self.students_enrolled) * 100


class WritingCourse(Course):
    def __init__(self, course_id, teacher_name, is_creative_writing=True):
        if is_creative_writing:
            standard_charge = 200
            cost_of_running = 800
        else:
            standard_charge = 200
            cost_of_running = 600

        super().__init__(course_id, teacher_name, max_students=15, standard_charge=standard_charge)
        self.cost_of_running = cost_of_running


if __name__ == "__main__":
    cooking_course_1 = CookingCourse("001", "Chef John")
    cooking_course_2 = CookingCourse("002", "Chef Sarah", is_italian_cooking=False)
    sewing_course_1 = SewingCourse("003", "Alice")
    writing_course_1 = WritingCourse("004", "James")
    writing_course_2 = WritingCourse("005", "Emily", is_creative_writing=False)

    cooking_course_1.add_student("John Doe")
    cooking_course_2.add_student("Jane Smith")
    sewing_course_1.add_student("Bob Johnson")
    writing_course_1.add_student("Michael Brown")
    writing_course_2.add_student("Sophia Lee")
    

    print(cooking_course_1)
    
    print(cooking_course_2)
    print(sewing_course_1)
    print(writing_course_1)
    print(writing_course_2)
