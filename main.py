from tkinter import Tk
from tkinter import Button, Entry, LabelFrame

root = Tk()
root.title("Python Timer App")
root.geometry("500x500")

labelframe = LabelFrame(text="Set Me", padx=185, pady=185)
labelframe.pack()

hour = Entry(labelframe, text="Timer", width=2)
hour.grid(row=0, column=0, padx=20, pady=20)

mins = Entry(labelframe, text="Timer", width=2)
mins.grid(row=0, column=1, padx=20, pady=20)

seconds = Entry(labelframe, text="Timer", width=2)
seconds.grid(row=0, column=2, padx=20, pady=20)

button = Button(labelframe, text="Start")
button.grid(row=1, columnspan=3)
root.mainloop()