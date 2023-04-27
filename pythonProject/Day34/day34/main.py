import requests

from tkinter import *
import html

parameters = {
    "amount": 10,
    "type": "boolean"
}


class Check:
    def __init__(self):
        self.response = requests.get(
            url="https://opentdb.com/api.php", params= parameters)
        self.response.raise_for_status()
        self.questions = self.response.json()["results"]
        self.correct = 0
        self.answered = 0

    def check_ans(self):
        if self.answered >= len(self.questions):
            canvas.itemconfig(question_on_canvas, text=f"Quiz Ended\nFinal score: {self.correct}\{self.answered}")
        else:
            question = self.questions[self.answered]["question"]
            question = html.unescape(question)
            canvas.itemconfig(question_on_canvas, text=f"{question}")

    def is_right(self):
        if self.answered < len(self.questions):
            if self.questions[self.answered]["correct_answer"] == "True":
                self.correct += 1
                score.config(text=f"{self.correct}/{self.answered+1}")
            else:
                score.config(text=f"{self.correct}/{self.answered + 1}")
            self.answered += 1
        self.check_ans()

    def is_wrong(self):
        if self.answered < len(self.questions):
            if self.questions[self.answered]["correct_answer"] == "False":
                self.correct += 1
                score.config(text=f"{self.correct}/{self.answered+1}")
            else:
                score.config(text=f"{self.correct}/{self.answered + 1}")
            self.answered += 1
            self.check_ans()

quiz = Check()
window = Tk()
window.title("Trivia Quiz")
# window.minsize(width=500, height=300)
window.config(padx=5, pady=5)
score_label = Label(text="score", font=("Arial", 24, "bold"))
score_label.grid(row=0, column=0)
score = Label(text=f": {0}/{0}", font=("Arial", 20, "italic"))
score.grid(row=0, column=1)
# canvas = Canvas(width=490, height=140)
canvas = Canvas()
image = PhotoImage(file="card_back.png")
canvas.create_image(0, 0, image=image)
question_on_canvas = canvas.create_text(200, 50, width=280, text="Question????", font=("Arial", 12, "bold"))
canvas.grid(row=1, column=0, columnspan=2)
right = PhotoImage(file="true.png")
right_button = Button(image=right, width=100, command=quiz.is_right)
right_button.grid(row=2, column=0)
wrong = PhotoImage(file="false.png")
wrong_button = Button(image=wrong, width=100, command=quiz.is_wrong)
wrong_button.grid(row=2, column=1)
quiz.check_ans()
window.mainloop()
