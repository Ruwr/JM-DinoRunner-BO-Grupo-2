import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS
import pygame

class ObstacleManage():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(0,1)
            if cactus_size == 0:
                self.large_cactus = Cactus(LARGE_CACTUS)
                self.large_cactus.rect.x = 300
                self.obstacles.append(Cactus(LARGE_CACTUS))
                
            elif cactus_size == 1:
                self.obstacles.append(Bird(BIRD))
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacles in self.obstacles:
            obstacles.update(game.game_speed, self.obstacles)
            if game.dino.dino_rect.colliderect(Obstacle.rect):
                pygame.time.delay(100)
                game.player_heart_manager.reduce_heart()
                
                if game.player_heart_manager.heart_count > 0:
                    self.obstacles.pop()
                    game.dino.has_lives = True
                else:
                    game.dino.has_lives = False
                    game.playing = False
                    game.death_count += 1
                    break



    def draw(self, screem):
        for obstacle in self.obstacles:
            obstacle.draw(screem)

