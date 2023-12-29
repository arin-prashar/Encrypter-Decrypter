from cryptography.fernet import Fernet
from typing import Tuple
from functools import lru_cache


@lru_cache(maxsize=1000)
def encrypt(text)-> Tuple[str,str]:
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(text.encode())
    # bytes to str
    with open("key.txt","wb") as file:
        file.write(encrypted)
        # newline
        file.write(b"\n")
        file.write(key)

    return (encrypted,key)

@lru_cache(maxsize=1000)
def decrypt(text,key)->str:
    f = Fernet(key)
    decrypted = f.decrypt(text.encode())
    print(decrypted)
    return decrypted