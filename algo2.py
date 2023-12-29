# ceaser cypher
from typing import Tuple
from functools import lru_cache
# lru cache
@lru_cache(maxsize=1000)
def encrypt(text)-> Tuple: 
    encrypted = ""
    for i in text:
        if i == " ":
            encrypted += " "
        elif i.isupper():
            encrypted += chr((ord(i) + 3 - 65) % 26 + 65)
        else:
            encrypted += chr((ord(i) + 3 - 97) % 26 + 97)
    return (encrypted)

@lru_cache(maxsize=1000)
def decrypt(text)->Tuple:
    decrypted = ""
    for i in text:
        if i == " ":
            decrypted += " "
        elif i.isupper():
            decrypted += chr((ord(i) - 3 - 65) % 26 + 65)
        else:
            decrypted += chr((ord(i) - 3 - 97) % 26 + 97)
    return decrypted
