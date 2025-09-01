# Write a Program to input 2 numbers & print their sum
first = int(input("enter first : "))
second = int(input("enter second : "))
print("sum =", first + second)

#WAP to input side of a square & print its area
side = float(input("enter square side: "))
print("area = ", side*side)

a = float(input("enter first : "))
b = float(input("enter second : "))
print("avg =", (a+b)/2)

# WAP to input 2 int numbers, a and b.
#print True if a is greater than or equal to b. If not print False
a = int(input("enter first : "))
b = int(input("enter second : "))
print(a >= b)

#WAP to input user's first name & print its lenght
name = input("enter your name : ")
print("lenght of your name is ", len(name))

str = "Hi, $Iam the $ symbol $99.99"
print(str.count("$"))

#WAP to check if a number entered by the user is odd or even
num = int(input("enter number: "))
rem = num % 2
if(rem == 0):
    print("EVEN")
else:
    print("ODD")    

#WAP to find the greatest of 3 numbers entered by the user
a = int(input("enter first number: "))
b = int (input("enter second number: "))
c = int(input("enter third number: "))
if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third is largest", c)    

# WAP to  check if a number is a multiple of 7 or not
x = int(input("enter number: "))
if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")
    
    #WAP to ask the user to enter names of their 3 favorite movies & store them in a list
movies = []
mov1 = input("enter 1st movie: ") 
mov2 = input("enter 2nd movie: ") 
mov3 = input("enter 3rd movie: ")    

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
list1 = [1, 2, 1]
list2 = [1, 2, 3]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")    

#WAP to count the number of students with the "A" grade in the following tuple
grade = ("c", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

#Store the above values in a list & sort them from "A" to "D"
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)

#Store following word meaning in a python dictionary
dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]

}
print(dictionary)

#you are give a list of subjects for students. Assume one classroom is required for 1
#Subject. How many classrooms are needed by all students
subjects = {
    "python", "java", "C++", "python", "javascript", "java",
    "python", "java", "C++"

}
print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an
#empty dictionary & add on by one. subject name as key & marks as value
marks = {}

x = int(input("enter phy :"))
marks.update({"phy" : x})
x = int(input("enter math :"))
marks.update({"math" : x})
x = int(input("enter chem:"))
marks.update({"chem" : x})

print(marks)

#Figure out a way to store 9 & 9.0 as separate values in the set

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)

#print numbers from 1 to 100
i = 1
while i<= 100:
    print(i)
    i += 1

#Print the numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

#print the multiplication table of a number n.
i = 1
while i <= 10:
    print(4*i)
    i += 1

n = int(input("enter number : "))
i = 1 
while i <= 10:
    print(n*i)
    i += 1

# Print the elements of the following list using a loop
nums = [1, 4, 9, 16, 25, 36, 49,  64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1 

#Print the elements of the following list using a loop:
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in nums:
    print(i)


#Search for a number x in this tuple using loop


# Range
seq = range(10)
for i in seq:
    print(i)

for i in range(2, 10):
    print(i)

for i in range(10):
    print(i)

for i in range(2, 100, 2):
    print(i)   

#Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)

#Print numbers from 100 to 1.

for i in range(100, 0, -1):
    print(i)

#Print the multiplication table of a numbers n
n = int(input("enter number: "))
for i in range(1, 11):
    print(n*i)

#WAP to find the sum of first n numbers (using while)
n = 7
sum = 0
for i in range(1, n+1):
    sum += i
print("total sum =", sum)    


#WAP to find the factorial of first n numbers (using for)
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1 
print("factorial =", fact)

#WAF to print the lenght of a list. (list is the parameter)
cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

#WAF to print the elements of a list in a single line. (list is the parameter)
cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]
def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(heroes)


#WAF to find the factorial of n (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    cal_fact(5)   

#WAF  to convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 86
    print(usd_val, "USD =", inr_val, "INR")

converter(1)

#Write a recursive function to calculate the sum of first n natural numbers
def calc_sum(n):
    if(n == 0):
         return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

#Write a recursive function to print all elements in a list.
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
fruits = ["mango", "litchi", "apple", "banana"]

print_list(fruits)

#WAF that replace all occurrences of java with "python" in above file


#Create student class that takes name & marks of 3 subjects as arguments in constructor
#Then create a method to print the average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is:", sum/3)

s1 = Student("Prahallad Das", [99, 98, 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()

# Create Account class with 2 attributes- balance & account no.n
# Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    #debit method 
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")  
        print("total balance = ", self.get_balance())  

    def get_balance(self):
        return self.balance    


acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)

#Q: Define a Circle class to create a circle with radius r using the constructor
# Define an Area() method of the class which calculates the area of the circle
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius
       

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


#Define a Employee class with attributes role, department & salary. This class
#show Detais() method.
#Create an Enginner class that inherits properties from Employee & attributes
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print("role =", self.role) 
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")
engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()

# 















