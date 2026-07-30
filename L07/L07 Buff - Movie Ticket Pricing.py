base_price= 10

age= int(input("What is your age? "))
card=input("Do you have VIP membership? Pls enter Yes/No: ")

if age<12:
    price=base_price*0.9 #Discount is 10%

    if card.lower()=="yes":
        price = price*0.5 #Discount is 50%

elif age>=12 and age<20:
    if card.lower()=="yes":
        price = base_price * 0.5 #Discount is 50%

else:
    price=base_price*0.95 #Discount is 5%

    if card.lower()=="yes":
        price= price*0.5 #Discount is 50%

print("Your total is: ", price)
    




