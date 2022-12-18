import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
usImage = "workingCSV/us-states-game-start/blank_states_img.gif"
screen.addshape(usImage)
turtle.shape(usImage)
data = pandas.read_csv("workingCSV/us-states-game-start/50_states.csv")
state_list = data.state.to_list()
guessed_states = []
while len(guessed_states) <= 50:
    new_title = str(len(guessed_states)) + "/50 states guessed correctly"
    answer_state = screen.textinput(
        prompt="Guess the State", title=new_title).title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_dict = {
            "Missing States": missing_states
        }
        df = pandas.DataFrame(missing_states_dict)
        df.to_csv("workingCSV/us-states-game-start/states_not_guessed.csv")
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
