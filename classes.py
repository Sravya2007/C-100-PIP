class Student(object):
    def __init__(self, name, age, gender, level, grades = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades
    def setGrade(self, course, grade):
        self.grades[course] = grade
    def getGrade(self, course):
        return self.grades[course]
    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)
john = Student("John", 12, "male", 6, {"Math": 3.3})
sravya = Student("Sravya", 14, "female", 9, {"Science": 9})
print(john.getGPA())
print(sravya.getGPA())