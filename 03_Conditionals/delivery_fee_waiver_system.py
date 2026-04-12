#You run online tea store:

#if order price is 300 or above -> free delivery
# Else 30 apply for charge for delivery.

order_amount = int(input("Enter your Orde price:"))
Delivery_fee =  0 if order_amount > 300 else 30
print(f"Total Price is: {order_amount+Delivery_fee}")