# A tea stall offers different prices  for different cup sizes  write a program that calculates the price based on size.

#Task
# input    :"Small", "Medium","Large"
#Small ->   10, Medium -> 15, Large -> 20 Prices of cup based on sizes.
#if  invalid : Show "Unknown cup size"

cup_size = input("Enter your Cup Size: ").lower();

cup_no = int(input("Enter How many cups you want:-> "))

if(cup_no < 0):
    print(f"Please Provide minimum 1 cup: {cup_no}")
else :
    if("small" == cup_size):
        print(f"Making Small tea: & Total Price: {cup_no*10}");
    elif("medium"== cup_size):
        print(f"Making Medium Tea:  & Total Price: {cup_no*15}");
    elif("large" == cup_size) :
        print(f"Makin Large Tea:  & Total Price: {cup_no*20}");
    else :
        print(f"Oops Try again!!!!!!")