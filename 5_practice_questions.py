# Practice questions 

# WAP to check a number entered by user is odd or even 

number = int(input("Enter a number to check it is even or odd : "))
even = number%2 == 0
odd = number%2 != 0
if(even):
    print("This is even number");
elif(odd):
    print("This is Odd number");
else:
    print("Enter Valid number");


# WAP to check the greatest of 3 numbers entered by user

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

if(num1>num2 and num1>num3):
    print(num1 , " is the Greater number");
elif(num2>num1 and num2>num3):
    print(num2 , ' is the greater number');
else:
    print(num3 , " is greater number")


# WAP to check if a number is multiply of 7 or not

multiply = int(input("Enter a number"));
check = multiply%7 == 0
if(check):
    print("This number is multiply of 7");
else:
    print("this number is not multiply of 7")
