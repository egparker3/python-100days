#16 May 2022

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

total = input("What was the total bill? $")
#can also do total = float(input("What was the total bill? $")) this would turn it into a float right away and don't have to do it at the end

tip = input("How much tip would you like to give? 10, 12, or 15? ")
tip_float = 1 + (float(tip) / 100)
#can similarly do this here with using float(input) after tip = 
#she used int for the tip and for the people
#for tip_float, I tried to do what she did above using the 1.12, but she did it differently, utilizing the below:
#bill_with_tip = tip / 100 * total + total 
#she also later though, described what I had done!

people = input("How many people to split the bill? ")

output = (float(total) / float(people)) * tip_float

#had to google this, because using the round function wasn't allowing 2 decimal places if they were both zeros:
output_float = "{:.2f}".format(output)

print(f"Each person should pay: ${output_float}")

#this was a formatting problem, and not a mathematical problem. That's why I had to use the format function
#I completed the project correctly without looking at the solution!