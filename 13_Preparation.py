"""
Practice questions for paper preparation :

Question : Create a program that calculates movie ticket price based on:

· Age: Child (<13): $8, Adult (13-64): $12, Senior (65+): $10
· Time: Matinee (before 5 PM): $2 discount
· Day: Wednesday: $3 discount

"""

age = int(input("Enter your Age ! : "))
price = 0

if age < 13 : 
    price = 8
    print("You are child now ! so it's 8 ",price)
elif age > 13 and age < 64 :
    price = 12
    print("You are adult. now it's 12 ",price)
else :
    price = 10
    print("you are oldman so it's 10 ",price)



time = int(input("Enter Time in 24-hours formate e.g : for 1PM type 13 : "))
if time < 17 :
    price -= 2
    print("Getting discount of 2 ",price)
if time > 17 :
    print("Miss time discount oops : " , price)

day = input("Enter current day name of a week ! : ")
if day == "Wednesday" :
    price -= 3
    print("getting discout of Wednesday : " , price)

print(f"Your Movie Ticket Price is {price}")