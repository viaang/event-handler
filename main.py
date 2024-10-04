from tkinter import *

window = Tk()

window.title("HEY")
window.geometry("500x500")

button = Button(text = "button")
button.pack()
 


def key_Bind (event) :

    print( 'I have been clicked')
    



button.bind("<Button-1>", key_Bind)
window.mainloop()