# Name : Cynthia Wanjiru
# Date : 18/02/2026
# Program to show list in python

friends = ["Rachael","Phoebe","Ross","Chandler","Monica","Joey"]

print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends.append("Jack")
print(friends)

new_friends = ["Nailah","Reenie","Wendy","Abigael"]

print(len(new_friends))

#new list of students
students = friends + new_friends

print(students)
students.pop()
print(students)
students.insert(3,"Dicky")
students.insert(6,"Jenny")
print(students)
students.extend("Dawn")
print(students)
students.remove("Ross")
print(students)

new_students = students.copy()
print(new_students)