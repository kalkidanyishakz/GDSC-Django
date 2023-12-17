                
#kalkidan yishak
class User:
    def __init__(self, name):
        self.name=name
    

class Teacher:
    def __init__(self, name , subject):
        super().__init__(name)
        self.name=name
        self.subject=subject
                   
class Course:
    def __init__(self, course_name, course_code, teacher):
        self.course_name=course_name
        self.course_code=course_code
        self.teacher=teacher
        self.courses=[]

    def __repr__(self):
        return f"course name {self.course_name} course code {self.course_code} teacher{self.teacher}"
    
    def add(self, course):
        if isinstance(course, Course):
            self.courses.append(course)
        

math=Course('math', '0223', 'admasu')
teacher1=Teacher('alamrew',math)        
math.display()

class Student(User):
    student_list=[]
    def __init__(self,  name, grade, age):
        assert type(age)==int, 'age should be integer'
        super().__init__(name)
        self.grade=grade
        self.age=age
        Student.student_list.append(self)
    
    def display_data(self):
        print(f"name: {self.name}\nage:{self.age}\ngrade:{self.grade}")
    
    def display_all():
        for student in Student.student_list:
            print(f"name: {student.name}\nage:{student.age}\ngrade:{student.grade}")

student1=Student('kal', 3, 21)
student1.display_data()
