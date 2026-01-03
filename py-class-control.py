class Person:
    def __init__(self, name, id):
        self.name=name
        self.id=id
    def get_info(self):
        return f"Name={self.name}, ID={self.id}"

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.__courses=[]
    def add_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)
    def remove_course(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
    def __add__(self, other):
        combined=Student(self.name, self.id)
        combined.__courses=list(set(self.__courses+other.__courses))
        return combined
    def get_info(self):
        return f"Name={self.name}, ID={self.id}, course={self.__courses}"
    
class School:
    def __init__(self):
        self.students=[]
    def add_student(self, student):
        self.students.append(student)
    def find_student(self, id):
        for student in self.students:
            if student.id==id:
                return student
        return None
