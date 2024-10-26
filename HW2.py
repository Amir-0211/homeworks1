          #NUMBER DATA TYPE


#1

num = float(input("Enter a number: "))
rounded = round(num, 2)
print("Rounded number: ", rounded)


#2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
print("Largest number: ", largest)
print("Smallest number: ", smallest)


#3

km = float(input("Enter the distance: "))
m= km * 1000 #meter
cm = m * 100
print( km, "kilometers is ",m, "meters or ",cm, "centimeters")

#4

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
int_div = num1 // num2
rem = num1 % num2
print(f"Integer division: {int_div}")
print(f"Remainder: {rem}")

#5

cel= float(input("Enter the temperature: "))
fah = (cel * 9/5) + 32
print(f"{cel}°C is {fah}°F.")

#6

num = int(input("Enter a number: "))
last_digit = num % 10
print(f"The last digit of {num} is {last_digit}.")

#7

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

#8

a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")




           #STRING DATA TYPE



#1

sen = input("Enter a sentence: ")
cap = sen.title()
print(f"Capitalized: {cap}")

#2

str = input("Enter a string: ")
vowels = "asdfpYbSRJ"
no_vowels = ''.join(char for char in str if char not in vowels)
print(f"String without vowels: {no_vowels}")

#3

str = input("Enter a string: ")
reversed= str[::-1]
print(f"Reversed: {reversed}")

#4

str = input("Enter a string: ")
underscored = str.replace(" ", "_")
print(f"Modified string: {underscored}")

#5

w = input("Enter a word: ")
if w == w[::-1]:
    print(f"{w} is a palindrome.")
else:
    print(f"{w} is not a palindrome.")

#6

str = input("Enter a string: ")
modified_string = str.replace("a", "o").replace("A", "O")
print(f"Modified string: {modified_string}")

#7

email = input("Enter your email address: ")
name = email.split('@')[0]
print(f"Username: {name}")

#8

str = input("Enter a string: ")
title_case = str.title()
print(f"Title Case: {title_case}")

#9

str = input("Enter a string: ")
modified_string = str[1:-1]
print(f"Modified string: {modified_string}")

#10

sent = input("Enter a sentence: ")
word = input("Enter a word to search: ")
if word in sent:
    print(f"'{word}' is present in the sentence.")
else:
    print(f"'{word}' is not present in the sentence.")

#11

str = input("Enter a string: ")
char = input("Enter the character to find: ")
pos = str.find(char)
if pos != -1:
    print(f"First occurrence of '{char}' is at position {pos}.")
else:
    print(f"'{char}' not found in the string.")

#12

str = input("Enter a string: ")
last_3 = str[-3:]
print(f"Last three characters: {last_3}")

#13

str = input("Enter a string: ")
times = int(input("Enter the number of times to repeat: "))
repeated = str * times
print(repeated)

#14

sent = input("Enter a sentence: ")
words = sent.split()
for word in words:
    print(word)

#15

str = input("Enter a string: ")
even_position_letters = str[1::2] 
print(f"Letters at even positions: {even_position_letters}")

#16

str = input("Enter a string: ")
formatted = f"Title: {str}"
print(formatted)

#17

sent = input("Enter a sentence: ")
words = sent.split()
reversed = ' '.join(reversed(words))
print(f"Reversed sentence: {reversed}")

#18

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
difference = abs(len(str1) - len(str2))
print(f"Difference in length: {difference}")




                  #BOOLEAN DATA TYPE



#1

username = input("Enter username: ")
password = input("Enter password: ")
if username and password:
    print("Both username and password are provided.")
else:
    print("Username or password cannot be empty.")

#2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 == num2:
    print("The two numbers are equal.")
else:
    print("The two numbers are not equal.")

#3

num = int(input("Enter a number: "))
if number > 0 and num % 2 == 0:
    print(f"{num} is positive and even.")
else:
    print(f"{num} is not positive and even.")

#4

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 != num2 and num1 != num3 and num2 != num3:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")

#5

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if len(str1) == len(str2):
    print("Both strings have the same length.")
else:
    print("The strings have different lengths.")

#6

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")

#7

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 + num2 > 50:
    print("The sum of the two numbers is greater than 50.")
else:
    print("The sum of the two numbers is not greater than 50.")

#8

num = int(input("Enter a number: "))
if 10 <= num <= 20:
    print(f"{num} is between 10 and 20.")
else:
    print(f"{num} is not between 10 and 20.")