# ============================================================
# Manejo de numeros y boleanos
# ============================================================
#
# COVER PAGE
#
# Nombre: Luis Gabriel Hernandez Jasso
# Matricula : 2630218
# Group: 1
# Materia : Metodologias de la programacion 
# ============================================================
# EXECUTIVE SUMMARY
# ============================================================
#
# Python has different numeric data types that are useful for
# performing calculations. The int type represents whole numbers,
# while the float type represents numbers that can contain decimals.
# Boolean values can only be True or False and are commonly obtained
# from comparisons between values.
# Arithmetic, relational, and logical operators allow programs to
# perform calculations and make decisions.
# It is important to validate numeric input before using it to avoid
# errors such as invalid conversions or division by zero.
# This program contains six problems that use integers, floats,
# booleans, comparisons, calculations, and input validation.
#
# ============================================================
# PRINCIPLES AND GOOD PRACTICES
# ============================================================
#
# Use int for values that normally represent whole numbers.
#
# Use float when a value can contain decimal numbers.
#
# Boolean values represent True or False conditions and are useful
# for making decisions inside a program.
#
# Input data should be validated before performing calculations.
#
# Division by zero must always be avoided because it produces
# an error in the program.
#
# Intermediate results should be stored in variables instead of
# repeating complex calculations.
#
# Variable names should clearly describe the information they store.
#
# Boolean variables should have names that explain what True and
# False represent, such as is_eligible or has_overtime.


# ============================================================
# PROBLEM 1: TEMPERATURE CONVERTER AND RANGE FLAG
# ============================================================
#
# Description:
# This program converts a temperature from Celsius to Fahrenheit
# and Kelvin. It also determines whether the Celsius temperature
# is considered high.
#
# Inputs:
# - temp_c (float): temperature in degrees Celsius.
#
# Outputs:
# - "Fahrenheit: <temp_f>"
# - "Kelvin: <temp_k>"
# - "High temperature: true|false"
#
# Validations:
# - The input must be convertible to float.
# - The Kelvin temperature cannot be below 0.
#
# Test cases:
# 1) Normal:
#    Input: 35
#    Fahrenheit: 95.0
#    Kelvin: 308.15
#    High temperature: true
#
# 2) Border:
#    Input: 30
#    High temperature: true
#
# 3) Error:
#    Input: -300
#    Output: "Error: invalid input"
#
# Key operations:
# float(), arithmetic operations, >=, boolean comparison
# ============================================================

try:
    temp_c = float(input("Enter temperature in Celsius: "))

    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15

    # Validate physical temperature
    if temp_k < 0.0:
        print("Error: invalid input")

    else:
        # Boolean comparison
        is_high_temperature = temp_c >= 30.0

        print(f"Fahrenheit: {round(temp_f, 2)}")
        print(f"Kelvin: {round(temp_k, 2)}")
        print(f"High temperature: {str(is_high_temperature).lower()}")

except ValueError:
    print("Error: invalid input")


# ============================================================
# PROBLEM 2: WORK HOURS AND OVERTIME PAYMENT
# ============================================================
#
# Description:
# This program calculates the weekly payment of a worker.
# The first 40 hours are paid at the normal hourly rate.
# Additional hours are paid at 150 percent of the normal rate.
#
# Inputs:
# - hours_worked (float)
# - hourly_rate (float)
#
# Outputs:
# - "Regular pay: <regular_pay>"
# - "Overtime pay: <overtime_pay>"
# - "Total pay: <total_pay>"
# - "Has overtime: true|false"
#
# Validations:
# - hours_worked must be greater than or equal to 0.
# - hourly_rate must be greater than 0.
#
# Test cases:
# 1) Normal:
#    Hours: 45
#    Rate: 100
#    Has overtime: true
#
# 2) Border:
#    Hours: 40
#    Rate: 100
#    Has overtime: false
#
# 3) Error:
#    Hours: -5
#    Rate: 100
#    Output: "Error: invalid input"
#
# Key operations:
# min(), max(), multiplication, comparison, boolean
# ============================================================

try:
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    # Validate inputs
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")

    else:
        # Separate regular and overtime hours
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        # Calculate payments
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5

        total_pay = regular_pay + overtime_pay

        # Boolean value
        has_overtime = hours_worked > 40

        print(f"Regular pay: {round(regular_pay, 2)}")
        print(f"Overtime pay: {round(overtime_pay, 2)}")
        print(f"Total pay: {round(total_pay, 2)}")
        print(f"Has overtime: {str(has_overtime).lower()}")

