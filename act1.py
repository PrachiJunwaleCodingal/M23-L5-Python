# lets top a window
from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Top window")
def topWindow():
	top = Toplevel()
	top.geometry("200x200")
	top.title("toplevel")
	label2 = Label(top, text = "Toplevel window")
	label2.pack()
	top.mainloop()

label1 = Label(root, text = "Root window")
btn = Button(root, text = "open another window", command = topWindow)
label1.pack()
btn.pack()
root.mainloop()