# ============================================================
# Manejo de strings
# ============================================================
#
# COVER PAGE
#
# Student name: Luis Gabriel Hernandez Jasso
# Matricula: 2630218
# Group: 1
# Materia: Metodologias de la programacion  
#
# ============================================================
# EXECUTIVE SUMMARY
# ============================================================
#
# A string in Python is a data type used to store text.
# Strings are written between single or double quotation marks.
# Strings are immutable, which means their characters cannot be
# changed directly after the string has been created.
# Basic string operations include concatenation, length, slicing,
# searching, replacing, splitting, joining, and formatting text.
# Methods such as strip() and lower() help normalize user input.
# Input validation is important because it prevents invalid data
# from being processed by a program.
# This program contains six problems that demonstrate different
# string operations, validations, and transformations.
#
# ============================================================
# PRINCIPLES AND GOOD PRACTICES
# ============================================================
#
# Strings are immutable, so string methods create new strings
# instead of changing the original string directly.
#
# It is good practice to use strip() before validating user input
# because users can accidentally enter extra spaces.
#
# lower() can be used before comparing text when uppercase and
# lowercase letters should be considered equal.
#
# Avoid unexplained numbers in indexes and document what each
# slice extracts from a string.
#
# Built-in string methods should be used instead of rewriting
# operations that Python already provides.
#
# Validations should be performed in order. First check if the
# input is empty and then verify its format.
#
# Clear variable names and understandable error messages make
# programs easier to read and maintain.


# ============================================================
# PROBLEM 1: FULL NAME FORMATTER
# ============================================================
#
# Description:
# This program receives a full name and removes unnecessary spaces.
# It formats the name using title case and generates the initials
# using the first letter of every word.
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - The name cannot be empty after strip().
# - The name must contain at least two words.
# - A string containing only spaces is not accepted.
#
# Test cases:
# 1) Normal:
#    Input: "Luis Gabriel Hernandez"
#    Output: "Luis Gabriel Hernandez" and "L.G.H."
#
# 2) Border:
#    Input: "  Luis   Jasso  "
#    Output: "Luis Jasso" and "L.J."
#
# 3) Error:
#    Input: "   "
#    Output: "Error: invalid name"
#
# Key operations:
# strip(), split(), join(), title(), len(), indexing
# ============================================================

full_name = input("Enter your full name: ")

# Remove spaces at the beginning and end
full_name = full_name.strip()

# Validate that the name is not empty
if full_name == "":
    print("Error: invalid name")

else:
    # Separate the name into words
    name_parts = full_name.split()

    # Validate that the name contains at least two words
    if len(name_parts) < 2:
        print("Error: enter at least two words")

    else:
        # Join the words again and format them
        formatted_name = " ".join(name_parts).title()

        # Create the initials
        initials = ""

        for word in name_parts:
            initials = initials + word[0].upper() + "."

        # Display results
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")


# ============================================================
# PROBLEM 2: SIMPLE EMAIL VALIDATOR
# ============================================================
#
# Description:
# This program performs a basic validation of an email address.
# The email must contain exactly one '@', cannot contain spaces,
# and the domain must contain at least one period.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email: true"
# - "Valid email: false"
# - "Domain: <domain_part>" if the email is valid.
#
# Validations:
# - The email cannot be empty after strip().
# - It must contain exactly one '@'.
# - It cannot contain spaces.
# - There must be text before and after '@'.
# - The domain must contain at least one '.'.
#
# Test cases:
# 1) Normal:
#    Input: "luis@gmail.com"
#    Output: "Valid email: true"
#            "Domain: gmail.com"
#
# 2) Border:
#    Input: "  alumno@school.com  "
#    Output: "Valid email: true"
#            "Domain: school.com"
#
# 3) Error:
#    Input: "luisgmail.com"
#    Output: "Valid email: false"
#
# Key operations:
# strip(), count(), find(), slicing, in, not in
# ============================================================

email_text = input("Enter an email address: ")

# Remove spaces at the beginning and end
email_text = email_text.strip()

# First validations
if (
    email_text != ""
    and email_text.count("@") == 1
    and " " not in email_text
):

    # Find the position of @
    at_position = email_text.find("@")

    # Extract the part before @
    local_part = email_text[:at_position]

    # Extract everything after @
    domain_part = email_text[at_position + 1:]

    # Validate local part and domain
    if (
        local_part != ""
        and domain_part != ""
        and "." in domain_part
        and not domain_part.startswith(".")
        and not domain_part.endswith(".")
    ):
        print("Valid email: true")
        print(f"Domain: {domain_part}")

    else:
        print("Valid email: false")

