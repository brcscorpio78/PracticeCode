import random
import string


# Function to generate a random character
def random_char():
    return random.choice(string.ascii_letters)

#Generate a list of random characters
characters = [random_char() for _ in range(12)] # Adjust the range for the desired length

#Shuffle the characters
random.shuffle(characters)

# Combine the shuffled characters into a password
password = ''.join(characters)

# Output the password
print(password)
