from tkinter import *
import random
import pandas
french = ""
data = pandas.read_csv("french_words.csv")
word_dict = {row[0]: row[1] for (index, row) in data.iterrows()}
BACKGROUND_COLOR = "#B1DDC6"


def flip_card(french):
    canvas.itemconfig(card_background, image=back)
    canvas.itemconfig(canvas_title, text="English")
    canvas.itemconfig(canvas_word, text=word_dict[french])


def card_fun():
    global french
    canvas.itemconfig(card_background, image=front)
    canvas.itemconfig(canvas_title, text="French")
    french = random.choice(list(word_dict.keys()))
    canvas.itemconfig(canvas_word, text=french)
    flash_card.after(3000, flip_card, french)


def is_known():
    word_dict.pop(french)
    card_fun()


flash_card = Tk()
flash_card.title("Flash Card")
flash_card.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
front = PhotoImage(file="card_front.png")
back = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=front)
canvas.config(highlightthickness=0)
canvas_title = canvas.create_text(375, 150, text="", fill="black",font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(375, 300, text="Word", fill="black",font=("Arial", 60, "bold"))
canvas.grid(row=0, column=1, columnspan=2)

wr_image = PhotoImage(file="wrong.png")
wrong = Button(image=wr_image, width=100, command=card_fun)
wrong.grid(row=1, column=1)
r_image = PhotoImage(file="right.png")
right = Button(image=r_image, width=100, command=is_known)
right.grid(row=1, column=2)
card_fun()

flash_card.mainloop()
