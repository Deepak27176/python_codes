import tkinter as tk

def click():
    km = float(input1.get())*1.60934
    km = round(km, 2)
    ans.config(text=f"{km}")
window = tk.Tk()
window.config(padx=100, pady=100)
window.title("MIles To KM")
my_label = tk.Label(text="Is equal to")
my_label.config(font=("Arial", 15, "bold"))
my_label.grid(row=2, column=0)
Miles = tk.Label(text="Miles")
Miles.config(font=("Arial", 10, "bold"))
Miles.grid(row=1, column=2)
Km = tk.Label(text="km")
Km.config(font=("Arial", 10, "bold"))
Km.grid(row=2, column=2)
ans = tk.Label(text="0")
ans.config(font=("Arial", 10, "italic"))
ans.grid(row=2, column=1)
my_botton = tk.Button(text="Calculate", command=click)
my_botton.grid(row=3, column=2)
input1 = tk.Entry()
input1.grid(row=1, column=1)

window.mainloop()