"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

    def add_subject(self, subject, grade):
        self.subjects.update({subject: grade})

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def view_subjects(self):
        print(f"{self.name}'s subject are {self.subjects}")

    def get_overall_mark(self): #Use average
        avg_mark = sum(self.subjects.values()) / len(self.subjects)
        print(f"Your average mark is {round(avg_mark,1)}%")
        return avg_mark

    def update_grade(self, subject, grade):
        self.subjects.update({subject: grade})


class CFGStudent (Student):

    def __init__(self, name, age, id, specialization):
        super().__init__(name, age, id)
        self.specialization = specialization


student_1 = CFGStudent(name= 'Nana', age=23, id=1234, specialization='Software')

student_1.add_subject('Dictionaries', 90)
student_1.add_subject('Lists', 78)
student_1.add_subject('Python', 100)
student_1.view_subjects()

student_1.get_overall_mark()

student_1.remove_subject('Lists')
student_1.view_subjects()