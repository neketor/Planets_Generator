import random
import string
from render import *
import math

planet_types_freeze = ["Снежная", "Ледяная"]
planet_types_other = ["Токсичная", "Радиационная", "Ядерная", "Мертвая"]
planet_types_normal = ["Каменная", "Водная", "Пустынная"]
terrain_types = ["Равнинная", "Холмистая", "Горная"]
size_types = ["Карликовая планета", "Средняя планета", "Газовый гигант"]

# Other_functions
def generate_alphanum_random_string(length):
    """Подбирает имя из рандомных символов, указав его длину."""
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string

def ellipse(draw, x, y, width, height, color = "white", outline = "white"):
  draw.ellipse((x, y, x+width, y+height), fill=color, outline=outline)

def circle_pos(x, y, points, starting_angle, circle_radius):
    pos = []
    angle_inc = 360 / points
    for i in range(points):
        angle = math.radians(starting_angle + (i * angle_inc))
        pos.append((x+(circle_radius*math.cos(angle)), y+(circle_radius*math.sin(angle))))
    return pos

# Planet_functions
def get_type(temperature):
    """Подбирает тип планеты, изходя из температуры."""
    if temperature > -5 and temperature < 50:
        return random.choice(planet_types_normal)
    elif temperature > -80 and temperature < 2:
        return random.choice(planet_types_freeze)
    else:
        return random.choice(planet_types_other)


def get_size_type(size):
    """Подбирает вид величины планеты (строка 8), исходя из её диаметра."""
    if size < 3200:
        return size_types[0]
    elif size > 100000:
        return size_types[2]
    else:
        return size_types[1]

def is_colony(temperature):
    """Определяет, колонизирована ли планета исходя из температуры."""
    if temperature > 10 and temperature < 30:
        return True
    return False

def get_pl_color(temperature, color):
    """Подбирает цвет планеты, изходя из температуры."""
    r = 0; g = 0; b = 0
    if temperature >= -5 and temperature <= 70:
        g += abs(temperature)
    elif temperature >= -100 and temperature <= -5:
        b+=abs(temperature)
    else:
        r+=abs(temperature)

    light_r = (r + 255) // 2
    light_g = (g + 255) // 2
    light_b = (b + 255) // 2
    return (light_r, light_g, light_b)

def planet_info_in_text(x, y, planet):
    draw.text((x, y), str(planet), font=planet_info)

