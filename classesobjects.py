# Creating classes
class Employee:
    'Common base class for all employees'
    empCount = 0  # class variable

    def __init__(self, name, salary):  # constructor or initialization method
        # called when new instance of this class is created
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary


# Creating instance objects - using class name and pass in whatever arguments its __init__ method accepts
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

# Accessing attributes
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del emp1.age  # Delete 'age' attribute.

getattr(obj, name[, default])  # access the attribute of object
hasattr(obj, name)  # to check if an attribute exists or not (0/1)
setattr(obj, name, value)  # to set an attribute. If attribute does not exist, then it is created
delattr(obj, name)  # to delete an attribute

# Built-in attributes
__dict__  # Dictionary containing the class's namespace

__doc__  # Class documentation string or none, if undefined

__name__  # Class name

__module__  # Module name in which the class is defined. "__main__" in interactive mode

__bases__  # Possibly empty tuple containing the base classes, in the order of their occurrence in the base class list

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

# Destroying objects
a = 40      # Create object <40>
b = a       # Increase ref. count  of <40>
c = [b]     # Increase ref. count  of <40>

del a       # Decrease ref. count  of <40>
b = 100     # Decrease ref. count  of <40>
c[0] = -1   # Decrease ref. count  of <40>


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"


pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)  # prints the ids of the obejcts
del pt1
del pt2
del pt3

# Class inheritance (creating child class from pre-existing parent class)


class SubClassName(ParentClass1, ParentClass2):  # subclass of 1 and 2
    'Optional class documentation strin'
    class_suite

# Example


class Parent:        # parent class
    parentAttr = 100

    def __init__(self):
        print "Calling parent constructor"

    def parentMethod(self):
        print 'Calling parent method'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "Parent attribute :", Parent.parentAttr


class Child(Parent):  # child class
    def __init__(self):
        print "Calling child constructor"

    def childMethod(self):
        print 'Calling child method'


c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

# Functions to check relationships
# issubclass(sub, sup) boolean function returns true if subclass sub is indeed a subclass of the superclass sup
# isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class

# Overriding methods example


class Parent:        # define parent class
    def myMethod(self):
        print 'Calling parent method'


class Child(Parent):  # define child class
    def myMethod(self):
        print 'Calling child method'


c = Child()          # instance of child
c.myMethod()         # child calls overridden method

# Base overloading methods - functions that can be overridden in child class

__init__(self[, args...])  # Initialization (with any optional arguments)
obj = className(args)  # example
__del__(self)  # destructor, deletes an object
del obj  # example
__repr__(self)  # valuable string representation
repr(obj)  # example
__str__(self)  # printable string representation
str(obj)  # example
__cmp__(self, x)  # object comparison
cmp(obj, x)  # example

# Overloading operators example


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2

# Data hiding example


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
print counter.__secretCount  # returns error

# can however still be accessed: object._className__attrName
print counter._JustCounter__secretCount  # returns the count
