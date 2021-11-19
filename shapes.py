from abc import ABC, abstractmethod
class Shape():
    
    def _init_ (self):
        self.sides = 0.0
        self.length = 0.0

    def perimiter(self):
        return self.sides * self.length 
       
    @abstractmethod
    def area():
        pass  

class Square(Shape):
          

    def __init__(self,length):
        self.sides = 4
        self.lenght = length

    def area(self):
        return self.length * self.length

class Triangle(Shape):
  

    def __init__(self, length, height):
        self.sides = 3
        self.length = length
        self.height = height 

    def area(self):
        return 0.5 * self.length * self.height

print(Square.perimiter(2))
print(Square.area(2))
print(Triangle.perimiter(2))
print(Triangle.area(2))         