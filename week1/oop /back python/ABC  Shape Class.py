from abc import ABC, abstractmethod


class shape(ABC):
    def __init__():
        pass 

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def primenter(self):
        pass

class Rectangle(shape) :

    def __init__(self, width, height):
        self.width=width
        self.height=height

    def area(self):

        return self.width*self.height
    


    def primenter(self):
        return 2*(self.width+self.height)
    

    
class Circle(shape) :

    def __init__(self,reduis):
        self.reduis=reduis

    def area(self):
        return pow(self.reduis,2) *22/7


    def primenter(self):
        return 2*(self.reduis)*22/7
    



objRec= Rectangle(2,3)

print("Rectangle Area : ",objRec.area())
print("Rectangle primenter : ",objRec.primenter())


print("****************************************************")


objCir= Circle(3)

print("Circle Area : ",objCir.area())
print("Circle primenter : ",objCir.primenter())


    


