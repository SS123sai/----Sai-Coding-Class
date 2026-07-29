a= int(input("Enter a number: "))
b= input("Enter a word: ")
c= int(input("Enter a number: "))

#Before swapping
print("Before Swapping: ")
print("A = ", a)
print("B = ", b)
print("C = ", c)
print()

#Swapping values
helper= a
a = b
b = c
c = helper

#After Swapping
print("\n After swapping")
print("A = ", a)
print("B = ", b)
print("C = ", c)

