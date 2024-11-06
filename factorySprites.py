from typing import List

import pygame
import random
import math

from pygame.examples.sprite_texture import event
from pygame.locals import RLEACCEL

from screen import Screen

class FactorySprites:
    event_types: list[int]

    def __init__(self, objects: list, periods: list, eventID : int  ):
        self._prototypes = objects
        self.periods = periods
        self.event_types = [id for id in range(eventID, eventID + len(self._prototypes))]

    def make(self, event_type):
        # we return a clone of the element starting from the first one
        return self._prototypes[event_type - self.event_types[0]].clone()