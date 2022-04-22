from tkinter import *
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=250, height=100)
window.config(padx=15, pady=15)

# Entry
entry = Entry(width=15)
entry.focus()
print(entry.get())
entry.grid(column=1, row=0)

#Label
label = Label(text="Miles")
label.grid(column=2, row=0)

label = Label(text="is equal to")
label.grid(column=0, row=1)

# label = Label(text=result)
# label.grid(column=1, row=1)

label = Label(text="km")
label.grid(column=2, row=1)


def action():
    result = 1.6 * float(entry.get())
    result = round(result, 1)
    label = Label(text=result)
    label.grid(column=1, row=1)


button = Button(text="Convert", command=action)
button.grid(column=1, row=2)


window.mainloop()