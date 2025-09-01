count = 1
while count <= 5:
     print("Hello World")
     count += 1
print(count)


i = 1
while i <= 5:
     print("Prahallad Das")
     i+=1

#print numbers from 1 to 5
i = 1
while i <= 5:
     print(i)
     i += 1
print("Loop ended")     

#print number from 5 to 1
i = 5
while i >=1:
     print(i)
     i -= 1
print("Loop ended")   

#Break keyword
i = 1
while i <= 5:
     print(i)
     if(i == 3):
          break
     i += 1
print("end of loop")

#continue
i = 0
while i <= 5:
     if(i == 3):
          i += 1
          continue #skip the step
     print(i)
     i += 1

#odd Number
i = 1
while i <= 10:
     if(i%2 == 0):
          i += 1
          continue #skip the step
     print(i)
     i += 1


#Even Number
i = 1
while i <= 10:
     if(i%2 != 0):
          i += 1
          continue #skip the step
     print(i)
     i += 1


nums = [1, 2, 3, 4, 5]
for val in nums:
     print(val)


tup = (1, 2, 3, 4, 2, 8, 9)
for num in tup:
     print(num)






