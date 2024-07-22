from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self ,name,age):
        self.name=name
        self.age=age
        pass


    @abstractmethod
    def display_info(self):
        pass


class Employee(Person):
    def __init__(self ,name,age,Employee_id,department):
        # super(Employee,self).__init__(name,age)
        Person.__init__(self,name,age)
        self.Employee_id=Employee_id
        self.department=department

    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.Employee_id)
        print(self.department)

    
class Student(Person):
    def __init__(self ,name,age,student_id,major):
        # super(Student,self).__init__(name,age)
        Person.__init__(self, name ,age)
        self.student_id=student_id
        self.major=major

    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.student_id)
        print(self.major)

    
class Intern(Employee,Student):
    def __init__(self, name, age,Employee_id,department,student_id,major):
        # super(Intern,self).__init__(name, age,Employee_id,department,student_id,major)      
        Employee.__init__(self, name ,age, Employee_id,department)
        Student.__init__(self, name ,age, student_id,major)

    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.student_id)
        print(self.major)
        print(self.Employee_id)
        print(self.department)

objEmployee=Employee("maria",22,"12345", "IT support")
objEmployee.display_info()
objStudent=Student("Ahmed",19,"54321", "CS")
objStudent.display_info()

objIntern=Intern("Nermeen",22,"12345","itsupport","30212","cs")
objIntern.display_info()

