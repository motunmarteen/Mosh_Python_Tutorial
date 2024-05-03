# # # import math

# # # # Print Function in Python
# # # full_name = "Motun Marteen"
# # # age = 20
# # # is_newPatient = True

# # # print(full_name)
# # # print(age)
# # # print(is_newPatient)

# # # # Input Function in Python
# # # name = input("What is your name? ")
# # # color = input("What is your favorite color? ")
# # # print(name + " likes " + color)

# # # # Age and type casting
# # # birthYear = int(input("What is your birth year? "))
# # # age = 2024 - birthYear
# # # print(age)

# # # # Conversion of pounds to kg
# # # weight = float(input("what is your weight in pounds? "))
# # # convertedWeight = weight * 0.453592
# # # print(convertedWeight)

# # # # Using Quotation, Doc String in Python and Indexing
# # # # The square bracket is [:] is used to copy as well in python
# # # course = "Python's Course for Beginners"
# # # another = course[:]
# # # print(course)
# # # print(another)

# # # docString = '''
# # # Hi Motun,

# # # How are you doing today and how much do you want to earn from the contract?
# # # '''
# # # print(docString)

# # # # Using indexing
# # # name = 'Jennifer'
# # # print(name[1:-1])

# # # # Formatted Strings - Using Curly braces and the F-String
# # # first_name = "Motun"
# # # last_name = "Marteen"
# # # msg = f"{first_name} [{last_name}] is a coder"
# # # print(msg)

# # # # String Methods
# # # course = "Python for Beginners"
# # # print(len(course))
# # # # Prints ---- 20 because there are 20 characters in the sentence including spaces
# # # # Using the len() can help to force a limit of character from user when passing data

# # # print(course.upper())
# # # # Prints PYTHON FOR BEGINNERS

# # # print(course.lower())
# # # # Prints python for beginners

# # # print(course.find("P"))
# # # # Prints 0 because this is the first letter of the sentence and 
# # # # it starts with the index 0

# # # print(course.find("O"))
# # # # Prints -1 because uppercase O can not be found in the sentence

# # # print(course.find("Beginners"))
# # # # prints 11 because the letter B in beginners starts the beginners word

# # # print(course.replace("Beginners", "Absolute Beginners"))
# # # # Prints --- Python for Absolute Beginners

# # # print(course.replace("beginners", "Absolute Beginners"))
# # # # Prints --- Python for Beginners because the find letter starts with
# # # # capital letter B not b

# # # print(course.find("P", "J"))
# # # # Print Jython for Beginners because it sees the letter P in it as Capital letter

# # # print("Python" in course)
# # # # prints True because it is still same as the capitalised P

# # # # Note that the "find" method produces the index while the "in" method 
# # # # produces boolean result

# # # # Math operator
# # # # +, -, /, //, *, **, %

# # # # Assignment Operator
# # # x = 10
# # # x-=3
# # # print(x)
# # # # -=, +=, *=, /=


# # # # DAY 3
 
# # #  xxx = 10 + 3 * 2 ** 2
# # #  print(xxx)
# # # #  =22
 
# # #  xx = (2 + 3) * 10 - 3
# # # #  =47
# # # #  Using PEMDAS - LR
# # # # Parenthesis, Exponential, Multiplication, Division, Addition, Subtraction -- All from left to right

# # # x = 2.9
# # # print(round(x))
# # # # 3 will be printed

# # # print(abs(-2.9))
# # # # 2.9 will be printed

# # # # Absolute function will return positive representation even if the value passed to it is negative
# # # # The absolute function

# # # # math module and importation
# # # print(math.ceil(2.9))
# # # # will print 3

# # # print(math.floor(2.9))
# # # # will print 2

# # # If statements
# # is_hot = True
# # is_cold = False

# # if is_hot:
# #     print("It is a hot day, drink plenty of water")
# # elif is_cold:
# #     print("It is a cold day, wear warm clothes")
# # else:
# #     print("It is a lovely day")
# # print("Enjoy your day!")

# # Conditional statement

# is_good_credit = False
# price = 1000000

# if is_good_credit:
#     print(f"You will need to put down ${price/10} as down payment")
# else:
#     print(f"You will need to put down ${price/5} as down payment")
    
# Logical Operators AND, OR

# =============AND==============

# has_high_income = True
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# # ===========OR==============
   
# has_high_incomes = False
# has_good_credits = True
 
# if has_high_incomes or has_good_credits:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# # ================NOT==================

# has_good_creditt = True
# has_criminal_record = True
 
# if has_good_creditt and not has_criminal_record:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# # AND : both
# # OR : at least one
# # NOT : reverses the value to True or False

# # Comparison Operators
# # >, <, >=, <=, ==, !=
# # Assignment operator has only one equal sign (=)
# # while comparison operator has two equal signs (==)
 
 
# name = input("What is your name? ")
# length_name = len(name)

# if length_name < 3:
#     print("Name must be at least 3 characters")
# elif length_name > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good")


# Day 4
# 01:16:17 Weight Converter Program 
# 01:20:43 While Loops
# 01:24:07 Building a Guessing Game
# 01:30:51 Building the Car Game
# 01:41:48 For Loops

# A program that converts Pound to Kg and Kg to Pounds

weight = float(input("Weight: "))

kilogram = weight / 0.45
pounds = weight * 0.45

unit = input("(L)bs or (K)g: ").upper()

if unit == "L":
    print(f"You are {pounds} kilos")
elif unit == "K":
    print(f"You are {kilogram} pounds")
else:
    print("incorrect input")