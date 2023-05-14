import tkinter

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    result.config(text=f"{km}")

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

#Label
result = tkinter.Label(text="0", font=("Arial", 24, "normal"))
result.grid(column=1, row=1)
is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 24, "normal"))
is_equal_label.grid(column=0, row=1)
miles_label = tkinter.Label(text="Km", font=("Arial", 24, "normal"))
miles_label.grid(column=2, row=1)
km_label = tkinter.Label(text="Miles", font=("Arial", 24, "normal"))
km_label.grid(column=2, row=0)

#Button
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


#Entry
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)
print(miles_input.get())

window.mainloop()