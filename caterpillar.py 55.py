import random
import turtle as t
t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.penup()

leaf = t.Turtle()
leaf_shape = ((0,0), (14,2), (18,6), (20,20),\
(6,18), (2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.speed(0)

def outside_window():
    pass
def game_over():
    pass
def display_score(current_score):
    pass
def place_leaf():
    pass

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    display.score(score)
place_leaf()

while True:
    if caterpillar.distance(leaf) < 20:
        place_leaf()
    if outside_window():
        game_over()
        break
t.onkey(start_game, 'space')
t.listen()
t.mainloop()

def outside_window():
    left_wall = t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = t.window_height()/2
    (x,y) = caterpillar.pos()
    out = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.write('GAME OVER!',align='center', font=('Aerial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-50
    score_turtle.setpos(x,y)

def place_leaf():
    leaf.setx(rd.rantint(-200,200))
    leaf.sety(rd.rantint(-200,200))

    
t.onkey(start_game,'space')
t.onkey(move_up,'up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()

    
