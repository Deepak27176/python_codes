import turtle
import pandas
ALIGNMENT = "center"
FONT = ("Arial", 9, "normal")

my_screen = turtle.Screen()
my_screen.title("U.S STATES")
my_screen.addshape("blank_states_img.gif")
image = "blank_states_img.gif"
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
score = 0
print(state_list)
flag = 50

guessed_States = []
while len(guessed_States)<50:
    answer_state = my_screen.textinput(f"{len(guessed_States)}/50 states guessed",
                                       "Enter the state").title()
    if answer_state == "Exit":
        states_to_learn = []
        print(guessed_States)
        for i in state_list:
            if i not in guessed_States:
                states_to_learn.append(i)
        new_data = pandas.DataFrame(states_to_learn)
        print(new_data)
        new_data.to_csv("learn.csv")
        break

    if answer_state in state_list:
        guessed_States.append(answer_state)
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.color("black")
        timmy.hideturtle()
        state_data = data[data["state"] == answer_state]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(f"{answer_state}", align=ALIGNMENT, font=FONT)

