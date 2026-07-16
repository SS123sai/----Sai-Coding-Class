# PART 1: Ask for temperature
temperature = int(input("What is the temperature? "))

# PART 2: Decide an activity based on temperature
if temperature <20:
    activity= "watch a movie!"
    print("It is a cold day!")
    print("Today lets "+ activity)
else:
    activity= "go for a walk!"
    print("It is a warm day!")
    print("Today lets " + activity)

print()
# PART 3: Ask whether its raining
rain= input("Is it raining? ")

# PART 4: Decide an activity based on whether it is raining
if rain.lower()== "yes":
    reminder= "take an umbrella!"
    print("It is raining today.")
    print("Remember to " + reminder)
else:
    reminder= "wear sunscreen!" 
    print("It is not raining!")
    print("Remember to "+ reminder)

print()
# PART 5: Ask about the homework time
homework= input("Have you done your homework? ")

# PART 6: Decide about homework
if homework.lower() == "yes":
    print("You have completed your homework!")
else:
    print("You have not completed your homework!")
    print("Ensure that your homework is completed.")

print()

# PART 7: Ask about the free time
free= int(input("How much free time do you have in hours? "))

# PART 8: Decide an activity:
if free > 1:
    print("You have a lot of free time!")
    print("Let's visit a friend!")
else:
    print("You do not have a lot of free time!")
    print("Read a book!")

print()

print("PLANNER COMPLETED")

print("===== PLANNER =====")
print("Temperature:", temperature)
print("Raining: " + rain)
print("Homework time:" , homework)
print("Free time: ", free)
print("=====THANK YOU!!======")



