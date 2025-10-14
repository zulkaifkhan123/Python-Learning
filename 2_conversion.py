"""
Type Conversion in Python

there are two type of type conversion in python
1. conversion : Python automatically convert type of variable without asking 
2. type casting : user manually convert type of data to another data type

"""


#type casting

value1 = "2"
value2 = 22.2
value1 = int(value1)

print(f"Addition of value1 and value2 is : {value1 + value2}") # 24.2

value3 = 2

value3 = str(value3);
print(type(value3)); #string



# type conversion
data = 2 
data2 = 2.2

print(data + data2) #4.2 
#here 2 is automatically converted to floating value 2.0
