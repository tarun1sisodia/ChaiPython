#A list of names you have to print and say out for order , there are list of orders need to out them or prepare them.

list = ["Tarun","Tarun","Gunni","Gunjan","Himanshu","Gargii","Mohit","Rohit","Sajan"]

for order in list:
    print(f"Order ready of: {order}")

# Enumeration
for idx,item in enumerate(list,start=1):
    print(f"{idx}: {item}: ")