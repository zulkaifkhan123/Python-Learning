"""
Loop Practice : 

"""

# WAP for checking Prime number : 

num = int(input("Enter Number --> "));

if num <=1 : 
    print(f"{num} is not a Prime Number .");
else :
    for i in range(2 , num+1) :
        pass

# NOTe: REMANING THIS WORK





# WAP to print Fibonacci sequence using for loop

n = int(input("Enter how many terms you want --> "))
"""
n = 10 
a = 0 , 1 , 1 , 2 , 3 , 5 , 8
b = 1 , 1 , 2 , 3 , 5 , 8 , 13
c = 0 , 1 ,  1 , 2 , 3 , 5 , 8 , 13 
"""
a = 0 ,
b = 1 ,
for i in range(n) : 
    print(a);
    c = a+b
    a = b 
    b = c


# 1. WAP to find the sum of first natural numbers (using while loop);

n = int(input("Enter a number --> "));
i=1;
save = 0

while i<=n :
    save += i
    i+=1
print(save) 


#2. WAP to find the factorial of first n numbers (using for loop);
# Note : factorial of a number is the product (multiplication) of all positive integers from 1 up to that number.

n = int(input("Enter a number --> "));
factorial = 1
for num in range(1,n+1) : 
    factorial *= num ;
print(f"factorial of {n} is {factorial}");

