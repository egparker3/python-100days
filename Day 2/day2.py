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