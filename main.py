import turtle
from pynput import keyboard

# ==============================================SetUp & Variables=+=============================================

# Window Title
turtle.title("Euler Orb")

# Turtle Variable Assigning
tur = turtle.Turtle()
sc = turtle.Screen()

# Background & Speed Variables
sc.bgcolor(0, 0, 0)
sc.tracer(200, 25)

# Global Lists That Are Reused
style_orb = ('Times New Roman', 20, 'bold')
style_spiral = ('Times New Roman', 25, 'bold')
degree = ['2', '.', '7', '1', '8']


# ============================================Basic Drawing Functions============================================


# To End Program
def end():
    turtle.bye()


# To Reset Canvas
def reset():
    tur.reset()


# To set Background Color Black
def background_b():
    sc.bgcolor(0, 0, 0)


# To set Background Color White
def background_w():
    sc.bgcolor(1, 1, 1)


# ============================================Key Input Functions================================================


# To Take Inputs from User
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        degree.append(key.char)

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

    if key == keyboard.Key.enter:
        # Stop listener
        return False


# To execute on_press When We Need It
def take_input():
    degree.clear()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


# ================================================Orb Functions==================================================


# No.1
def euler_orb_ice():

    p_size = 1
    r = 1
    b = 1
    g = 1
    y = float(''.join(degree))

    for i in range(1350):
        tur.forward(i * 1.5)
        tur.right(360 / y)
        p_size += 0.03

        if r > 0:
            r -= 0.005
        if r < 0.05 and b > 0:
            b -= 0.005
        if b < 0.1 and g > 0:
            g -= 0.005

        tur.pensize(p_size)
        tur.pencolor(r, b, g)

    tur.goto(0, -250)
    tur.pencolor(1, 1, 1)
    tur.write("Euler Orb(Ice)", True, align="center", font=style_orb)


# No.2
def euler_orb_leaf():

    p_size = 1
    r = 1
    b = 1
    g = 1

    for i in range(1350):
        tur.forward(i * 1.5)
        tur.right(360 / 2.718)
        p_size += 0.03

        if r > 0:
            r -= 0.005
        if r < 0.05 and b > 0:
            b -= 0.005
        if b < 0.1 and g > 0:
            g -= 0.005

        tur.pensize(p_size)
        tur.pencolor(b, g, r)

    tur.pencolor(1, 1, 1)
    tur.goto(0, -250)
    tur.write("Euler Orb(Leaf)", True, align="center", font=style_orb)


# No.3
def euler_orb_fire():

    p_size = 1
    r = 1
    b = 1
    g = 1

    for i in range(1350):
        tur.forward(i * 1.5)
        tur.right(360 / 2.718)
        p_size += 0.03

        if r > 0:
            r -= 0.005
        if r < 0.05 and b > 0:
            b -= 0.005
        if b < 0.1 and g > 0:
            g -= 0.005

        tur.pensize(p_size)
        tur.pencolor(g, b, r)

    tur.goto(0, -250)
    tur.pencolor(1, 1, 1)
    tur.write("Euler Orb(Fire)", True, align="center", font=style_orb)


# No.4
def euler_orb_aurora():

    p_size = 1
    r = 1
    b = 1
    g = 1

    for i in range(1350):
        tur.forward(i * 1.5)
        tur.right(360 / 2.718)
        p_size += 0.03

        if r > 0:
            r -= 0.005
        if r < 0.05 and b > 0:
            b -= 0.005
        if b < 0.1 and g > 0:
            g -= 0.005

        tur.pensize(p_size)
        tur.pencolor(r, g, b)

    tur.goto(0, -250)
    tur.pencolor(1, 1, 1)
    tur.write("Euler Orb(Aurora)", True, align="center", font=style_orb)


# No.5
def euler_orb_heart():

    p_size = 1
    r = 1
    b = 1
    g = 1

    for i in range(1350):
        tur.forward(i * 1.5)
        tur.right(360 / 2.718)
        p_size += 0.03

        if r > 0:
            r -= 0.005
        if r < 0.05 and b > 0:
            b -= 0.005
        if b < 0.1 and g > 0:
            g -= 0.005

        tur.pensize(p_size)
        tur.pencolor(g, r, b)

    tur.goto(0, -250)
    tur.pencolor(1, 1, 1)
    tur.write("Euler Orb(Heart)", True, align="center", font=style_orb)


# No.6
def euler_orb_nightmare():

    p_size = 1
    r = 1
    b = 1
    g = 1

    for i in range(1350):
        tur.forward(i * 1.5)
        tur.right(360 / 2.718)
        p_size += 0.03

        if r > 0:
            r -= 0.005
        if r < 0.05 and b > 0:
            b -= 0.005
        if b < 0.1 and g > 0:
            g -= 0.005

        tur.pensize(p_size)
        tur.pencolor(b, r, g)

    tur.goto(0, -250)
    tur.pencolor(1, 1, 1)
    tur.write("Euler Orb(Nightmare)", True, align="center", font=style_orb)


# ===============================================Spiral Functions================================================


# No. 1
def euler_spiral_galaxy():

    p_size = 2.5
    y = float(''.join(degree))

    for i in range(2300):
        tur.forward(i * 1.5)
        tur.right(360 / y)
        tur.pensize(p_size)
        tur.pencolor(0, 0, 0)

    tur.goto(0, -350)
    tur.pencolor(1, 1, 1)
    tur.write("E u l e r  S p i r a l ( G a l a x y )", True, align="center", font=style_spiral)


# No.2
def euler_spiral_web():

    p_size = 1.5
    y = float(''.join(degree))

    for i in range(1400):
        tur.forward(i * 3)
        tur.right(360 / y)
        tur.pensize(p_size)
        tur.pencolor(1, 1, 1)

    tur.pencolor(0, 0, 0)
    tur.goto(0, -350)
    tur.write("E u l e r  S p i r a l ( W e b )", True, align="center", font=style_spiral)


# No.3
def euler_spiral_illusion():

    p_size = 1.5
    y = float(''.join(degree))

    for i in range(2300):
        tur.forward(i * 1.5)
        tur.right(360 / y)
        tur.pensize(p_size)
        tur.pencolor(0, 0, 0)

    tur.goto(0, -350)
    tur.pencolor(1, 1, 1)
    tur.write("E u l e r  S p i r a l ( I l l u s i o n )", True, align="center", font=style_spiral)


# ===============================================User Input Clause===============================================

sc.onkey(euler_orb_ice, 'i')
sc.onkey(euler_orb_leaf, 'l')
sc.onkey(euler_orb_fire, 'f')
sc.onkey(euler_orb_heart, 'h')
sc.onkey(euler_orb_aurora, 'a')
sc.onkey(euler_orb_nightmare, 'n')
sc.onkey(euler_spiral_web, 'Down')
sc.onkey(euler_spiral_galaxy, 'Up')
sc.onkey(euler_spiral_illusion, 'Left')
sc.onkey(background_w, 'w')
sc.onkey(background_b, 'b')
sc.onkey(reset, 'z')
sc.onkey(end, 'e')
sc.onkey(take_input, 'v')
sc.listen()

# ================================================Program Finish================================================

turtle.done()
