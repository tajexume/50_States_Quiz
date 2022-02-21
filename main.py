import turtle
import pandas
def creategame():
  screen = turtle.Screen()
  screen.title("50 States Guessing Game")
  image = "blank_states_img.gif"
  screen.addshape(image)
  turtle.shape(image)
  states_table = pandas.read_csv("50_states.csv")
  usa = states_table.state.to_list()
  for x in range(len(usa)):
    usa[x] = usa[x].upper()
  states_X = states_table.x.to_list()
  states_Y = states_table.y.to_list()
  correct = 0
  x = []
  y = []
  answered = []
  while correct != 50:
    answer_state = screen.textinput(title=f" {correct}/50", prompt="Enter a state")
    answer_state = answer_state.upper()
    if answer_state in usa:
      tim = turtle.Turtle()
      tim.ht()
      tim.penup()
      index = usa.index(answer_state)
      tim.goto(states_X[index], states_Y[index])
      tim.write(f"{answer_state}")
      correct += 1
      answered.append(answer_state)
      x.append(states_X[index])
      y.append(states_Y[index])
      states_X.pop(index)
      states_Y.pop(index)
      usa.pop(index)
    while correct == 1:
      reset = screen.textinput(title="You Won!", prompt="Play Again? Yes or No")
      if reset.upper() == "YES":
        screen.clearscreen()
        creategame()
      elif reset.upper() == "NO":
        screen.bye()
  screen.mainloop()
creategame()


