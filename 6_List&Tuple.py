"""
List is an ordered and mutable collection that allows
us to store multiple items in a single variable.

Tuple is an ordered and immutable collection used to store
multiple items in a single variable.
It is defined using parentheses ( ), and once a tuple is created,
its elements cannot be changed or modified.

"""

student = ["ali" , 32];
student[0] = "zulkaif" # mutable
print(student) # ["zulkaif" , 32]

print(student[0:]) # print hole array or list

student.append("mango") # added new element at last of list
print(student) 

#student.pop(); # it remove last element of list 
#print(student)

student.insert(1,31)
print(student)

teacher = ("imran" , 73);
#teacher[0] = "khan" # it will give error because tuple is immutable
print(teacher) # ("imran" , 73)
print(teacher[0:]) # print hole array or tuple
print(len(teacher)) # print length of tuple
#teacher.append("mango") # it will give error because tuple is immutable
#print(teacher)
#teacher.pop(); # it will give error because tuple is immutable
#print(teacher)
#teacher.insert(1,31) # it will give error because tuple is immutable
#print(teacher)

