"""
For Loop Practice : 

"""
# 1. Print the multiplication table of a number n

n = int(input("enter a number"))

for num in range(1,11,1) : 
    print(n*num);
else : 
    print("this is the table of ",n)


# 2. Print the elements of the following list using a for loop : 

list_items = [1,4,9,16,25,36,49,64,81,100]

for item in list_items : 
    print(item);
else : 
    print("loop end here ");


# 3. Search for a number x in this tuple using for loop : 

tuple_items = (1,4,9,16,25,36,49,64,81,100);

number = 64
flag = False

for item in tuple_items : 
    print(item)
    if item == number :
        flag = True
        print("Number Found");
        break
if not flag : 
    print("number not found");

 
