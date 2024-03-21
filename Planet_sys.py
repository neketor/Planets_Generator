from functions import *
from random import randint, choice
from datetime import datetime
from render import *
from Classes import *


def Planet_sys_Generator(name):
    """Генерация планетарной системы с изображением."""
    Pl_sys = Planet_sys(name)
    r = 300
    r_minus = 70
    text_pos = [40, 20]
    for belt in range(randint(2, 4)):# Отрисовка поясов, и размещение планет по ним.
        planets_count = 0
        belt = circle_pos(450, 450, 800, 0, r)
        planets_belt = circle_pos(450, 450, randint(1, 3), randint(-30, 30), r)
        for pos in belt:
            ellipse(draw, pos[0], pos[1], 1, 1, "white")
        for pos in planets_belt:
            planets_count += 1
            planet_diam = randint(2000, 150000)
            pl_render_diam = (planet_diam / 1000) / 2
            planet = Planet(generate_alphanum_random_string(randint(4, 10)), planet_diam, randint(1, 100), randint(-120, 120)); planet.number = len(Pl_sys.planets)
            planet.color_pl = get_pl_color(planet.temperature, planet.color_pl)
            ellipse(draw, pos[0]-pl_render_diam/2, pos[1]-pl_render_diam/2, pl_render_diam, pl_render_diam, planet.color_pl)
            Pl_sys.planets.append(planet)
            draw.text((pos[0]+pl_render_diam/2, pos[1]+pl_render_diam/2), str(len(Pl_sys.planets)), font=headline)
            print(planet)
        r = r-r_minus

    im.save('draw-ellipse-rectangle-line.jpg', quality=95)
    im.show()

Planet_sys_Generator("Pon")