import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, DEFAULT_TYPE, DUCKING, JUMPING

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 300
    JUMP_VEL = 8.5

    def __init__(self):
        self.dino_run = {DEFAULT_TYPE: RUNNING}
        self.dino_duck = {DEFAULT_TYPE: DUCKING}
        self.dino_jump = {DEFAULT_TYPE: JUMPING}


        self.image = self.dino_run[DEFAULT_TYPE][0]
        self.type = DEFAULT_TYPE
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.steps = 0
        self.running = True
        self.ducking = False
        self.jumping = False
        self.jump_vel = self.JUMP_VEL
        self.has_lives = True

    def update(self, imput_user):
        if self.running:
            self.run()

        if self.ducking:
            self.ducking()

        if self.jumping:
            self.jumping()

        if imput_user[pygame.K_DOWN] and not self.jumping:
            self.ducking = True
            self.jumping = False
            self.running = False
        elif imput_user[pygame.K_UP] and not self.jumping:
            self.ducking = False
            self.jumping = True
            self.running = False

        elif not self.jumping:
            self.ducking = False
            self.jumping = False
            self.running = True

        if self.steps >= 10:
            self.steps = 0

    def run(self):
        self.image = self.dino_run[DEFAULT_TYPE][0] if self.steps <= 5 else self.dino_run[DEFAULT_TYPE][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.steps += 1

    def duck(self):
        self.image = self.dino_duck[DEFAULT_TYPE][0] if self.steps <= 5 else self.dino_duck[DEFAULT_TYPE][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 30
        self.steps += 1

    def jump(self):
         # self.image = self.dino_jump[self.type]
        self.image = JUMPING
        if self.jumping:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.jumping = False
            self.jump_vel = self.JUMP_VEL


    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))