# --------- NOTES ---------
# PEMDAS - Left to Right:

# () Paranthesis
# ** Exponent
# * / Multiplication Division
# + - Addition Subtraction

# print(3 * 3 + 3 / 3 - 3)
# print(round(8/3, 2)) # rounds off to float value with two decimal places
# print(round(8/3)) # rounds off to integer value
# print(8//3) # chops off decimal value

# f-string
# print(f"Your score is {score}")

# --------- TIP CALCULATOR ---------

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100
people = int(input("How many people to split the bill? "))

per_person_bill = bill/people
per_person_bill_with_tip = per_person_bill + per_person_bill * tip

print(f"Each person should pay: ${round(per_person_bill_with_tip, 2)}")