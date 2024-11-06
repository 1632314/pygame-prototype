import pygame
import random
import math

from pygame.examples.scrap_clipboard import screen
from pygame.locals import RLEACCEL

from gameSprite import GameSprite
from screen import Screen


# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Umbrella(GameSprite):
    Max_Speed = 10
    Min_Speed = 5

    def __init__(self):
        super(Umbrella, self).__init__()
        self.surf = pygame.image.load("icons/umbrella.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0 + 20, Screen.width-20),
                0
            )
            #     random.randint(0, Screen.height),
            # )
        )
        self.speed = random.randint(self.Min_Speed, self.Max_Speed)
        self.time = 0

    # Move the bird based on speed
    # Remove it when it passes the left edge of the screen.py
    def update(self):
        self.time += 1
        #speed_x = -self.speed
        speed_y = self.speed
        self.rect.move_ip(0, speed_y)
        if self.rect.top > Screen.height:
            self.kill()

    def clone(self):
        return Umbrella()