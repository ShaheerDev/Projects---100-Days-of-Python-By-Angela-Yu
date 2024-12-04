import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game ")
image = "blank_states_img.gif"
screen.addshape(image)


data = pandas.read_csv("50_states.csv")
states = data['state']
x_cor = data['x']
y_cor = data['y']

def get_coordinates(state_name):
    state_data = data[data['state'] == state_name]

    return int(state_data.x), int(state_data.y)
is_game_on = True
while is_game_on:
    turtle.shape(image)
    answer_state = turtle.textinput(title="Guess The state", prompt="Guess Another State.")
    if answer_state in states.values:
        writer_turtle = turtle.Turtle()
        writer_turtle.hideturtle()
        x, y = get_coordinates(answer_state)
        writer_turtle.penup()
        writer_turtle.goto(x, y)
        writer_turtle.write(answer_state)
    elif answer_state == None:
        is_game_on = False
turtle.mainloop()
