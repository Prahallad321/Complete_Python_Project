light = input("light color: ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

num = 6
if(num > 5):
    print("greater than 2")
if(num > 3):
    print("greater than 3")    

marks = int(input("enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "c"
else:
    grade = "D"
print("grade of the student: ", grade)                


age = 17
#nesting
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")            









