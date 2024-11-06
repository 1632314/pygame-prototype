import pygame

from bird import Bird
from cloud import Cloud
from factorySprites import FactorySprites
from game import Game
from jet import Jet
from missile import Missile
from mountain import Mountain
from screen import Screen
from umbrella import Umbrella

# Initialize PyGame
# setup for sounds_music, defaults are good
pygame.mixer.init()
pygame.init()
# create the screen object
pygame.display.set_mode((Screen.width, Screen.height))

level = 'difficult'

if level=='easy':
    # easy game, only birds and clouds
    factory_flying = FactorySprites([Bird()], [300], pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud()], [400], pygame.USEREVENT + 10)
elif level=='difficult':
    factory_flying = FactorySprites([Bird(), Umbrella(), Jet(), Missile()], [400, 500, 600, 700],
    pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud(), Mountain()], [500, 2000],
    pygame.USEREVENT + 10)
else:
    assert False

# play
game = Game(factory_flying, factory_landscape)
game.play()