
class Student:
    def __init__(self,name,age, grade):
        self.name = name 
        self.age = age 
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
    
class Course:
    def __init__(self,name,max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []
    def add_student(self,student):
        if len(self.students) <  self.max_students:
            self.students.append(student)
            return True 
        return False
    
    def get_avg_grade(self):
        value =  0 
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)    
s1 = Student('Vanessa',21,90.5)
s2 = Student('Eli',23,79.6)
s3 = Student('Jay',20,96.7)

c1 = Course('IT',20)
print(c1.add_student(s1))
print(c1.add_student(s2))
print(c1.add_student(s3))
print(c1.students[0].name)
print(c1.get_avg_grade())

'''Static methods --> A method that belong to a class rather than any object from that
                      class instance usually used for general utility functions.
                      
Instance methods --> Best for operations on instance of the class(object)
static methods --> Best for utility functions that do not need access to class data                                                               
'''
class Employee:
    def __init__(self, name, position):
        self.name = name 
        self.position = position 
    #Instance method   
    def get_details(self):
        return f"{self.name} {self.position}"
    
    @staticmethod
    def is_valid_pos(position):
        valid_pos = ['CEO','Manager','Assintant Manager','Secretary','Clerk']
        return position in valid_pos
    
print(Employee.is_valid_pos('Manager'))

'''class method ---> Allow operations related to the class itself
                     Takes (cls)as the first parameter'''
                     
class Student:
    count = 0 
    total_gpa = 0
    def __init__(self,name,GPA):
        self.name = name 
        self.GPA = GPA
        Student.count += 1 
        Student.total_gpa += float(GPA)
    #Instance method    
    def get_info(self):
        return f"{self.name} {self.GPA}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students is {cls.count}"
    
    @classmethod
    def avarage_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Avarag GPA is: {cls.total_gpa / cls.count}"
    
s1 = Student('Mel', 4.5)
s2 = Student('Seth', 4.0)
s3 = Student('Yoshi', 3.9)
s4 = Student('Rags', 3.0)
s5 = Student('Steph', 2.5)

print(s2.get_info())
print(Student.get_count())
print(Student.avarage_gpa())


    
    
    
    
                      
                      

            
        