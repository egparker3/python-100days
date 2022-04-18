#Starting day 2 of the bootcamp it is 4/10/2022

#Data Types

#other data types besides Strings
#Strings are a string of characters and are inside two quotes
#Subscripting: If I want to denote a specific character in a string, I can use a double bracket []
print("hello"[0])
#this will print an 'h' because it is the first character in the string
#programmers always start counting with 0
print("hello"[4])
#as long as you have quotes around something, even numbers, the program will think this is a string and won't count them as numbers
print("123" + "456")
#len(123) gives 'TypeError: object of type 'int' has no len()' because of a type error, length can only apply to strings. It doesn't like working with Integers

#Integer data type: number without any decimal places
#write the numbers without anything else
print(123 + 456)
#Can replace commas in large integers with underscores; instead of 1,300 it would be 1_300

#Float: floating point number: numbers with decimal points
#4.56

#Boolean: can either be True or False, make sure both True and False are capitalized and no quotes

#this is not a data type, but if you want to comment out a line, just press Command + /

#if you want to know what data type something is, can use the type() function

print(type(3))

#can do a type conversion, or type casting: change data from one type to the other

#can use the str() function to change a data type to a string

num_char = len(input("what is your name? "))
new_var = str(num_char)
print("length of name" + new_var + " is this long")
#this is what I did the other day on my own

# can change types to Floats as well using float()

print(70 + float("105.5"))
#this changes the string into a float and gives you a float number

# 4/11/2022

#below is the first project/challenge of Day 2:

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

x = (two_digit_number[0])
y = (two_digit_number[1])

a = int(x)
b = int(y)
print(a + b)

#another way that the teacher described was less letters and went as follows:
print(int(x) + int(y))

#OR another way, is doing this:
c = int(two_digit_number[0])
d = int(two_digit_number[1])
print(c + d)

#4/13/2022

# 3 + 5 addition
# 3 - 5 subtraction
# 3 * 5 multiplication
# 3 / 5 division
# whenever you're dividing, you get a float number. 
# ** is an exponent 
# 3**2 = 9

# order of PEMDAS 
# parentheses
# exponents
# multiplication & division
# addition & subtraction
# the one most to the left will be done first for M and D, and A and S

#this was the code challenge she had us do which was a BMI calculator

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

#what the teacher did was this:

# bmi = int(weight) / float(height) ** 2
#bmi_as_int = int(bmi)

#but i wonder if we could do this too:

bmi = int(int(weight) / float(height) ** 2)
print(bmi)

#yep that worked! 
#in her solution, she als did it like i did with converting beforehand

# 4/16/2022
# if you do print(8 / 3) it becomes 2.66666666
# then if you do print(int(8 / 3)) it just truncates it to 2, instead of rouding up to 3 
print(8/3)
print(int(8/3))
# can just use the round() function
print(round(8/3))
#in the round() function, you can add a comma and then specify how many digits you'd like it to come out to after the decimal ; decimal places
print(round(8/3,2))
#whenever you divide a number by another number, the result is always a floating point number
#the floor division, or // , always truncates a floating point number in the same way, without rouding. turns it into an Integer
#8//3 = 2
print(8 //3)
#even a whole division is a floating point number, ex:
# 4 / 2 = 2.0
print(4 / 2)

#the following gives result as 2, then the /= divides again by 2, which equals 1
result = 4 / 2
result /= 2
print(result)
# the /= uses the previous result as a short hand, instead of using:
#result = result/2

#another example:

score = 0

#then, instead of saying, 
#score = score + 1
score += 1
print(score)
#this is handy when you need to manipulate a value based on its previous value

#f-strings

#instead of having to convert a bunch of different data types and use + signs to print a string of concatinated things, can use f-string

score = 0
height = 1.8
isWinning = True

# in order to print this without f string, would need to do:
#print("your score is " + str(score) + str(height)) and so on
#you add the character f in front of your string
#f"your score is {}" these are curly brackets

print(f"your score is {score}, your height is{height}, you are winning is {isWinning}")
#f-strings turn everything into a string

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