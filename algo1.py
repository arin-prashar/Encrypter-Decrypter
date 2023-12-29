from cryptography.fernet import Fernet
from typing import Tuple
from functools import lru_cache
import json


@lru_cache(maxsize=1000)
def encrypt(text)-> Tuple[str,str]:
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(text.encode())
    # bytes to str
    # write key to json file
    with open('key.json','w') as f:
        json.dump(key.decode(),f)

    return (encrypted,key)

@lru_cache(maxsize=1000)
def decrypt(text,key)->str:
    f = Fernet(key)
    decrypted = f.decrypt(text.encode())
    return decrypted

encrypt("hello")