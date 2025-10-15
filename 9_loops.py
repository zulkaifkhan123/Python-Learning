"""
Loop : A loop in programming is a control structure that allows a block of code to repeat multiple times until a specific condition is met.

In simple words, loops help to execute a set of statements again and again automatically, without writing the same code multiple times.

Types of loops in Python:
1. For Loop
2. While Loop
-->  Nested Loop

"""

# While loop 
# A while loop keeps running a block of code as long as a given condition is true.

i = 1
while i <= 10 :
    print("I Love Python❤");
    i += 1
print("Loop Ended Here ");


# For Loop 
# Repeats a block of code for each item in a sequence or a fixed number of times.


n = int(input("Enter a number "))

for num in range(1,11,1) :  # (start , end , increment or Step)
    print(n*num);
else : 
    print("this is the table of ",n)

# The range() function in Python is used to generate a sequence of numbers.
