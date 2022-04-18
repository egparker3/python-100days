# 4/17/2022

#this was a project for how much life you have left:

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)

years_left = (90 - age_int)

months = years_left * 12

weeks = years_left * 52

days = years_left * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")