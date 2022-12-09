from dino_runner.utils.constants import HEART_COUNT
from dino_runner.components.player_hearts.hearts import Heart


class PlayerHeartManager:
    def _init_(self):
        self.heart_count = HEART_COUNT
        
    def draw(self, screen):
        x_postion = 10
        y_postion = 20

        for counter in range(self.heart_count):
            heart = Heart(x_postion, y_postion)
            heart.draw(screen)
            x_postion += 30

    def reduce_heart(self):
        self.heart_count -= 1