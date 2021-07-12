from tkinter import Tk
from tkinter import Button, Entry, LabelFrame, Label, font


root = Tk()
root.title("Python Timer App")
general_font = font.Font(weight="bold", size="10", family="Calibri")
labelframe_font = font.Font(size="12", family="Calibri")
colon_font = font.Font(weight="bold", size="16")
root.geometry("380x200")

labelframe = LabelFrame(text="Set Me", padx=10, pady=10)
labelframe["font"] = labelframe_font
labelframe.configure(bg="ivory3")
labelframe.pack()

hours = Entry(labelframe, width=2, borderwidth=3)
hours.grid(row=0, column=0, padx=20, pady=20, ipadx=20, ipady=20)

colon_1 = Label(labelframe, text=":")
colon_1.grid(row=0, column=1)
colon_1["font"] = colon_font
colon_1.configure(bg="ivory3")

mins = Entry(labelframe, width=2, borderwidth=3)
mins.grid(row=0, column=2, padx=20, pady=20, ipadx=20, ipady=20)

colon_2 = Label(labelframe, text=":")
colon_2.grid(row=0, column=3)
colon_2["font"] = colon_font
colon_2.configure(bg="ivory3")

seconds = Entry(labelframe, width=2, borderwidth=3)
seconds.grid(row=0, column=4, padx=20, pady=20, ipadx=20, ipady=20)

button = Button(labelframe, text="Start", bg="green", fg="white")
button["font"] = general_font
button.grid(row=1, columnspan=6)
root.mainloop()