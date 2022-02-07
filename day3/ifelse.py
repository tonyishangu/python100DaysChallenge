#if .... else statements
print("Welcome to the rollercoaster")
height = int(input("Enter your height in cm\n"))

if height >= 120:
    print("You are allowed to ride the rollercoaster")
    #nested if statements and elif
    age = int(input("Enter your age\n"))
    if age <= 12 :
        print("Pay ksh. 500")
    elif age <= 18 :
        print("Pay ksh. 700")
    else:
        print("Pay ksh. 1200")
else:
    print("Sorry you have to grow taller for you to ride")