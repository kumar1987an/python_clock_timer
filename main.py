from tkinter import Tk
from tkinter import Button, Entry, LabelFrame, Label, font


root = Tk()
root.title("Python Timer App")
general_font = font.Font(weight="bold", size="10", family="Calibri")
labelframe_font = font.Font(size="12", family="Calibri")
root.geometry("350x200")

labelframe = LabelFrame(text="Set Me", padx=10, pady=10)
labelframe["font"] = labelframe_font
labelframe.configure(bg="ivory3")
labelframe.pack()

hour = Entry(labelframe, width=2, borderwidth=3)
hour.grid(row=0, column=0, padx=20, pady=20, ipadx=20, ipady=20)

colon_1 = Label(labelframe, text=":")
colon_1.grid(row=0, column=1)

mins = Entry(labelframe, width=2, borderwidth=3)
mins.grid(row=0, column=2, padx=20, pady=20, ipadx=20, ipady=20)

colon_2 = Label(labelframe, text=":")
colon_2.grid(row=0, column=1)

seconds = Entry(labelframe, width=2, borderwidth=3)
seconds.grid(row=0, column=3, padx=20, pady=20, ipadx=20, ipady=20)

button = Button(labelframe, text="Start", bg="green", fg="white")
button["font"] = general_font
button.grid(row=1, columnspan=4)
root.mainloop()