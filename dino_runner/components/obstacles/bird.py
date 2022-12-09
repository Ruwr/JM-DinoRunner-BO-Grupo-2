import random
from dino_runner.components.obstacles.obstacles import Obstacle


class Bird(Obstacle):
    
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(self, image.type) 
        self.rect.y = random.randint(300,350)