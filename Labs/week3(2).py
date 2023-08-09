class Course:
    def __init__(self, course_id, teacher_name, max_students, standard_charge):
        self.__course_id = course_id
        self.__teacher_name = teacher_name
        self.__students_enrolled = []
        self.__max_students = max_students
        self.__standard_charge = standard_charge
        self.__income = 0
        self.__cost_of_running = 0

    def add_student(self, student):
        if len(self.__students_enrolled) < self.__max_students:
            self.__students_enrolled.append(student)
            self.__income += self.__standard_charge
            return True
        else:
            return False

    # Getter for course_id
    def get_course_id(self):
        return self.__course_id

    # Getter for teacher_name
    def get_teacher_name(self):
        return self.__teacher_name

    # Getter for students_enrolled
    def get_students_enrolled(self):
        return self.__students_enrolled

    # Getter for max_students
    def get_max_students(self):
        return self.__max_students

    # Getter for standard_charge
    def get_standard_charge(self):
        return self.__standard_charge

    # Getter for income
    def get_income(self):
        return self.__income

    # Setter for standard_charge
    def set_standard_charge(self, new_standard_charge):
        self.__standard_charge = new_standard_charge

    def __str__(self):
        return f"Course ID: {self.__course_id}, Teacher: {self.__teacher_name}, Enrolled Students: {len(self.__students_enrolled)}, Max Students: {self.__max_students}, Income: ${self.__income}"


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
        return len(self.get_students_enrolled()) * 100


class WritingCourse(Course):
    def __init__(self, course_id, teacher_name, is_creative_writing=True):
        if is_creative_writing:
            standard_charge = 200
            cost_of_running = 800
        else:
            standard_charge = 200
            cost_of_running = 600

        super().__init__(course_id, teacher_name, max_students=15, standard_charge=standard_charge)
        self.__cost_of_running = cost_of_running

    # Getter for cost_of_running
    def get_cost_of_running(self):
        return self.__cost_of_running

    # Setter for cost_of_running
    def set_cost_of_running(self, new_cost_of_running):
        self.__cost_of_running = new_cost_of_running


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



    print(cooking_course_1)  # Output: Course ID: 001, Teacher: Chef John, Enrolled Students: 1, Max Students: 10, Income: $600
    print(cooking_course_2)
    print(sewing_course_1)
    print(writing_course_1)
    print(writing_course_2)
    
    
    
    
    
    # print(cooking_course_1.get_course_id())  # Output: 001
    # print(cooking_course_1.get_teacher_name())  # Output: Chef John
    # print(cooking_course_1.get_students_enrolled())  # Output: ['John Doe']
    # print(cooking_course_1.get_max_students())  # Output: 10
    # print(cooking_course_1.get_standard_charge())  # Output: 500
    # print(cooking_course_1.get_income())  # Output: 500

    # cooking_course_1.set_standard_charge(600)
    # print(cooking_course_1.get_standard_charge())  # Output: 600