except ValueError:
    print("Error: invalid input")


# ============================================================
# PROBLEM 3: DISCOUNT ELIGIBILITY WITH BOOLEANS
# ============================================================
#
# Description:
# This program determines whether a customer is eligible for
# a 10 percent discount.
# A customer receives the discount if the customer is a student,
# is a senior, or has a purchase total of at least 1000.
#
# Inputs:
# - purchase_total (float)
# - is_student_text (string: YES or NO)
# - is_senior_text (string: YES or NO)
#
# Outputs:
# - "Discount eligible: true|false"
# - "Final total: <final_total>"
#
# Validations:
# - purchase_total must be greater than or equal to 0.
# - Student input must be YES or NO.
# - Senior input must be YES or NO.
#
# Test cases:
# 1) Normal:
#    Purchase: 500
#    Student: YES
#    Senior: NO
#    Discount eligible: true
#
# 2) Border:
#    Purchase: 1000
#    Student: NO
#    Senior: NO
#    Discount eligible: true
#
# 3) Error:
#    Purchase: 500
#    Student: MAYBE
#    Senior: NO
#    Output: "Error: invalid input"
#
# Key operations:
# float(), upper(), ==, or, boolean comparison
# ============================================================

try:
    purchase_total = float(input("Enter purchase total: "))

    is_student_text = input("Are you a student? (YES/NO): ")
    is_senior_text = input("Are you a senior? (YES/NO): ")

    # Normalize text
    is_student_text = is_student_text.strip().upper()
    is_senior_text = is_senior_text.strip().upper()

    # Validate inputs
    if purchase_total < 0:
        print("Error: invalid input")

    elif (
        is_student_text not in ("YES", "NO")
        or is_senior_text not in ("YES", "NO")
    ):
        print("Error: invalid input")

    else:
        # Convert text comparisons to boolean values
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        # Determine discount eligibility
        discount_eligible = (
            is_student
            or is_senior
            or purchase_total >= 1000.0
        )

        # Calculate final total
        if discount_eligible:
            final_total = purchase_total * 0.90

        else:
            final_total = purchase_total

        print(
            f"Discount eligible: "
            f"{str(discount_eligible).lower()}"
        )
        print(f"Final total: {round(final_total, 2)}")

except ValueError:
    print("Error: invalid input")


# ============================================================
# PROBLEM 4: BASIC STATISTICS OF THREE INTEGERS
# ============================================================
#
# Description:
# This program receives three integer numbers and calculates
# their sum, average, maximum value, and minimum value.
# It also determines whether all three numbers are even.
#
# Inputs:
# - n1 (int)
# - n2 (int)
# - n3 (int)
#
# Outputs:
# - "Sum: <sum_value>"
# - "Average: <average_value>"
# - "Max: <max_value>"
# - "Min: <min_value>"
# - "All even: true|false"
#
# Validations:
# - All three values must be convertible to int.
# - Negative numbers are allowed.
#
# Test cases:
# 1) Normal:
#    Input: 4, 8, 12
#    All even: true
#
# 2) Border:
#    Input: 0, 0, 0
#    Sum: 0
#    Average: 0.0
#    All even: true
#
# 3) Error:
#    Input: 5, hello, 10
#    Output: "Error: invalid input"
#
# Key operations:
# int(), +, /, max(), min(), %, and
# ============================================================

try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))

    # Calculate sum
    sum_value = n1 + n2 + n3

    # Calculate average
    average_value = sum_value / 3

    # Find maximum and minimum
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    # Check if all numbers are even
    all_even = (
        n1 % 2 == 0
        and n2 % 2 == 0
        and n3 % 2 == 0
    )

    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")

except ValueError:
    print("Error: invalid input")


# ============================================================
# PROBLEM 5: LOAN ELIGIBILITY
# ============================================================
#
# Description:
# This program determines whether a person is eligible for a loan.
# The decision is based on monthly income, monthly debt,
# debt ratio, and credit score.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - "Debt ratio: <debt_ratio>"
# - "Eligible: true|false"
#
# Validations:
# - monthly_income must be greater than 0.
# - monthly_debt must be greater than or equal to 0.
# - credit_score must be greater than or equal to 0.
# - Income cannot be zero because it is used as a divisor.
#
# Eligibility rules:
# - monthly_income >= 8000.0
# - debt_ratio <= 0.4
# - credit_score >= 650
#
# Test cases:
# 1) Normal:
#    Income: 10000
#    Debt: 2000
#    Credit score: 700
#    Eligible: true
#
# 2) Border:
#    Income: 8000
#    Debt: 3200
#    Credit score: 650
#    Debt ratio: 0.4
#    Eligible: true
#
# 3) Error:
#    Income: 0
#    Debt: 1000
#    Credit score: 700
#    Output: "Error: invalid input"
#
# Key operations:
# float(), int(), division, >=, <=, and
# ============================================================

