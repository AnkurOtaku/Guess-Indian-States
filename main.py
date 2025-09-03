import time
import turtle

screen = turtle.Screen()
screen.title('Name Indian States')
image = 'India-Outline-Map.gif'
screen.addshape(image)
turtle.shape(image)

states = [
    ["Andhra Pradesh",-102, -223],
    ["Arunachal Pradesh",343, 238],
    ["Assam",295, 164],
    ["Bihar",99, 134],
    ["Chhattisgarh",-15, -2],
    ["Goa",-260, -198],
    ["Gujarat",-316, 53],
    ["Haryana",-174, 240],
    ["Himachal Pradesh",-151 ,329],
    ["Jharkhand",77, 67],
    ["Karnataka",-201, -231],
    ["Kerala",-190, -353],
    ["Madhya Pradesh",-126, 53],
    ["Maharashtra",-213, -71],
    ["Manipur",331, 121],
    ["Meghalaya",256, 135],
    ["Mizoram",306, 77],
    ["Nagaland",347, 163],
    ["Odisha",52, -38],
    ["Punjab",-200 ,295],
    ["Rajasthan",-244, 164],
    ["Sikkim",169, 197],
    ["Tamil Nadu",-119, -338],
    ["Telangana",-105, -119],
    ["Tripura",263, 80],
    ["Uttar Pradesh",-55, 171],
    ["Uttarakhand",-98, 275],
    ["West Bengal",152, 54],
]

is_game_on = True

def guess_state():
    global is_game_on
    state_found = False

    answer_state = screen.textinput(title=f'{28-len(states)} States Correct', prompt="What's another state name?").lower()
    print(answer_state)
    for state in states:
        if state[0].lower() == answer_state:
            state_name = turtle.Turtle()
            state_name.penup()
            state_name.goto(state[1], state[2])
            state_name.hideturtle()
            state_name.write(state[0],True, 'center', ('Arial', 8, 'normal'))
            states.remove(state)
            print(len(states))
            state_found = True

        elif answer_state == 'give up':
            is_game_on = False
            state_found = True
            give_up()

    if not state_found:
        err = turtle.Turtle()
        err.hideturtle()
        err.penup()
        err.home()
        err.write('Enter correct spelling of the state', True, 'center', ('Arial', 10, 'normal'))
        time.sleep(3)
        err.clear()
        err.reset()

    if len(states) <= 0:
        is_game_on = False
        celebrate()

def celebrate():
    print('You won')

def give_up():
    for state in states:
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.color('red')
        time.sleep(0.5)
        state_name.goto(state[1],state[2])
        state_name.write(state[0], True, 'center', ('Arial', 12, 'normal'))

while is_game_on:
    guess_state()

screen.exitonclick()