"""
Question : Print All Prime Numbers Between 1 to 100

"""


for num in range (2 , 11) :
    for i in range (2 , num) : 
        if num % i == 0 :
            break
    else :
        print(num)
        


"""
Question : indentify wheather the entered number by user is prime or not 

"""

value = int(input("Enter Number --> : "))

for num in range(2, value):
    if value % num == 0:
        print("This is NOT a Prime number. because it is divisable by ",num)
        break
else:
    print("This is a Prime number.")


