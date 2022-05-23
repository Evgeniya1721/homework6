lecturers_list = []
students_list = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def avg_grade(self):
        overall_grade = 0
        grades_count = 0
        if len(self.grades) == 0:
            return 0
        else:
            for grades in self.grades.values():
                if len(grades) > 0:
                    for grade in grades:
                        overall_grade += grade
                        grades_count += 1
            return overall_grade / grades_count

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course_name, grade):
        if isinstance(lecturer, Lecturer) and course_name in \
                self.courses_in_progress and course_name in \
                lecturer.courses_attached and 1 <= grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Mistake'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {round(self.avg_grade(), 2)}\n' \
               f'Курсы в процессе изучения: {", ".join(map(str, self.courses_in_progress))}\n' \
               f'Завершенные курсы: {", ".join(map(str, self.finished_courses))}'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() < other.avg_grade()
        else:
            return 'Mistake'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        lecturers_list.append(self)

    def avg_grade(self):
        overall_grade = 0
        if len(self.grades) > 0:
            for grade in self.grades:
                overall_grade += grade
            return overall_grade / len(self.grades)
        else:
            return 0

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        else:
            return 'Mistake'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(self.avg_grade(), 2)}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in \
                self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Mistake'


def avg_grade_all_lecturers(lecturers_list, course_name):
    all_lecturers_avg_grade = 0
    lecturers_count = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in \
                lecturer.courses_attached:
            all_lecturers_avg_grade += lecturer.avg_grade()
            lecturers_count += 1
    if lecturers_count == 0:
        return 'Mistake'
    return round(all_lecturers_avg_grade / lecturers_count, 2)


def avg_grade_all_students(students_list, course_name):
    all_students_avg_grade = 0
    students_count = 0
    for student in students_list:
        if isinstance(student, Student) and course_name in \
                student.courses_in_progress:
            all_students_avg_grade += student.avg_grade()
            students_count += 1
    if students_count == 0:
        return 'Mistake'
    return round(all_students_avg_grade / students_count, 2)


successful_student = Student('Capitan', 'America', 'male')
successful_student.courses_in_progress += ['C++']
successful_student.finished_courses += ['Java']
successful_student.add_courses('Introduction to programming')

failing_student = Student('Iron', 'Man', 'male')
failing_student.courses_in_progress += ['C++']
failing_student.finished_courses += ['Java']
failing_student.add_courses('Introduction to programming')

cool_reviewer = Reviewer('Stan', 'Lee')
cool_reviewer.courses_attached += ['C++']
cool_reviewer.courses_attached += ['Java']

cool_reviewer = Reviewer('Jack', 'Kirby')
cool_reviewer.courses_attached += ['C++']
cool_reviewer.courses_attached += ['Java']

cool_reviewer.rate_hw(successful_student, 'C++', 8)
cool_reviewer.rate_hw(successful_student, 'C++', 9)
cool_reviewer.rate_hw(successful_student, 'C++', 9)
cool_reviewer.rate_hw(successful_student, 'Java', 7)
cool_reviewer.rate_hw(successful_student, 'Java', 10)
cool_reviewer.rate_hw(successful_student, 'Java', 8)

cool_reviewer.rate_hw(failing_student, 'Java', 9)
cool_reviewer.rate_hw(failing_student, 'Java', 9)
cool_reviewer.rate_hw(failing_student, 'Java', 9)
cool_reviewer.rate_hw(failing_student, 'C++', 7)
cool_reviewer.rate_hw(failing_student, 'C++', 9)
cool_reviewer.rate_hw(failing_student, 'C++', 6)

cool_lecturer = Lecturer('Kurt', 'Busiek')
cool_lecturer.courses_attached += ['C++']
lecturers_list.append(cool_lecturer)

def_lecturer = Lecturer('Roger', 'Stern')
def_lecturer.courses_attached += ['C++']
lecturers_list.append(def_lecturer)

successful_student.rate_lecturer(cool_lecturer, 'C++', 10)
successful_student.rate_lecturer(cool_lecturer, 'C++', 8)
successful_student.rate_lecturer(cool_lecturer, 'C++', 9)

failing_student.rate_lecturer(def_lecturer, 'C++', 9)
failing_student.rate_lecturer(def_lecturer, 'C++', 7)
failing_student.rate_lecturer(def_lecturer, 'C++', 8)

print('Лекторы:')
print(cool_lecturer)
print()
print('Проверяющие:')
print(cool_reviewer)
print()
print('Студенты:')
print(successful_student)
print()
print('Средняя оценка лекторов:')
print(avg_grade_all_lecturers(lecturers_list, 'C++'))
print()
print('Средняя оценка студентов:')
print(avg_grade_all_students(students_list, 'C++'))


