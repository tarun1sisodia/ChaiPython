#You're building a ticket info system for a railway app
#Based on seat type, show its features
 #Task:
    #input: "sleeper", "AC", "general","luxury"
    #Match using match-case
    #Unknown -> show: "Invalid seat type"

seat = input("Enter your Seat Type to get details: \n").lower()

match seat:
   case "sleeper":
      print("This includes Non-Ac and General Seat Quality: \n")
   case "ac":
      print("This includes Ac and better quality than all of seat:\n")
   case "general":
         print("This doesn't include Seat and and no AC :\n")
   case "luxury":
         print("Welcome! Best AC and Seat Availability :\n")

