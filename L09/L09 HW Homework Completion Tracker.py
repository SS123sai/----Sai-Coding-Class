print("My Homework Checklist!")

total_homework = 7
original_count = total_homework
print(f" You have {original_count} homework to do!")
print()

completed_homework = 0
count= 1

while count<= original_count:
    if count==1:
        print("Next homework is Maths!")
    elif count==2:
        print("Next homework is Physics!")
    elif count==3:
        print("Next homework is Chemistry!")
    elif count==4:
        print("Next homework is English!")
    elif count==5:
        print("Next homework is ICT!")
    elif count==6:
        print("Next homework is Arabic!")
    else:
        print("Next homework is History!")

    completed = input("Have you completed this homework? (yes/no): ")
    if completed.lower()=="yes":
        print("Great! Move on to the next!")
        count+=1
        completed_homework +=1
    else:
        print("Okay, please complete the homework!")
    remaining = original_count - completed_homework
    print(f"You have {remaining} homework left!")
    print()

# Homework summary
print("============= HOMEWORK SUMMARY =============")
print(f"You had to complete {original_count} homework")
print(f"You have successfully completed {completed_homework} homework")
print("Remaining homework is : ", original_count- completed_homework)
print("Great Work!")
print()
print()

print("Let us take a sneak peek at an infinite loop!")
print("The loop will run forever as long as the safety count meets the requirement")
infinite_count = 0
safety_count = 0

while infinite_count <=10:
    print("I WILL RUN FOREVER!!")
    safety_count+=1

    if safety_count==15:
        break