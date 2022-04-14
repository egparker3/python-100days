# 4/13/2022

#she had us do a BMI calculator and this is what I came up with

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#bmi = weight/height^2
#height and weight are strings

height_float = float(height)
weight_float = float(weight)

bmi = int(weight_float / (height_float ** 2))

print(bmi)