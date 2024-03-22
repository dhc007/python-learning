#if else statements
a=int(input("Enter your age:\n"))
print("your age is: ",a)
if(a>=18): # conditional operators: >,<.>=,<=,==,!=
    print("You can drive")
else:
    print("You cannot drive")

mb=93000
bdgt=int(input("What is your budget for the car?"))
if(bdgt>=900000):
    print("You should consider buying Car 1")
elif(700000<=bdgt<900000):
    print("You should go for a Car2")
elif(500000<=bdgt<700000):
    print("You should go for a Car2")
elif(400000<=bdgt<300000):
    print("You should go for a Car2")
else:
    print("We do not have anything in that range for you\nThank You for Visiting Us Have a Great Day!!")