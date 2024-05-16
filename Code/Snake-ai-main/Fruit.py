from pygame.math import Vector2
from Constants import BANNER_HEIGHT, NO_OF_CELLS
import random



class Fruit:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.generate_fruit() 

    def generate_fruit(self):
        border = NO_OF_CELLS - 1

        x = random.randrange(1, border)
        y = random.randrange(BANNER_HEIGHT, border)
        self.position = Vector2(x, y)

