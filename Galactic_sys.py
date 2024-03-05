from functions import *
from random import randint, choice
from datetime import datetime

class Planet:
    def __init__(self, name, size, gravitation, temperature):
        self.name = name
        self.size = size
        self.temperature = temperature
        self.pl_type = get_type(temperature)
        self.terr_type = choice(terrain_types)
        self.grav = gravitation
        self.size_type = get_size_type(size)
        self.is_colony = is_colony(temperature)
        self.birth = datetime.now()

    def __str__(self):
        return f"Информация о планете {self.name}: \n   Тип планеты: {self.pl_type}\n   Тип местности планеты: {self.terr_type}\n   Размер планеты: {self.size}км \n   Гравитация планеты: {self.grav}H\n   Температура планеты: {self.temperature}°С\n   Колонизирована ли планета: {self.is_colony}\n   Время рождения планеты: {self.birth}\n    {self.size_type}"

class Planet_sys:
    def __init__(self, name):
        self.name = name
        self.planets = [Planet(generate_alphanum_random_string(randint(4, 10)), randint(2000, 150000), randint(1, 100), randint(-120, 120)) for i in range(randint(3, 8))]

    def __str__(self):
        return f"Список планет в планетарной системе {self.name}: \n"+"".join([str(i)+"\n\n" for i in self.planets])

class Galactic:
    def __init__(self, name):
        self.name = name
        self.diameter = randint(10000, 1000000)
        self.sol_sys = [Planet_sys(generate_alphanum_random_string(randint(4, 10))) for i in range(randint(50, 200))]

    def __str__(self):
        return f"Имя галактики: {self.name} | Диаметр галактики {self.diameter} | Состав галактики: Планетарных систем: {len(self.sol_sys)}\n Планетарные системы данной галактики:\n"+"".join([str(i)+"\n\n" for i in self.sol_sys])

galactic_sys = Galactic(generate_alphanum_random_string(randint(4, 10)))
print(galactic_sys)