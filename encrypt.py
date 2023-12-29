import algo1
import algo2
import algo3

def encrypt(text,option):
    print(option)
    if option == 1:
        return algo1.encrypt(text)
    elif option == 2:
        return algo2.encrypt(text)
    elif option == 3:
        return algo3.encrypt(text)
    else:
        return "Invalid option"