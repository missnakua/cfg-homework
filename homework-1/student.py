from abc import ABC, abstractmethod

"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum, a student has a name, an age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""

class Student:

    def __init__(self, name, age, id, subjects, grade):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = subjects() # dict()
        self.grade = grade


    def get_grade(self, grade):
        return self.grade


    def add_subject(self, subjects):
        self.subjects.update(subjects)


    def remove_subject(self, subject):
        self.subjects.popitem({subject})


    def view_subjects(self):
        pass


    def overall_mark(self): #Use average
        pass


class Software(Student):
    pass


class DataScience(Student):
    pass

# bukky =
# chido =
# jess =
# michelle =
# lauren =
# odera =




# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method (and a new variable) to get student's overall mark (use average)

# class CFGStudent(Student):
#
#     def __init__(self, subject, grade):
#         super().__init__(subject="History", grade=98)
#
#     def add_subject(self, subject, grade=int):
#         self.subjects.update({subject:grade})
#         print(f"{subject} subject has been added to {self.subjects}")
#
# student1 = CFGStudent(name='Jess', age=23, id=1234, grade=88)
#
# student.add.subject('History', 78)
#
#
# print(student1)