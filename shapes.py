#A Circle instance accepts attribute radius (r)
class Circle:
    def __init__(self,radius):
        self.r = radius

#Area (A) of a circle using the formula A=πr2
    def area(self):
        pi = 3.14
        result = pi * self.r * self.r
        return f"The area of the given circle is, {result}."
   
#Circumference (c) using the formula C=2πr
    def circumference(self):
        pi = 3.14
        result = 2 * pi * self.r
        return f"The circumference of the given circle is, {result}."

circle = Circle(3)
print(circle.area())
print(circle.circumference())

#A Square instance accepts the attribute side (a)
class Square:
    def __init__(self,side):
        self.a = side

#Area (A) of the square using the formula A=a2
    def area(self):
        result = self.a * self.a
        return f"The area of the given square is, {result}."

#Perimeter (P) of the square using the formula P=4a
    def perimeter(self):
        result = 4 * self.a
        return f"The perimeter of the given square is, {result}."

square = Square(3)
print(square.area())
print(square.perimeter())

#A Rectangle instance accepts two sides of a rectangle (w,l)
class Rectangle:
    def __init__(self,width,length):
        self.w = width
        self.l = length

#Area (A) of the rectangle using the formula A=wl
    def area(self):
        result = self.w * self.l
        return f"The area of the given rectangle is, {result}."

#Perimeter (P) of the rectangle using the formula P=2(l+w)
    def perimeter(self):
        result = 2 * (self.w + self.l)
        return f"The perimeter of the given rectangle is, {result}."

rectangle = Rectangle(3, 2)
print(rectangle.area())
print(rectangle.perimeter())

#A Sphere Instance accepts the radius of the sphere (r)
class Sphere:
    def __init__(self, radius):
        self.r = radius

#Surface Area (A) using the formula A=4πr2
    def surface_area(self):
        pi = 3.14
        result = 4 * pi * (self.r * self.r)
        return f"The surface area of the given sphere is, {result}."

#Volume (V) of the sphere using the formula V = 4/3(πr3)
    def volume(self):
        pi = 3.14
        result = 4/3 * (pi * (self.r ** 3))
        return f"The volume of the given sphere is, {result}."

sphere = Sphere(5)
print(sphere.surface_area())
print(sphere.volume())
