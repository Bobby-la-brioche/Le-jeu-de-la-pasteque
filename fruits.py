from entity import Entity
from constants import VOLUME_OFF, VOLUME_ON, FULLSCREEN_OFF, FULLSCREEN_ON
from pygame.image import load
from pygame import draw
from image import fitImageScale

class Fruit(Entity):
    def __init__(self, window_size: tuple[int, int], image, ratio_taille: float, ecran, pos: tuple[int, int] = ..., background_size=False, se_dessinner: bool = True, hitbox: bool = False):
        super().__init__(window_size, image, ratio_taille, pos, background_size, se_dessinner, hitbox)
    
        self.hitbox= 0
        self.fruit = True
        self.draw_hitbox= False