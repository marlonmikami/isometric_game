max_color_range = 150
min_color_range = 50
color_change_value = 1


color_shift = "B"
r = min_color_range
g = min_color_range
b = min_color_range


def get_color():
    define_screen_color()
    return r, g, b


def define_screen_color():
    global color_shift, r, g, b
    # Define the screen color
    if color_shift == "R":
        r = increase_color_value(r)
        g = decrease_color_value(g)
        b = decrease_color_value(b)
        if r >= max_color_range:
            color_shift = "G"
    if color_shift == "G":
        g = increase_color_value(g)
        r = decrease_color_value(r)
        b = decrease_color_value(b)
        if g >= max_color_range:
            color_shift = "B"
    if color_shift == "B":
        b = increase_color_value(b)
        r = decrease_color_value(r)
        g = decrease_color_value(g)
        if b >= max_color_range:
            color_shift = "R"


def decrease_color_value(color):
    global min_color_range
    if color > min_color_range:
        color -= color_change_value
    if color < min_color_range:
        color = min_color_range
    return color


def increase_color_value(color):
    global max_color_range
    if color < max_color_range:
        color += color_change_value
    if color > max_color_range:
        color = max_color_range
    return color