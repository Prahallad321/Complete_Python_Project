class Student:
    name = "karan"

s1 = Student()
print(s1.name) 
s2 = Student()
print(s2.name)

class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)

#constructor
class Student:
    #default constructors
 def __init__(self):
       pass
   #parameterized constructors     
 def __init__(self, name, marks):
       
        self.name = name
        self.marks = marks
        print("Adding new student in Database...")
# creating object
s1 = Student("Karan", 97)
print(s1.name, s1.marks)

s2 = Student("arjun", 87)
print(s2.name, s2.marks)

#Abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()

#Encapsulation

#Inheritance
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())

#Multi Level Inheritance
class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped. ")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("diesel")
car1.start()

# Multiple Inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class c(A, B):
    varC = "welcome to class C"

c1 = c()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#Class Methods
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = "Rahul"


p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)

#Property 
class Student:
   def __init__(self, phy, chem, math):
       self.phy = phy
       self.chem = chem
       self.math = math
   @property
   def percentage(self):
       return str((self.phy + self.chem + self.math)/ 3) +"%"
     
stu1 = Student(98, 97, 99)
print(stu1.percentage)
stu1.phy = 86
print(stu1.percentage)

print("apna" + "college") #concatenate
print(type("apna"))

print([1, 2, 3] + [4, 5, 6]) #merge

#complex Number Addition
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.real = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)    


num1 = complex(1, 3)
num1.showNumber()

num2 = complex(4, 6)
num2.showNumber()

num3 = num1 + num2

num3.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img   # fixed

    def showNumber(self):
        print(f"{self.real} + {self.img}i")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)    


# Creating objects using our Complex class
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()







