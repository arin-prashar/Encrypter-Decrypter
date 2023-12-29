import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import sys
import encrypt
import decrypt
import pyperclip
from pyperclip import copy

# Global variables
# The main window
main_window = None
# The main frame
main_frame = None
# The main title
main_title = None

# The input Text frame , lable and entry
input_text_frame = None
input_text_label = None
input_text_entry = None

# The output Text frame , lable and entry
output_text_frame = None
output_text_label = None
output_text_entry = None

# dropdown to choose of 3 options to encrypt/decrypt
dropdown_frame = None
dropdown_label = None
dropdown = None

# decrypt key
key_frame = None
key_label = None
key_entry = None

# The button frame and buttons for encrypt/decrypt
button_frame = None
encrypt_button = None
decrypt_button = None
copy_button = None

# The status bar
status_bar = None

# The main function
def main():
    global main_window
    global main_frame
    global main_title
    global input_text_frame
    global input_text_label
    global input_text_entry
    global output_text_frame
    global output_text_label
    global output_text_entry
    global dropdown_frame
    global dropdown_label
    global dropdown
    global button_frame
    global encrypt_button
    global decrypt_button
    global copy_button
    global status_bar
    global key_frame
    global key_label
    global key_entry

    # Create the main window
    main_window = tk.Tk()
    main_window.title("Encrypt/Decrypt")
    main_window.geometry("500x800")
    main_window.resizable(False, False)

    # Create the main frame
    main_frame = ttk.Frame(main_window, width=500, height=500)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Create the main title
    main_title = ttk.Label(main_frame, text="Encrypt/Decrypt")
    main_title.config(font=("Courier", 44))
    main_title.pack(pady=20)

    # Create the input text frame
    input_text_frame = ttk.Frame(main_frame, width=500, height=100)
    input_text_frame.pack(fill=tk.BOTH, expand=True)

    # Create the input text label
    input_text_label = ttk.Label(input_text_frame, text="Input text:")
    input_text_label.config(font=("Courier", 20))
    input_text_label.pack(pady=10)

    # Create the input text entry
    input_text_entry = ttk.Entry(input_text_frame, width=50)
    input_text_entry.pack(pady=10)

    key_frame = ttk.Frame(main_frame, width=500, height=100)
    key_frame.pack(fill=tk.BOTH, expand=True)

    key_label = ttk.Label(key_frame, text="Enter the key:")
    key_label.config(font=("Courier", 20))
    key_label.pack(pady=10)

    key_entry = ttk.Entry(key_frame, width=50)
    key_entry.pack(pady=10)
    # Create the output text frame
    output_text_frame = ttk.Frame(main_frame, width=500, height=100)
    output_text_frame.pack(fill=tk.BOTH, expand=True)

    # Create the output text label
    output_text_label = ttk.Label(output_text_frame, text="Output text:")
    output_text_label.config(font=("Courier", 20))
    output_text_label.pack(pady=10)

    # Create the output text entry
    output_text_entry = ttk.Entry(output_text_frame, width=50)
    output_text_entry.pack(pady=10)

    # Create the dropdown frame
    dropdown_frame = ttk.Frame(main_frame, width=500, height=100)
    dropdown_frame.pack(fill=tk.BOTH, expand=True)

    # Create the dropdown label
    dropdown_label = ttk.Label(dropdown_frame, text="Choose an option:")
    dropdown_label.config(font=("Courier", 20))
    dropdown_label.pack(pady=10)

    # Create the dropdown
    dropdown = ttk.Combobox(dropdown_frame, width=50)
    global values
    values = ['Random Key Gen', 'Ceasar Cipher', 'Vigenere Cipher']
    dropdown['values'] = values
    dropdown.current(0)
    dropdown.pack(pady=10)

    # Create the button frame
    button_frame = ttk.Frame(main_frame, width=500, height=100)
    button_frame.pack(fill=tk.BOTH, expand=True)

    # Create the encrypt button
    encrypt_button = ttk.Button(button_frame, text="Encrypt", command=lambda: encrypt_button_pressed())
    encrypt_button.pack(side=tk.LEFT, padx=10)

    # Create the decrypt button
    decrypt_button = ttk.Button(button_frame, text="Decrypt", command=lambda: decrypt_button_pressed())
    decrypt_button.pack(side=tk.LEFT, padx=10)

    # Create the copy button
    copy_button = ttk.Button(button_frame, text="Copy", command=lambda: copy_button_pressed())
    copy_button.pack(side=tk.LEFT, padx=10)

    # Create the status bar
    status_bar = ttk.Label(main_frame, text="Encrypt/Decrypt")
    status_bar.config(font=("Courier", 20))
    status_bar.pack(pady=20)

    # Start the main loop
    main_window.mainloop()

# The encrypt button pressed function
def encrypt_button_pressed():
    global input_text_entry
    global output_text_entry
    global dropdown
    global status_bar

    # Get the input text
    input_text = input_text_entry.get()

    # Get the dropdown value
    dropdown_value = dropdown.get()
    dropdown_value=values.index(dropdown_value)+1
    output_text = encrypt.encrypt(input_text,dropdown_value)

    # Set the output text
    output_text_entry.delete(0, tk.END)
    output_text_entry.insert(0, output_text)

    # Set the status bar
    status_bar.config(text="Encrypted")

# The decrypt button pressed function
def decrypt_button_pressed():
    global input_text_entry
    global output_text_entry
    global dropdown
    global status_bar
    global key_entry
    # Get the input text
    input_text = input_text_entry.get()

    # Get the dropdown value
    dropdown_value = dropdown.get()
    dropdown_value=values.index(dropdown_value)+1
    
    key=key_entry.get()

    # Decrypt the input text
    output_text = decrypt.decrypt(input_text,dropdown_value,key)

    # Set the output text
    output_text_entry.delete(0, tk.END)
    output_text_entry.insert(0, output_text)

    # Set the status bar
    status_bar.config(text="Decrypted")

# The copy button pressed function
def copy_button_pressed():
    global output_text_entry
    global status_bar

    # Get the output text
    output_text = output_text_entry.get()

    # Copy the output text
    copy(output_text)

    # Set the status bar
    status_bar.config(text="Copied")

# Call the main function
main()