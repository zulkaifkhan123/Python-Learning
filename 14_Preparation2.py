"""
Question : Loan Eligibility Checker

Write a program that checks if a person is eligible for a loan based on:

· Age must be between 21 and 65
· Annual income must be at least $30,000
· Credit score must be 650 or higher

If eligible, check if they qualify for premium rate (credit score > 750 and income > $50,000).

"""

age = int(input("Enter Your Age : "));
annual_income = int(input("What is Your Annual incom : "));
credit_score = int(input("What is Your Credith Score between 300-850 : "));



if (age > 21 and age < 65) and (annual_income >= 30000) and (credit_score >= 650) :
    if credit_score > 750 and annual_income > 50000 :
        print("Congrates You Are selected for Premium rate of Loan 🎉")
    else :
        print("You Are Eligibal For loan 🎉")
else :
    print("You are not Eligibal for Loan")





