"""
Loop Practice : 

"""

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

