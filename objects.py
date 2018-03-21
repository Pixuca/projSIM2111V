import random
class robo:
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    color = (153, 51, 0)

class bola:
    x = 400
    y = 300
    thickness = 10
    color = (255, 255, 0)

class line:
    xi = robo.x
    yi = robo.y
    xf = bola.x
    yf = bola.y
    thickness = 1
    color = (0, 0, 0)
