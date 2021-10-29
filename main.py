import turtle
from pynput import keyboard

# ==============================================SetUp & Variables=+=============================================

# Window Title
turtle.title("Euler Orb")

# Turtle Variable Assignment
tur = turtle.Turtle()
sc = turtle.Screen()

# Background & Speed Variables
sc.bgcolor(0, 0, 0)
sc.tracer(250, 1)
tur.hideturtle()

# Global Lists
colors = ['i']  # => Default color
degrees = ['2.718']  # => Default Degree
orb_titles = {'f': 'Fire', 'a': 'Aurora', 'h': 'Heart',
              'n': 'Nightmare', 'i': 'Ice', 'l': 'Leaf'
              }
orb_writing_style = ('Times New Roman', 20, 'bold')
spiral_writing_style = ('Times New Roman', 40, 'bold')

# ===============================================Basic Functions=================================================


# Swap r, g, b Slots to Execute Different Euler Orb Gradients
def rgb_swap(color, r, g, b):
  
    # i, a, h, f, n, l Corresponds To Ice, Aurora, Heart,...etc Gradients 
    if color == "i":
        r, g, b = r, g, b
        return r, g, b

    if color == "a":
        r, g, b = r, b, g
        return r, g, b

    if color == "h":
        r, g, b = b, r, g
        return r, g, b

    if color == "f":
        r, g, b = b, g, r
        return r, g, b

    if color == "n":
        r, g, b = g, r, b
        return r, g, b

    if color == "l":
        r, g, b = g, b, r
        return r, g, b


# Position Turtle() At Desired Location
def position(color, x, y):
    tur.pencolor(color)
    tur.penup()
    tur.goto(x, y)

    
# =======================================Basic Drawing Functions For User=======================================


# End Program
def end():
    turtle.bye()


# Reset Canvas
def reset_canvas():
    tur.reset()


# Position Turtle() at the center
def go_home():
    tur.penup()
    tur.goto(0, 0)
    tur.pendown()


# Set Background Color Black
def background_b():
    sc.bgcolor(0, 0, 0)


# Set Background Color White
def background_w():
    sc.bgcolor(1, 1, 1)


# ================================================Orb Functions==================================================


def euler_orb():
    
    r = 1
    b = 1
    g = 1
    p_size = 1
    orb_size_cnst = 1.5
    degree = float(''.join(degrees))
    color = ''.join(colors)

    for i in range(1350):
        tur.forward(i * orb_size_cnst)
        tur.right(360 / degree)
        p_size += 0.03
        # Color Gradient Clause
        if r > 0.005:
            r -= 0.005
        if r < 0.005 < g:
            g -= 0.005
        if g < 0.005 < b:
            b -= 0.005
        tur.pensize(p_size)
        tur.pencolor(rgb_swap(color, r, g, b))

    position((1, 1, 1), 0, -250)
    tur.write("Euler Orb({0})".format(orb_titles[color]), True, align="center", font=orb_writing_style)


# ===============================================Spiral Functions================================================


# Spiral No. 1
def euler_spiral_galaxy():
  
    p_size = 2.5
    orb_size_cnst = 1.5
    degree = float(''.join(degrees))

    for i in range(2300):
        tur.forward(i * orb_size_cnst)
        tur.right(360 / degree)
        tur.pensize(p_size)
        tur.pencolor(0, 0, 0)

    position((1, 1, 1), 0, -350)
    tur.write(" ".join("Euler Spiral (Galaxy)"), True, align="center", font=spiral_writing_style)


# Spiral No.2
def euler_spiral_illusion():
  
    p_size = 1.5
    orb_size_cnst = 1.5
    degree = float(''.join(degrees))

    for i in range(2300):
        tur.forward(i * orb_size_cnst)
        tur.right(360 / degree)
        tur.pensize(p_size)
        tur.pencolor(0, 0, 0)

    position((1, 1, 1), 0, -350)
    tur.write(" ".join("Euler Spiral (Illusion)"), True, align="center", font=spiral_writing_style)


# Spiral No.3
def euler_spiral_web():
  
    p_size = 1.5
    orb_size_cnst = 3
    degree = float(''.join(degrees))

    for i in range(1400):
        tur.forward(i * orb_size_cnst)
        tur.right(360 / degree)
        tur.pensize(p_size)
        tur.pencolor(1, 1, 1)

    position((0, 0, 0), 0, -350)
    tur.write(" ".join("Euler Spiral (Web)"), True, align="center", font=spiral_writing_style)


# ============================================Key Input Functions================================================


# Take Degree Inputs From User
def degree_input(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        degrees.append(key.char)

    except AttributeError:
        print('special key {0} pressed'.format(key))

    if key == keyboard.Key.enter:
        # Stop listener
        return False

    
# Take Color Inputs From User
def color_input(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        colors.append(key.char)

    except AttributeError:
        print('special key {0} pressed'.format(key))

    if key == keyboard.Key.enter:
        # Stop listener
        return False
    

# Execute Function degree_input() When We Need It
def take_degrees_input():
    degrees.clear()
    with keyboard.Listener(on_press=degree_input) as listener:
        listener.join()


# Execute Function color_input() When We Need It
def take_color_input():
    colors.clear()
    with keyboard.Listener(on_press=color_input) as listener:
        listener.join()
    
    
# ===============================================User Input Clause===============================================

# Basic Drawing Functions
sc.onkey(end, 'x')
sc.onkey(go_home, 'y')
sc.onkey(reset_canvas, 'z')
sc.onkey(background_b, 'b')
sc.onkey(background_w, 'w')

# User Input Activation Keys
sc.onkey(take_color_input, 'c')
sc.onkey(take_degrees_input, 'd')

# Execution Keys
sc.onkey(euler_orb, 'o')
sc.onkey(euler_spiral_galaxy, 'Up')
sc.onkey(euler_spiral_illusion, 'Down')
sc.onkey(euler_spiral_web, 'Left')

sc.listen()

# ================================================Program Finish================================================

turtle.done()
