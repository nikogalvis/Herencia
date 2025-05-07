class Point:
  
  definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
  def __init__(self, x: float=0, y: float=0):
    self.x = x
    self.y = y
  def move(self, new_x: float, new_y: float):
    self.x = new_x
    self.y = new_y
  def reset(self):
    self.x = 0
    self.y = 0

class Line:
   def __init__(self, start: Point = Point(0,0), end: Point = Point(0,0)):
      self.start = start
      self.end = end  
   
class Rectangle:
    def __init__(self, width: float = 0, height: float = 0,  center: Point = Point(0,0)):
        self.width = width
        self.height = height
        self.center = center
    
    def top_right(self):
       return (self.center.x+(self.width)/2, self.center.y+(self.height/2))
    
    def top_left(self):
       return (self.center.x-(self.width)/2, self.center.y+(self.height/2))
    
    def bottom_left(self):
       return (self.center.x-(self.width)/2, self.center.y-(self.height/2))
    
    def bottom_right(self):
       return (self.center.x+(self.width)/2, self.center.y-(self.height/2))
    
    def method(self):
       return ((f"Top right Point {self.top_right()}"),
               (f"Top left Point {self.top_left()}"),
               (f"Bottom left Point {self.bottom_left()}"),
               (f"Bottom Right Point{self.bottom_right()}"))
    
    def init(self):
        for i in self.method():
          print(i)
    
    def compute_area(self):
       return self.width*self.height
    
    def compute_perimeter(self):
       return 2*(self.width + self.height)
    
    def compute_interference_point(self, point: Point):
       (min_x, max_y)= self.top_left()
       (max_x, min_y)= self.bottom_right()
       return ((min_x < point.x < max_x)and
               (min_y < point.y < max_y))
    
    def compute_interference_line(self, line: Line):
       return (self.compute_interference_point(line.start) or self.compute_interference_point(line.end))
    
data_1 = Rectangle(width = 4, height = 7, center = Point(0,0))

class Square(Rectangle):
  def __init__(self, edge: float = 0, center: Point = Point(0,0)):
     super().__init__(width = edge, height = edge, center = center)
     self.edge = edge

data_2 = Square(edge = 8, center = Point(0,0))
data_3 = Point(5,4)
data_2.init()
data_4 = Line(start = Point(2,0),end = Point(0,2))
print(data_2.compute_interference_line(data_4))
