"""
-give the user some choices
-ask the user to make a using a number
-tell the user that you got in their choice
-confirm that the user made a valid chance(from thelist of options)
"""

asking = True

a= "Apple"
o= "Orange"
b= "Banana"

while asking:
    print(f"Choices:\n1. {a}\n2. {o}\n3. {b}")
    choice = input("please choose a fruit (1,2, or 3 )")
    print(f"You chose choice #{choice}")

    if choice == "1" or choice =="2"or choice=="3":
        asking = False
    else:
        print("Please only type in 1,2, or 3 :) ")

print("Thank you for making a valid choice!")
