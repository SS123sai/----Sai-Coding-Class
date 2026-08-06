print("Ultimate Movie Experience")
number= int(input("how many people are there? "))
total=0
for i in range(number):
    age=int(input("Please enter age: "))
    if age>=25:
        print("Ticket price is $30")
        total+=30
    elif age>=18:
        print("Ticket price is $20")
        total+=20
    else:
        card= input("Do you have student id card? ")
        if card.lower()=="yes":
            amount= 15 * 0.8  #80% discount
            print(f"Ticket price is {amount}")
            total+=amount
        else:
            print("Ticket price is $15")
            total+=15
print("Total amount: ", total)
