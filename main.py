import algo1
import algo2

from tkinter import *
from tkinter import messagebox

class Encrypt:
    def __init__(self,text=""):
        self.text = text
        self.key = bytes()
        self.root=Tk()
        self.val=()

    def encrypt(self,type) -> None:
        self.text=self.text_box.get("1.0",END)
        if type == 1:
            self.val=algo1.encrypt(self.text)
            self.key=self.val[1]
            messagebox.showwarning("Encrypted Text","Encrypted Text is saved in key.txt")
            messagebox.showinfo("Key","Key is saved in key.txt")
            print(self.val)
        elif type == 2:
            self.val=algo2.encrypt(self.text)
            messagebox.showinfo("Encrypted Text",self.val[:-1])
            print(self.val[:-1])
        else:
            messagebox.ERROR("Invalid type","Invalid type")

    def main(self) -> None:
        self.root.title("Encrypter")
        self.root.geometry("500x500")
        self.root.resizable(False,False)
        self.root.configure(bg="black")
        # self.root.iconbitmap("icon.ico")
        
        self.frame=Frame(self.root,width=300,height=300,bg="black")
        self.frame.configure(bg="black",cursor="arrow")
        self.frame.grid()

        self.title=Label(self.frame,text="Encrypter / Decrypter",font="Arial 20 bold",bg="black",foreground="white")
        self.title.grid(row=0,columnspan=2,padx=10,pady=10)

        self.input=Label(self.frame,text="Text To Encrypt",font="Arial 15",bg="black",foreground="white")
        self.input.grid(row=1,column=0,padx=10,pady=10)


        # text box
        self.text_box=Text(self.frame,width=25,height=1,foreground="white",bg="black",font="Arial 15",cursor="arrow",insertbackground="white")
        self.text_box.grid(row=1,column=1,padx=10,pady=10)

        # encrypt button
        self.encrypt_button1=Button(self.frame,text="Random Key Gen",command=lambda:self.encrypt(1),bg="black",foreground="Yellow")
        self.encrypt_button1.grid(row=2,column=0,padx=10,pady=10)

        self.encrypt_button2=Button(self.frame,text="Ceasar Cipher",command=lambda:self.encrypt(2),bg="black",foreground="Yellow")
        self.encrypt_button2.grid(row=2,column=1,padx=10,pady=10)

        # decrypt button
        self.decrypt_button=Button(self.frame,text="Key Decrypt",command=lambda:self.decrypt(1),bg="black",foreground="Yellow")
        self.decrypt_button.grid(row=4,column=0,padx=10,pady=10)

        self.decrypt_button=Button(self.frame,text="Ceasar Decrypt",command=lambda:self.decrypt(2),bg="black",foreground="Yellow")
        self.decrypt_button.grid(row=4,column=1,padx=10,pady=10)

        # exit button
        self.exit_button=Button(self.frame,text="Exit",command=self.root.destroy,bg="black",foreground="Yellow")
        self.exit_button.grid(row=5,columnspan=3,padx=10,pady=10)

        self.root.mainloop()

if __name__ == "__main__":
    ob=Encrypt()
    ob.main()