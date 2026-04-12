# A local cafe wants a program that suggests a snack
#if a customer  asks for cookies or samosa, it confirms the order 
#otherwise , it says its's not available 

#Task 
#take snack input 
#if it's  "Cookies" or "Samosa" , confirm the order
#Else  show unavailability

snack = input("Enter your Prefered Snack:  ").lower()

print(f"User said: {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice: :) {snack} Your Order is in Processing")
else :
    print(f"Not Available")
    