else:
    print("Valid email: false")


# ============================================================
# PROBLEM 3: PALINDROME CHECKER
# ============================================================
#
# Description:
# This program determines whether a phrase is a palindrome.
# A palindrome reads the same from left to right and from right
# to left. Spaces and uppercase/lowercase differences are ignored.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - "Is palindrome: true"
# - "Is palindrome: false"
# - "Normalized phrase: <text>"
#
# Validations:
# - The phrase cannot be empty after strip().
# - The normalized phrase must contain at least 3 characters.
#
# Test cases:
# 1) Normal:
#    Input: "Anita lava la tina"
#    Output: "Is palindrome: true"
#
# 2) Border:
#    Input: "oso"
#    Output: "Is palindrome: true"
#
# 3) Error:
#    Input: "  "
#    Output: "Error: invalid phrase"
#
# Key operations:
# strip(), lower(), replace(), len(), slicing, ==
# ============================================================

phrase = input("Enter a phrase: ")

# Validate empty input
if phrase.strip() == "":
    print("Error: invalid phrase")

else:
    # Convert to lowercase and remove spaces
    normalized_phrase = phrase.lower().replace(" ", "")

    # Validate minimum length
    if len(normalized_phrase) < 3:
        print("Error: the phrase must have at least 3 characters")

    else:
        # Reverse the normalized phrase
        reversed_phrase = normalized_phrase[::-1]

        # Compare both strings
        if normalized_phrase == reversed_phrase:
            print("Is palindrome: true")

        else:
            print("Is palindrome: false")

        print(f"Normalized phrase: {normalized_phrase}")


# ============================================================
# PROBLEM 4: SENTENCE WORD STATS
# ============================================================
#
# Description:
# This program receives a sentence and separates it into words.
# It displays the total number of words, the first word, the last
# word, the shortest word, and the longest word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Word count: <n>"
# - "First word: <word>"
# - "Last word: <word>"
# - "Shortest word: <word>"
# - "Longest word: <word>"
#
# Validations:
# - The sentence cannot be empty after strip().
# - At least one word must exist after split().
#
# Test cases:
# 1) Normal:
#    Input: "Python makes coding fun"
#    Output:
#    Word count: 4
#    First word: Python
#    Last word: fun
#
# 2) Border:
#    Input: "  Hello  "
#    Output:
#    Word count: 1
#
# 3) Error:
#    Input: "   "
#    Output: "Error: invalid sentence"
#
# Key operations:
# strip(), split(), len(), indexing
# ============================================================

sentence = input("Enter a sentence: ")

# Remove external spaces
sentence = sentence.strip()

# Validate the sentence
if sentence == "":
    print("Error: invalid sentence")

