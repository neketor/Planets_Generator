from functions import *
from random import randint, choice
from datetime import datetime
from render import *
from Classes import *



def galaxy_sys_generator(is_render=True):
    galaxy = Galaxy_sys(generate_alphanum_random_string(randint(4, 10)))
    if is_render:
        for i in range(100):
            # Вызываем функцию circle_pos для каждого круга спирали
            positions = circle_pos(galaxy.center_x, galaxy.center_y, galaxy.points, galaxy.angle, galaxy.radius)
            # Рисуем точки на изображении
            for pos in positions:
                color = (255, 255, 255)
                ellipse(draw, pos[0]+randint(-abs(i-100)//10, abs(i-100)//10), pos[1]+randint(-abs(i-100)//10, abs(i-100)//10), galaxy.size, galaxy.size, color, outline=None)
                galaxy.size -= galaxy.size_minus
                print(galaxy.size)
            galaxy.radius += galaxy.radius_plus  # Увеличиваем радиус для создания спирали
            galaxy.angle += galaxy.angle_plus # Увеличиваем угол для вращения спирали
        print(galaxy.radius)
        print(galaxy); print(galaxy.angle)
        im.save('draw-ellipse-rectangle-line.jpg', quality=95)
        im.show()
    else:
        print(galaxy)
a = galaxy_sys_generator()