## IMPORTS
import math
from random import randint

## CLASSES
class Point():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def is_in_rectangle(self, rectangle):
        if rectangle.lower_left.x < self.x < rectangle.upper_right.x \
            and rectangle.lower_left.y < self.y < rectangle.upper_right.y:
            return True
        else:
            return False
        
    def distance(self,point):
        distance = math.sqrt( (self.x - point.x)**2 + (self.y - point.y)**2 )
            
        return distance
        
    def __str__(self):
        pass
    
    
class Rectangle():
    
    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right
        
        width = self.lower_left.x - self.upper_right.x
        lenght = self.lower_left.y - self.upper_right.y
        self.area = width*lenght
    
    def guess_area(self,area):
        if area == self.area:
            return True
        else:
            return False

## INTERFACE
# Create rectangle and display coordinates
rectangle = Rectangle( Point(randint(0,9),randint(0,9)), Point(randint(10,19),randint(10,19)) )
print(f"Ractangle Coordinates: {rectangle.lower_left.x}, {rectangle.lower_left.y} and {rectangle.upper_right.x}, {rectangle.upper_right.y}")

# User guess: point in rectangle
user_point = Point(float(input("Guess X: ")),float(input("Guess Y: ")))
print("Your point was inside rectangle:", user_point.is_in_rectangle(rectangle))

# User guess: area
user_area = float(input("Guess rectangle area: "))
print("Area guessed correctly? ", rectangle.guess_area(user_area), ". Rectangle area is:", rectangle.area)
if not rectangle.guess_area(user_area):
    print("Your area was off by:", rectangle.area - user_area)
