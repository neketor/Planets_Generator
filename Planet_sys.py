from functions import *
import os
from random import randint, choice
from datetime import datetime
from render import *

class Planet:
    def __init__(self, name, size, gravitation, temperature):
        self.name = name
        self.size = size
        self.color_pl = (0, 0, 0)
        self.temperature = temperature
        self.pl_type = get_type(temperature)
        self.terr_type = choice(terrain_types)
        self.grav = gravitation
        self.size_type = get_size_type(size)
        self.is_colony = is_colony(temperature)
        self.birth = datetime.now()
        self.number = 0

    def __str__(self):
        return f"   Информация о планете {self.name} №{self.number}: \n       Тип планеты: {self.pl_type}\n       Тип местности планеты: {self.terr_type}\n       Размер планеты: {self.size}км \n       Гравитация планеты: {self.grav}H\n       Температура планеты: {self.temperature}°С\n       Колонизирована ли планета: {self.is_colony}\n       Время рождения планеты: {self.birth}\n    {self.size_type}"


class Planet_sys:
    def __init__(self, name):
        self.name = name
        # self.planets = [Planet(generate_alphanum_random_string(randint(4, 10)), randint(2000, 150000), randint(1, 100), randint(-120, 120)) for i in range(randint(3, 8))]
        self.planets = []


    def __str__(self):
        return f"Список планет в планетарной системе {self.name}: \n\n"+"".join([str(i)+"\n\n" for i in self.planets])

def Planet_sys_Generator(name):
    """Генерация планетарной системы с изображением."""
    Pl_sys = Planet_sys(name)
    r = 300
    r_minus = 70
    text_pos = [40, 20]
    for belt in range(randint(2, 4)):# Отрисовка поясов, и размещение планет по ним.
        planets_count = 0
        belt = circle_pos(450, 400, 800, 0, r)
        planets_belt = circle_pos(450, 400, randint(1, 3), randint(-30, 30), r)
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
        r = r-r_minus

    im.save('draw-ellipse-rectangle-line.jpg', quality=95)
    im.show()

Planet_sys_Generator("Pon")