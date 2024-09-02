class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.slope = (y2-y1)/(x2 - x1)
        self.yinter = y2 - ((self.slope)*x2)

    def contains(self, x, y):
        if x < self.x1 or x > self.x2 or y < self.y1 or y > self.y2:
           return False
        return y == (self.slope * x) + self.yinter
    
    def get_distance(self):
        dis = (((self.x2 - self.x1)**2) + (self.y2 - self.y1)**2)**0.5
        return dis
    
    def get_x1(self):
        return self.x1
    
    def get_y1(self):
        return self.y1
    
    def get_x2(self):
        return self.x2
    
    def get_y2(self):
        return self.y2

    def get_y(self, x):
        y = (self.slope * x) + self.yinter
        if x < self.x1 or x > self.x2 or y < self.y1 or y > self.y2:
            return -999.999
        return y
    


class Point:
  # Constuctor
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  def is_on_x_axis(self):
    if self.__y == 0: return True
    else: return False

  def is_on_y_axis(self):
    if self.__x == 0: return True
    else: return False

  def translate(self, dist_x, dist_y):
    self.__x = self.__x + dist_x
    self.__y = self.__y + dist_y

  def get_x(self):
    return self.__x

  def get_y(self):
    return self.__y

  def set_x(self, new_x):
    self.__x = new_x

  def set_y(self, new_y):
    self.__y = new_y

  def __str__(self):
    return f"({self.__x}, {self.__y})"

  def __eq__(self, other):
    return self.__x == other.__x and self.__y == other.__y
  


x1 = float(input("Enter x1 : "))
y1 = float(input("Enter y1 : "))
x2 = float(input("Enter x2 : "))
y2 = float(input("Enter y2 : "))
a = Line(x1,y1,x2,y2)
print(f'value of x1 on this line is {a.get_x1():.3f}')
print(f'value of x2 on this line is {a.get_x2():.3f}')
print(f'value of y1 on this line is {a.get_y1():.3f}')
print(f'value of y2 on this line is {a.get_y2():.3f}')
print('==========')
print('Check x and y are on this line ?')
check_x = float(input('Enter x : '))
check_y = float(input('Enter y : '))
if a.contains(check_x,check_y):
   print(f'x = {check_x:.3f} and y = {check_y:.3f} are on this line')
else:
   print(f'x = {check_x:.3f} and y = {check_y:.3f} are not on this line')
print(f'Distance between startPoint and endPoint is {a.get_distance():.3f}')
print('==========')
print('Find value of y that gives( x , y ) on this line')
x_value = float(input('Enter x : '))
y_value = a.get_y(x_value)
print(f'value of y is {y_value:.3f}')
if a.contains(x_value,y_value):
   print(f'( x , y ) = ( {x_value:.3f} , {y_value:.3f} ) on this line')
else:
   print(f'( x , y ) = ( {x_value:.3f} , {y_value:.3f} ) is not on this line')