import pyperclip
from tkinter import *

# Create a new window with n buttons, each of which copies a different string to the clipboard
def split_n(myFile, n):
    myStr = open(myFile, "r").read()
    # Split myStr into n parts
    chunks = [myStr[i:i+len(myStr)//n] for i in range(0, len(myStr), len(myStr)//n)]
    
    window = Tk()
    for i in range(n):
        button = Button(window, text=f"Copy {i+1}", command=lambda x=chunks[i]: pyperclip.copy(x))
        button.grid(row=i, column=0)
    window.mainloop()

split_n("babyagi.py",5)