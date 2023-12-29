import base64
import pyperclip

def encrypt(text):
    text=text.encode()
    text=base64.b64encode(text)
    return text

def decrypt(text):
    text=text.decode()
    text=base64.b64decode(text)
    return text


print(encrypt("asd"))
