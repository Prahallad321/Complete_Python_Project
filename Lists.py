marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(marks[0])
print(marks[1])
print(len(marks))

student = ["karan", 95.4, 17, "Delhi"]
print(student[0])
student[0] = "arjun"
print(student)

#Slicing
marks = [85, 94, 76, 63,48]
print(marks[0:5])

# Appending
list = [2, 1, 3]
list.append(4)
print(list)

# sorting Ascending
list = [2, 1, 3]
list.sort()
print(list)

#sorting Decending order
list = [2, 1, 3]
list.sort(reverse=True)
print(list)

#Reverse Method
list = ['a', 'd','e', 'f','c', 'b']
list.reverse()
print(list)

#insert method
list = [2, 1, 3]
list.insert(1, 5)
print(list)

#remove Method

#POP Method
list = [2, 1, 3, 1]
list.pop(2)
print(list)
