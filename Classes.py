from functions import *
from random import randint, choice, uniform
from datetime import datetime

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
        return f"Список планет в планетной системе {self.name}: \n\n"+"".join([str(i)+"\n\n" for i in self.planets])

class Galaxy_sys:
    def __init__(self, name):
        self.name = name
        self.diameter = 0

        #render_settings
        self.center_x = 450; self.center_y = 450
        self.radius = 10; self.radius_plus = uniform(1, 3)
        self.points = 2
        self.angle = 0; self.angle_plus = randint(1, 4)
        self.size = 20; self.size_minus = self.size / 100 * 0.3
        self.type_ = get_galaxy_type(self.points, self.angle_plus)

    def __str__(self):
        return f"   Информация о галактике {self.name}\n       Тип галактики: {self.type_}\n       Диаметр галактики: {self.diameter}"


