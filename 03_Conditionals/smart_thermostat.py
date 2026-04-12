#I'm Building a smart thermostat alert system
#if the device_status is "active"
# and  temperature  > 35  -> Warm :" High Temperature alert!!"
    #else "Temperature Normal"
#if device is OFF => "Device is Offline"


temp = int(input("Enter Temperature: "))

status = input("Enter Device Status: ").lower()

if status == "active":
        if temp > 35:
            print(f"Device is Active !! Temperature High")
        else:
            print(f"Device is Active &&  Temperature is Normal")
elif status == "offline":
    print(f"Device is OFFLINE")
else:
    print(f"May be Device is Offline")