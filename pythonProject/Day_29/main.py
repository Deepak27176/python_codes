import tkinter as tk

def add():

    with open("data.txt", mode="a") as file:
        file.write(f"{web_input.get()} | {mail_input.get()} |  {pass_input.get()} \n")
    web_input.delete(0, "end")
    pass_input.delete(0, "end")

app_window = tk.Tk()
app_window.config(padx=100, pady=100)
canvas = tk.Canvas(width=200, height=224)
Image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=Image)
canvas.grid(row=0, column=1)
web_label = tk.Label(text="Website", font=("Arial",15,"bold"))
web_label.grid(row=1, column=0)
mail_label = tk.Label(text="User/Email", font=("Arial",15,"bold"))
mail_label.grid(row=2, column=0)
pass_label = tk.Label(text="Password", font=("Arial",15,"bold"))
pass_label.grid(row=3, column=0)
web_input = tk.Entry(width=35)
web_input.grid(row=1, column=1)
mail_input = tk.Entry(width=35)
mail_input.insert(-1, "deepakyerramsetti@gmail.com")
mail_input.grid(row=2, column=1)
pass_input = tk.Entry(width=20)
pass_input.grid(row=3, column=1)
add_button = tk.Button(text="ADD",command=add)
add_button.grid(row=3, column=2)

app_window.mainloop()