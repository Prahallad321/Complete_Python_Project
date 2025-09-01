
collection = {1, 2, 2, 3, 4, "hello", "hello", "world"}
print(collection)
print(type(collection))

collection = set() #empty set; syntax
collection.add(1)
collection.add(2)
collection.add("apnacollege")
collection.add((1, 2, 3))

print(collection)


collection = { "hello", "apnacollege", "world", "coding", "python"}
print(collection.pop())
print(collection.pop())

#union Method 
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1)
print(set2)

#Intersection
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))



