# Random Password Generator 06/10/2024

import string
import random

# Define the character sets: lowercase, uppercase, digits, and special characters
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

# Combine all the character sets into a single pool
character_pool = lowercase_letters + uppercase_letters + digits + special_characters

# Ask the user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate the password by randomly selecting characters from the pool
password = ''.join(random.choices(character_pool, k=password_length))

# Display the generated password
print("Generated Password:", password)
