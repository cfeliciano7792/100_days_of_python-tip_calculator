#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Displaying user imput prompts
print("Welcome to the tip calculator!")

bill = input("What was the total bill? ")

tip_amount = (input("How much tip would you like to give? 10, 12, or 15? "))

people_splitting = input("How many people are splitting the bill? ")

#Converting user input values from strings to integers or floating point number
float_bill = float(bill)
integer_tip_amount = int(tip_amount)
integer_people_splitting = int(people_splitting)

#Converting tip value into a percentage

tip_percentage = integer_tip_amount / 100

total_tip = float_bill * tip_percentage

# calculating total bill with tip

total_bill_tip = (float_bill + total_tip)

#dividing total bill by amount of people

split_amount = round(total_bill_tip / integer_people_splitting, 2)

print(f"Each person should pay : ${split_amount}")






