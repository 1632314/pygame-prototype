from abc import abstractmethod

import pygame
import random
import math
from pygame.locals import RLEACCEL

from screen import Screen

class GameSprite(pygame.sprite.Sprite):

    @abstractmethod
    def clone(self):
        pass