# повторное прохождение занятия, на след день, с прописью ручками
import dataclasses


@dataclasses.dataclass
class Student:
    name: str
    surname: str
# class StudentsIterator:
#
#     def __init__(self, students: list):
#         self.__index = 0
#         self.__students = students
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__index < len(self.__students):
#             student = self.__students[self.__index]
#             self.__index += 1
#             return student
#         else:
#             raise StopIteration


class Group:
    def __init__(self, name: str):
        self.name = name
        self.__students = []

    def add_student(self, student: Student):
        self.__students.append(student)

    def __iter__(self):
       return iter(self.__students)


if __name__ == '__main__':
    group = Group('Group1')
    group.add_student(Student('Joe', 'Smith'))
    group.add_student(Student('Roi', 'Jones'))
    group.add_student(Student('Eddy', 'Stoun'))
    group.add_student(Student('Ed2', 'St1111n'))
    group.add_student(Student('E34y', 'St34un'))

    for student in group:
        print(student)
