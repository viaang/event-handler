from tkinter import *
from tkinter import messagebox
window = Tk()

window.geometry("800x800")
window.title("Tk")

def alert() :
   messagebox.showerror('Virus', 'Alert I have installed a virus') 


button = Button(text = 'click me', height='2', width='4', command=alert)
button.pack()

def cancel() :
   box = messagebox.askquestion('cancel', 'do you want to cancel the virus ?')
   if box == 'yes' :
      messagebox.showinfo('succsess ', 'It has been sucessful')
      


button1 = Button(text = "cancel", height = '2', width = '5', command = cancel)
button1.place(x = 400, y = 400)





window.mainloop()