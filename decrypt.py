import algo1
import algo2
import algo3

def decrypt(text,option,key):
    if option == 1:
        return algo1.decrypt(text,key)
    elif option == 2:
        return algo2.decrypt(text,key)
    elif option == 3:
        return algo3.decrypt(text,key)
    else:
        return "Invalid option"
