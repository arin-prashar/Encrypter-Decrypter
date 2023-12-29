# Vigenere Cipher
import random
import json


def generate_random_key(length):
    # Create the output variable
    output = ""
    # write to json file
    # Loop through the length
    for i in range(length):
        # Generate a random character
        random_character = chr(random.randint(32, 126))

        # Add the random character to the output
        output += random_character

    with open('key.json','w') as f:
        json.dump(output,f)
    # Return the output
    return output

def encrypt(text):
    # Create the output variable
    output = ""

    key=generate_random_key(len(text))

    # Loop through each character in the text
    for i in range(len(text)):
        # Get the character at index i
        character = text[i]

        # Get the character code of the character at index i
        character_code = ord(character)

        # Get the key at index i
        key_character = key[i % len(key)]

        # Get the key character code of the key character at index i
        key_character_code = ord(key_character)

        # Add the character code and the key character code
        sum = character_code + key_character_code

        # Add the sum to the output
        output += chr(sum)

    # Return the output
    return output

def decrypt(text,key):
    # Create the output variable
    output = ""
    # Loop through each character in the text
    for i in range(len(text)):
        # Get the character at index i
        character = text[i]

        # Get the character code of the character at index i
        character_code = ord(character)

        # Get the key at index i
        key_character = key[i % len(key)]

        # Get the key character code of the key character at index i
        key_character_code = ord(key_character)

        # Subtract the key character code from the character code
        difference = character_code - key_character_code

        # Add the difference to the output
        output += chr(difference)

    # Return the output
    return output