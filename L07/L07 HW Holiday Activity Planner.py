print("====================================")
print("          HOLIDAY PLANNER           ")
print("====================================")


print("School weekend = 1")
print("Family holiday = 2")
holiday_type= int(input("What is your holiday type: "))

if holiday_type==1:
    print("Outdoor = 1")
    print("Indoor =  2")
    destination= int(input("What is your destination type?: "))

    if destination==1:
        print("Go to the beach!")
        print("Don't forget the sunscreen and umbrella!")
    else:
        print("Watch a movie!")
        print("Don't forget the popcorn!")

elif holiday_type==2:
    print("Outdoor = 1")
    print("Indoor = 2")
    destination= int(input("What is your destination type? "))

    if destination==1:
        print("Go camping!")
        print("Don't forget the tent and sleeping bags!")
    else:
        print("Have a cosy barbeque night!")
        print("Don't forget the marshmallows!")
else:
    print("Invalid input")
    print("Please enter 1 for School Weekend and 2 for Family Holiday")

