# Daniel Keuning
# UWYO COSC 1010
# Submission Date: 11/19/2024
# Lab 10
# Lab Section: 11
# Sources, people worked with, help given to: 
#   - Used ChatGPT to interpret the get_hash() function and what the heck it was doing.
#   - After I figured that out, everything else was pretty simple 


#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

print(get_hash('gopokes'))

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

try:
    hash_file = open('hash', 'r') 
    actual_password = hash_file.read().strip()

except FileNotFoundError:
    print("Error: File Not Found.")
    quit

try:
    passwords_file = open('rockyou.txt', 'r')
    passwords_list = []
    for line in passwords_file:
        line = line.strip()
        passwords_list.append(line)

except FileNotFoundError:
    print("Error: File Not Found.")
    quit

try:
    for password in passwords_list:
        password_hashed = get_hash(password).strip()
        if password_hashed == actual_password:
            print(f"Password: {password}")

except:
    print("No Password Found.")
