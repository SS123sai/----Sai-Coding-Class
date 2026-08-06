print("=== Grocery bill ===")

high_priced = medium_priced = low_priced = 0

customer_served = 0
total_sales = 0

serving = True

while serving:
    name = input("What is your name: ")
    number_items = int(input(f"Hello {name}, how many different items are you purchasing?: "))

    if number_items <= 0:
        print("Invalid item count. Please enter a positive number!")
        continue

    print(f"Billing items for customer {name}")
    print()

    total = 0
    item_count = 1

    while item_count <= number_items:
        item_name = input("What is the name of the product?: ")
        item_price= int(input("What is the price of the product?: "))
        quantity = int(input("How much quantity are you purchasing?: "))

        if item_price<=0 or quantity<=0:
            print("Invalid price or quantity- please try again.")
            continue

        total_per_item = item_price * quantity
        total+= total_per_item
        
        
        print(f"For {item_name}, the price is {item_price} x {quantity} = {total_per_item}")
        print()

        if total_per_item < 50:
            low_priced += total

        elif total_per_item <= 100:
            medium_priced += total

        else:
            high_priced += total

        item_count += 1
    total_sales+= total

    customer_served+=1 
    print(f"total amount for customer {name}= {total}")
    print("Billing Complete")
    print()

    again = input("Are you the next customer? (yes/no): ")
    if again.strip().lower()=="no":
        serving = False

print("=== BILL REPORT ===")
print(f"Customer total bill = {total}")
print(f"Total Sales = {total_sales}")





