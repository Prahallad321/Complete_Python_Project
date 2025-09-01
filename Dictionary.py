
info = {
    "name" : "apnacollege",
    "subjects": ["Python", "C", "Java"],
    "topics" : ("dict", "set"),
    "age" : 35,
    "is_adult" : True,
    12.99 : 94.4
}
info["name"] = "Prahallad"
info["surname"] = "Das"
print(info)

#Nested Dictionary
student = {
  "name" : "Prahallad Das",
   "subjects" : {
       "phy" : 97,
       "chem" : 98,
       "math" : 95
    }
 }

print(len(student))
print(list(student.keys()))
print(student["subjects"])
print(list(student.values()))






