#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line

bill_str = input("What's the bill ?\n")
bill = int(bill_str)
# print(type(bill))
num_of_people = input("How many are you ?\n")
people = int(num_of_people)
tip_perc = "12%, 14%, 20%"
print(tip_perc)
tips = input("choose a percentage to tip\n")
tip_chosen = int(tips)
calc_tip = float((bill / people) * tip_chosen)
tip = calc_tip
print(tip + bill)