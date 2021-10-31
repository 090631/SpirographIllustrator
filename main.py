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
orb_writing_style = (
    'Times New Roman', 20, 'bold'
)
spiral_writing_style = (
    'Times New Roman', 40, 'bold'
)
orb_titles = { 
    'i': 'Ice',
    'a': 'Aurora', 
    'h': 'Heart',
    'n': 'Nightmare', 
    'f': 'Fire',
    'l': 'Leaf'
}

# ===============================================Basic Functions=================================================
# Write Orb & Sprial Titles
def write(name: str, style: tuple) -> None:
    tur.write(
        name, True, align="center", font=style
    )

# Position Turtle() at the desired location With Out Leaving A Trail
def position(color: tuple, x: int, y: int) -> None:
    tur.pencolor(color)
    tur.penup()
    tur.goto(x, y)

# Swap r, g, b slots to execute different Euler Orb variants
def rgb_swap(color: str, r: int, g: int, b: int) -> tuple:
    colorDict = {
        'i' : (r, g, b),
        'a' : (r, b, g),
        'h' : (b, r, g),
        'f' : (b, g, r),
        'n' : (g, r, b),
        'l' : (g, b, r)
    }
    r, g, b = colorDict[color]
    return r, g, b

# =======================================Basic Drawing Functions For User=======================================
# End Program
def end() -> None:
    turtle.bye()


# Reset Canvas
def reset_canvas() -> None:
    tur.reset()


# Position Turtle() at the center
def go_home() -> None:
    tur.penup()
    tur.goto(0, 0) 
    tur.pendown()


# Set Background Color Black
def background_b() -> None:
    sc.bgcolor(0, 0, 0)


# Set Background Color White
def background_w() -> None:
    sc.bgcolor(1, 1, 1)

# ================================================Orb Functions==================================================
def euler_orb() -> None:
    p_size = 1
    r = 1
    b = 1
    g = 1
    orb_size = 1.5
    degree = float(''.join(degrees))
    color = ''.join(colors)

    for i in range(1350):
        tur.forward(i * orb_size)
        tur.right(360 / degree)
        
        if p_size <= 25:
            p_size += 0.03
        if r > 0.005:
            r -= 0.005
        if r < 0.005 < g:
            g -= 0.005
        if g < 0.005 < b:
            b -= 0.005
        tur.pensize(p_size)
        tur.pencolor(rgb_swap(color, r, g, b))

    position((1, 1, 1), 0, -250)
    write(f"Euler Orb ({orb_titles[color]})", orb_writing_style)

# ===============================================Spiral Functions================================================
def euler_spiral_galaxy() -> None:
    p_size = 2.5
    spiral_size = 1.5
    degree = float(''.join(degrees))

    for i in range(2300):
        tur.forward(i * spiral_size)
        tur.right(360 / degree)
        tur.pensize(p_size)
        tur.pencolor(0, 0, 0)

    position((1, 1, 1), 0, -350)
    write(" ".join("Euler Spiral (Galaxy)"), spiral_writing_style
    )


def euler_spiral_illusion() -> None:
    p_size = 1.5
    spiral_size = 1.5
    degree = float(''.join(degrees))

    for i in range(2300):
        tur.forward(i * spiral_size)
        tur.right(360 / degree)
        tur.pensize(p_size)
        tur.pencolor(0, 0, 0)

    position((1, 1, 1), 0, -350)
    write(" ".join("Euler Spiral (Illusion))"), spiral_writing_style)


def euler_spiral_web() -> None:
    p_size = 1.5
    spiral_size = 3
    degree = float(''.join(degrees))

    for i in range(1400):
        tur.forward(i * spiral_size)
        tur.right(360 / degree)
        tur.pensize(p_size)
        tur.pencolor(1, 1, 1)

    position((.5, .5, .5), 0, -350)
    write(" ".join("Euler Spirals (Web)"), spiral_writing_style)


def euler_spiral_web():
    p_size = 1.5
    spiral_size = 3
    degree = float(''.join(degrees))

    for i in range(1400):
        tur.forward(i * spiral_size)
        tur.right(360 / degree)
        tur.pensize(p_size)
        tur.pencolor(1, 1, 1)

    position((0, 0, 0), 0, -350)
    write(" ".join("Euler Spiral (Web)"), spiral_writing_style)

# ============================================User Input Functions================================================
# Take Degree Inputs from User
def degree_input(key: str) -> None:
    try:
        print(f'alphanumeric key {key.char} pressed')
        degrees.append(key.char)

    except AttributeError:
        print(f'special key {key} pressed')

    if key == keyboard.Key.enter:
        # Stop listener
        return False


# Take Color Inputs from User
def color_input(key: str) -> None:
    try:
        print(f'alphanumeric key {key.char} pressed')
        colors.append(key.char)

    except AttributeError:
        print(f'special key {key} pressed')

    if key == keyboard.Key.enter:
        # Stop listener
        return False


# Execute Function degree_input() When We Need It
def take_degrees_input() -> None:
    degrees.clear()
    with keyboard.Listener(on_press=degree_input) as listener:
        listener.join()


# Execute Function color_input() When We Need It
def take_color_input() -> None:
    colors.clear()
    with keyboard.Listener(on_press=color_input) as listener:
        listener.join()

# ===============================================User Input Keys===============================================
# Basic Drawing Functions Keys
sc.onkey(end, 'x')
sc.onkey(go_home, 'y')
sc.onkey(reset_canvas, 'z')
sc.onkey(background_b, 'b')
sc.onkey(background_w, 'w')

# User Input Activation Keys
sc.onkey(take_color_input, 'c')
sc.onkey(take_degrees_input, 'd')

# Orb & Spiral Execution Keys
sc.onkey(euler_orb, 'o')
sc.onkey(euler_spiral_galaxy, 'Up')
sc.onkey(euler_spiral_illusion, 'Down')
sc.onkey(euler_spiral_web, 'Left')

sc.listen()
# ================================================Program Finish================================================
turtle.done()
