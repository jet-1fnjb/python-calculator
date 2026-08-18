# ==========================================
# Python Calculator
# ==========================================
# Description:
# A simple command-line calculator written
# in Python.
#
# The calculator can perform:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
#
# Author: jet-1fnjb
# ==========================================


# ------------------------------------------
# Addition function
# ------------------------------------------
# This function receives two numbers and
# returns their sum.
def add(a, b):
    return a + b


# ------------------------------------------
# Subtraction function
# ------------------------------------------
# This function receives two numbers and
# returns the difference.
def subtract(a, b):
    return a - b


# ------------------------------------------
# Multiplication function
# ------------------------------------------
# This function receives two numbers and
# returns their product.
def multiply(a, b):
    return a * b


# ------------------------------------------
# Division function
# ------------------------------------------
# This function receives two numbers and
# returns the result of the division.
#
# We check if the second number is zero
# because dividing by zero causes an error.
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."

    return a / b


# ------------------------------------------
# Main calculator program
# ------------------------------------------
# The while loop keeps the calculator
# running until the user chooses option 5.
while True:

    # Display the calculator menu.
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Ask the user to choose an operation.
    choice = input("Choose an option (1-5): ")

    # If the user chooses 5, stop the program.
    if choice == "5":
        print("Goodbye!")
        break

    # Check whether the user's choice is valid.
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        continue

    # ------------------------------------------
    # Get numbers from the user
    # ------------------------------------------
    # try/except prevents the program from
    # crashing if the user enters text instead
    # of a number.
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Please enter valid numbers.")
        continue

    # ------------------------------------------
    # Perform the selected operation
    # ------------------------------------------

    # Addition
    if choice == "1":
        result = add(num1, num2)
        print(f"Result: {result}")

    # Subtraction
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"Result: {result}")

    # Multiplication
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"Result: {result}")

    # Division
    elif choice == "4":
        result = divide(num1, num2)
        print(f"Result: {result}")