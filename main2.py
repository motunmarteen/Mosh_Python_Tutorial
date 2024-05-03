# Develop a Python script that calculates the age of a person based on their birth year and the current year.

birthYear = int(input("What year were you born? "))
currentYear = int(input("What is the current year? "))
age = currentYear - birthYear
if birthYear and currentYear >= 2024:
    print("Incorrect input")
else:
    print(f"You are {age} years old")

# Modify the age calculation program to handle invalid inputs (e.g., non-numeric birth year).


