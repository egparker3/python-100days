#this was the first project of Day 2: adding a two digit number 

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