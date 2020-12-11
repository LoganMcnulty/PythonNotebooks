"https://realpython.com/python-super/#:~:text=An%20Overview%20of%20Python's%20super()%20Function,-If%20you%20have&text=While%20the%20official%20documentation%20is,to%20call%20that%20superclass's%20methods."


# # Super() Basic Example

# +
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimiter(self):
        return 2 * self.length + 2 * self.width
    
    def tacos(self):
        print("I love tacos")
    
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        face_area = super().area()
        return face_area * self.length
    
    def phrase(self):
        self.phrase = 'The end is the beginning'
        return self.phrase
        

x = Rectangle(10, 5)
print(x.area())

y = Square(20)
print(y.perimiter())
y.tacos()

z = Cube(10)
print (z.area())
# Notice that even the cube technically has a "width" passed on from Rectangle
print(z.width)


# -

# # Super() Deep Dive

# +
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print("Calculating rectangle area...")
        return self.length * self.width
    
    def perimiter(self):
        return 2 * self.length + 2 * self.width
    
    def tacos(self):
        print("I love tacos")
    
class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)
        
    def area(self):
        print("Calculating square area...")
        return self.length**2
        
# notice in volume() here that Square is the subclass argument passed to super(), instead of Cube
# This causes Super() to search for the "area()" method one level above Square, i.e., rectangle
"""The parameterless call to super() is recommended and sufficient for most use cases, and needing to change the search hierarchy regularly could be indicative of a larger design issue."""

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length
        
x = Cube(10)
print(x.surface_area())
print(x.volume())
# -

# # Super() in multiple inheritance


