import pygame
import random

HEIGHT = 720


class Rock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 80
        self.image = pygame.image.load("assets/Ink_Droplet.png")
        self.speed = random.randrange(1, 15)

    def move(self):
        self.y += self.speed
        if (self.y > HEIGHT - 20):
            self.y = 0
