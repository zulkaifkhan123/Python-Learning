"""

Question : Shopping Discount Calculator

Calculate the final price after discounts based on:

· Membership level:
  · "gold": 20% discount
  · "silver": 15% discount
  · "bronze": 10% discount
  · "none": 5% discount for purchases over $100
· Purchase amount: Additional 5% discount if purchase > $200

"""

membership = input("Enter What you buy ? (gold , silver , bronze ) if none of them (none) : ")
parchase_amount = float(input("Enter Parchase amount : "))
discount = 0
if membership == "gold" :
    discount = 20
elif membership == "silver" :
    discount = 15
elif membership == "bronze" :
    discount = 10 
elif membership == "none" :
    if parchase_amount > 100 :
        discount = 5
else :
    print("Enterd Invalid Membership !");

if parchase_amount > 200 :
    discount += 5

print(f"You got Discout of {discount}%");