try:
    monthly_income = float(
        input("Enter monthly income: ")
    )

    monthly_debt = float(
        input("Enter monthly debt: ")
    )

    credit_score = int(
        input("Enter credit score: ")
    )

    # Validate input before division
    if (
        monthly_income <= 0
        or monthly_debt < 0
        or credit_score < 0
    ):
        print("Error: invalid input")

    else:
        # Calculate debt ratio
        debt_ratio = monthly_debt / monthly_income

        # Determine loan eligibility
        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print(f"Debt ratio: {round(debt_ratio, 2)}")
        print(f"Eligible: {str(eligible).lower()}")

except ValueError:
    print("Error: invalid input")


# ============================================================
# PROBLEM 6: BODY MASS INDEX AND CATEGORY FLAGS
# ============================================================
#
# Description:
# This program calculates Body Mass Index (BMI) using a person's
# weight in kilograms and height in meters.
# It also creates boolean values to identify the BMI category.
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - "BMI: <bmi>"
# - "Underweight: true|false"
# - "Normal: true|false"
# - "Overweight: true|false"
#
# Validations:
# - weight_kg must be greater than 0.
# - height_m must be greater than 0.
# - Height cannot be zero because it is used in division.
#
# BMI categories:
# - Underweight: BMI < 18.5
# - Normal: 18.5 <= BMI < 25.0
# - Overweight: BMI >= 25.0
#
# Test cases:
# 1) Normal:
#    Weight: 70
#    Height: 1.75
#    BMI: 22.86
#    Normal: true
#
# 2) Border:
#    Weight: 74
#    Height: 2
#    BMI: 18.5
#    Normal: true
#
# 3) Error:
#    Weight: 70
#    Height: 0
#    Output: "Error: invalid input"
#
# Key operations:
# float(), division, multiplication, round(), comparisons
# ============================================================

try:
    weight_kg = float(
        input("Enter weight in kilograms: ")
    )

    height_m = float(
        input("Enter height in meters: ")
    )

    # Validate values before calculating BMI
    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")

    else:
        # Calculate BMI
        bmi = weight_kg / (height_m * height_m)

        # Boolean category flags
        is_underweight = bmi < 18.5

        is_normal = (
            bmi >= 18.5
            and bmi < 25.0
        )

        is_overweight = bmi >= 25.0

        # Display results
        print(f"BMI: {round(bmi, 2)}")

        print(
            f"Underweight: "
            f"{str(is_underweight).lower()}"
        )

        print(
            f"Normal: "
            f"{str(is_normal).lower()}"
        )

        print(
            f"Overweight: "
            f"{str(is_overweight).lower()}"
        )

except ValueError:
    print("Error: invalid input")


# ============================================================
# CONCLUSIONS
# ============================================================
#
# Integers and floating-point numbers can be used together to
# solve different types of real-world calculations in Python.
# Comparisons between numeric values generate boolean values,
# which can be used with if statements to make decisions.
# Validating ranges before performing calculations helps prevent
# incorrect results and errors such as division by zero.
# Logical operators such as and, or, and not make it possible
# to combine multiple conditions in a single decision.
# I learned how int, float, and bool can work together in
# calculations involving salaries, discounts, loans, and BMI.
# These concepts are useful for creating programs that analyze
# information and make decisions based on specific rules.


# ============================================================
# REFERENCES
# ============================================================
#
# 1. Python Software Foundation.
#    Built-in Types - Numeric Types: int, float, complex.
#    https://docs.python.org/3/library/stdtypes.html
#
# 2. Python Software Foundation.
#    Boolean Operations - and, or, not.
#    https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
#
# 3. Python Software Foundation.
#    Built-in Functions.
#    https://docs.python.org/3/library/functions.html
#
# 4. Python Software Foundation.
#    An Informal Introduction to Python - Numbers.
#    https://docs.python.org/3/tutorial/introduction.html#numbers
#
# 5. Python Software Foundation.
#    More Control Flow Tools.
#    https://docs.python.org/3/tutorial/controlflow.html
