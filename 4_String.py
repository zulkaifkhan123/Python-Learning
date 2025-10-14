# String : String is a data type that is used 
# to store diffrent sequence of characters.


# Slicing in Python means extracting a specific 
# portion (or part) of a sequence such as a string, 
# list, or tuple by using an index range.

name = "muhammad Ali";
print(name[1:4]) # uha
print(name[0:]) # Muhammad Ali
print(name[-12:]) # Muhammad Ali

# Note : Slicing goes from left to right 

# String Functions 

print(name.endswith("Ali")) # True
print(name.capitalize()) 
# it will capitalize first char and it won't modify orignal string

print(name.find("d")) # 7
print(name.count("m")) # 3

print("my name is {}".format(name)) 
#In Python, the .format() method is used to insert (or format) 
# values into a string.
#It replaces placeholders {} inside a string with specified values.
