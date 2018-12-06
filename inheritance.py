# od CodeCademy

"""
*** CLASSES ***

Initializing a class
There is a special function named __init__() that gets called 
whenever we create a new instance of a class. 
It exists by default, even though we don't see it. 
However, we can define our own __init__() function inside the class, 
overwriting the default version. We might want to do this in order 
to provide more input variables, just like we would with any other function.

The first argument passed to __init__() must always 
be the keyword self - this is how the object keeps track 
of itself internally - but we can pass additional variables after that.

In order to assign a variable to the class (creating a member variable), we use dot notation.
For instance, if we passed newVariable into our class, inside the __init__() function we would say:
self.new_variable = new_variable




# We also use the word object in parentheses because we want
# our classes to inherit the object class. 
# This means that our class has all the properties of an object, 
# which is the simplest, most basic class. 
# Later we'll see that classes can inherit other, more complicated classes.

"""

# Pr 1

print "Primer 1"
class Customer(object):
  # pass
  # pass se koristi koga sakas da ja deklariras klasata i da kazes deka
  # klasava (ili metod na klasata/nekoja funkcija) ke se dospecificira podocna
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
print
print

# Pr 2

print "Primer 2"
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
    
triag = Triangle("a", "b", "c")
print triag.side1
triag.number_of_sides = 3
print triag.number_of_sides
print
print

# Pr 3 (override)

print "Primer 3"
class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!
print
print


# Pr 4 (override)
# povik na metod od base class (parent or superclass)
# vo derived class (subclass)

print "Primer 4"

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)
print
print


# Pr 5

print "Primer 5"

class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False

my_triangle = Triangle(30, 60, 90)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle

print
print


# Pr 6

print "Primer 6"

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
    
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

# my_car.display_car()
print my_car.condition
my_car.drive_car()
print my_car.condition

class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg = mpg
    self.battery_type = battery_type
    
  def drive_car(self):
    self.condition = "like new"
    
my_car = ElectricCar("Tesla", "red", 999, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition
print
print


# Pr 7

"""One useful class method to override is the built-in __repr__() method, 
which is short for representation; by providing a return value in this method, 
we can tell Python how to represent an object of our class (for instance, when using a print statement)."""

print "Primer 7"

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)
print my_point