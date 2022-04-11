#Today is day 1 of my 100 Days of Code: The Complete Python Pro Bootcamp course. April 6th 2022
print("hello world")
# Write your code below this line 👇
print("Hello world!")
#print function follows parentheses, inside the parentheses you tell it what you want to print.
#in order to tell computer that something is not code, you need to use quotes
#not having ending quotes produces a Syntax Error
#Strings: a line of characters, with the quotes showing beginning and end of the string of characters
#if you don't have the ending quotes, the ending parenthesis will not be the same color as the beginning parenthesis 
#if you come across a red error, copy and paste the error into google, with stackoverflow.com usually having an answer
#OK, the first assignement she gave us is through Coding Rooms, and the input is the following:
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
#I got the answer correct on the first try!
#using double quotes or single quotes doesn't matter for printing
print('hello')
#however, if you want to have a quote inside a quote, you need to use the single quote inside the double quote, so that the computer knows where your strings are. If you used a double quote then another double quote, it would think your string is the print and the function/code comes after the first double quote. 
#4/7/2022
#either you can use the Print function on each line to write code on each line, or you can use the \n function inside of double quotes to print on separate lines
print("hello world!\nhello world")
#concatenation: combining two strings using + to turn it into a single string
print("hello" + "emily")
#to add a space, a space needs to be inside the quotes
print("hello " + "emily")
#or you can add a space this way
print("hello" + " " + "emily")
# you will get indentation errors if there are spaces before your print statement
#if you have multiple errors, when you run your code, the program will only alert you to your first error. then you run again, and it will alert to you to your second error, and so on, until it is all fixed
#she had us do a second assignment which was de-bugging! submitted first try correct
#the initial assignement looked like this:
#print(Day 1 - string manipulation")
#print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
#print(("New lines can be created with a backslack and n.")
#solution:
#print("Day 1 - String Manipulation")
#print('String Concatenation is done with the "+" sign.')
#print('e.g. print("Hello " + "world")')
#print("New lines can be created with a backslash and n.")
#learning a new function called input("a prompt for the user") and this allows the user to interact with the code. only once the user interacts with the code, will the code be done
input("hello")
#once user presses enter, does the code continue to run, uses the information, and then code is done and you get the arrow again
#nesting functions: when one function is inside another
print("hello" + input("what is your name?"))
#ok exercise number 3, she wanted us to print the number of characters in a name, we had to look up a new function ourselves which counts numbers in a string, which was len(). So my answer was:
print(len(input("What is your name? ")))
#in her answer she had a space after the ? but it gave me a slight error? but still said it was 100% so idk 
#watching her solution, she DID add the space so it must have been a strange error
#you can input spaces inside of the functions to make it more clear
print( len( input("What is your name? ") ) )

#Variables are words assigned to functions / actions
name = input("What is your name?")
print(name)

# this was the last project in day 1:
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b 
b = c 

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
#4/9/2022
x = input("what is your name? ")
length = (len(x))
print("length of name: " + str(length) + " characters")
#if you want your variable to be multiple words, separate them by an underscore x_y
#you can use numbers in your variable name but they can't be at the beginning of the name
#this was the final project of Day 1 

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")
#2. Ask the user for the city that they grew up in.
city_name = input("What's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city_name + " " + pet_name)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
