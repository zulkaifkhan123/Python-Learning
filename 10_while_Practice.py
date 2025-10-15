"""
Loops Practice Questions : 

1. Print the multiplication table of a number n.
"""

n = int(input("Enter A number to Print It's Multiplication Table : "))
i=1
while i <=10 :
    print(i*n);
    i += 1

print("Loop Ended Here ");



# 2. Print the following list using Loop 

list_items = [1,4,9,16,25,36,49,64,81,100]
length = len(list_items);
length -= 1
i = 1
while i <= length : 
    print(list_items[i]);
    i += 1
print("loop end here ");



# Search for a number x in this tuple using loop

# method 1 : 

tuple_items = (1,4,9,16,25,36,49,64,81,100);
length = len(tuple_items) - 1
number = 64 ;
i = 1
while i <= length : 
    list_item = tuple_items[i]
    result = number == list_item
    if(result) :
        print("number is found in touple")
        break
    else :
        print("number Not Found..")
    i += 1
print("loop end here ");

# method 2 : 

tuple_items = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
length = len(tuple_items) - 1
number = 64
i = 0
found = False  # flag to track if number found

while i <= length:
    list_item = tuple_items[i]
    if number == list_item:
        print("Number is found in tuple.")
        found = True
        break
    i += 1

if not found:
    print("Number not found in tuple.")

print("Loop ended here.")