else:
    # Separate the sentence into words
    words = sentence.split()

    # First and last words
    first_word = words[0]
    last_word = words[-1]

    # Start using the first word as shortest and longest
    shortest_word = words[0]
    longest_word = words[0]

    # Compare each word
    for word in words:

        if len(word) < len(shortest_word):
            shortest_word = word

        if len(word) > len(longest_word):
            longest_word = word

    # Display results
    print(f"Word count: {len(words)}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# ============================================================
# PROBLEM 5: PASSWORD STRENGTH CLASSIFIER
# ============================================================
#
# Description:
# This program analyzes a password and classifies it as weak,
# medium, or strong according to its length and the types of
# characters that it contains.
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - The password cannot be empty.
# - The password length is checked using len().
#
# Rules:
# - Weak:
#   Less than 8 characters.
#
# - Medium:
#   At least 8 characters and contains at least two different
#   character types.
#
# - Strong:
#   At least 8 characters and contains an uppercase letter,
#   lowercase letter, digit, and symbol.
#
# Test cases:
# 1) Normal:
#    Input: "Hello123!"
#    Output: "Password strength: strong"
#
# 2) Border:
#    Input: "Password"
#    Output: "Password strength: medium"
#
# 3) Error:
#    Input: ""
#    Output: "Error: password cannot be empty"
#
# Key operations:
# len(), isupper(), islower(), isdigit(), isalnum()
# ============================================================

password_input = input("Enter a password: ")

# Validate empty password
if password_input.strip() == "":
    print("Error: password cannot be empty")

else:
    # Boolean flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    # Check every character
    for character in password_input:

        if character.isupper():
            has_upper = True

        elif character.islower():
            has_lower = True

        elif character.isdigit():
            has_digit = True

        elif not character.isalnum():
            has_symbol = True

    # Count how many character types are present
    character_types = 0

    if has_upper:
        character_types += 1

    if has_lower:
        character_types += 1

    if has_digit:
        character_types += 1

    if has_symbol:
        character_types += 1

    # Classify the password
    if len(password_input) < 8:
        password_strength = "weak"

    elif (
        has_upper
        and has_lower
        and has_digit
        and has_symbol
    ):
        password_strength = "strong"

    elif character_types >= 2:
        password_strength = "medium"

    else:
        password_strength = "weak"

    print(f"Password strength: {password_strength}")


# ============================================================
# PROBLEM 6: PRODUCT LABEL FORMATTER
# ============================================================
#
# Description:
# This program receives a product name and its price and creates
# a label using a fixed width of exactly 30 characters.
# If the label is longer, it is truncated. If it is shorter,
# spaces are added at the end.
#
# Inputs:
# - product_name (string)
# - price_text (string that must represent a positive number)
#
# Outputs:
# - 'Label: "<exactly 30 characters>"'
# - "Length: 30"
#
# Validations:
# - The product name cannot be empty.
# - The price cannot be empty.
# - The price must be numeric.
# - The price must be greater than zero.
#
# Test cases:
# 1) Normal:
#    Product: "Notebook"
#    Price: "25.50"
#    Output: label with exactly 30 characters
#
# 2) Border:
#    Product: "Pen"
#    Price: "1"
#    Output: label completed with spaces until 30 characters
#
# 3) Error:
#    Product: "Pen"
#    Price: "zero"
#    Output: "Error: invalid price"
#
# Key operations:
# f-strings, len(), slicing, concatenation, *
# ============================================================

# Constant for the required label size
LABEL_WIDTH = 30

product_name = input("Enter a product name: ")
price_text = input("Enter a positive price: ")

# Normalize inputs
product_name = product_name.strip()
price_text = price_text.strip()

# Validate product name
if product_name == "":
    print("Error: product name cannot be empty")

# Validate price input
elif price_text == "":
    print("Error: invalid price")

else:

    # Try to convert the price to a number
    try:
        price_value = float(price_text)

        # Validate positive price
        if price_value <= 0:
            print("Error: invalid price")

        else:
            # Create the original label
            label = (
                f"Product: {product_name} | "
                f"Price: ${price_value:.2f}"
            )

            # If the label is longer than 30 characters,
            # keep only the first 30 characters
            if len(label) > LABEL_WIDTH:
                label = label[:LABEL_WIDTH]

            # If the label is shorter than 30 characters,
            # add the necessary spaces at the end
            elif len(label) < LABEL_WIDTH:
                missing_spaces = LABEL_WIDTH - len(label)
                label = label + (" " * missing_spaces)

            # Display the label between quotation marks
            print(f'Label: "{label}"')
            print(f"Length: {len(label)}")

    # This error occurs if the price cannot be converted to float
    except ValueError:
        print("Error: invalid price")


# ============================================================
# CONCLUSIONS
# ============================================================
#
# Strings are essential in programming because a large amount of
# user input and program output is represented as text.
# Methods such as strip(), lower(), split(), join(), and replace()
# make it easier to clean and transform text.
# Normalizing text before comparing it helps avoid problems caused
# by extra spaces or differences between uppercase and lowercase.
# Input validation prevents incorrect or empty data from being
# processed by a program.
# I also learned that strings in Python are immutable, so operations
# on strings normally create new strings instead of changing them.
# Slicing is useful for extracting, reversing, and limiting text.
# These tools help create programs that are clearer and more reliable.


# ============================================================
# REFERENCES
# ============================================================
#
# 1. Python Software Foundation.
#    Built-in Types - Text Sequence Type - str.
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# 2. Python Software Foundation.
#    An Informal Introduction to Python - Strings.
#    https://docs.python.org/3/tutorial/introduction.html#strings
#
# 3. Python Software Foundation.
#    Built-in Functions.
#    https://docs.python.org/3/library/functions.html
#
# 4. Python Software Foundation.
#    The Python Tutorial - Data Structures.
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 5. Python Software Foundation.
#    Input and Output.
#    https://docs.python.org/3/tutorial/inputoutput.html
#
