from entity import Entity
from constants import VOLUME_OFF, VOLUME_ON, FULLSCREEN_OFF, FULLSCREEN_ON
from pygame.image import load
from pygame import mixer, display
'''
classe bouton:
doit pouvoir avoir deux images qui alternent.
doit avoir une fonction "bonton_appuye" qui fait l'action qu'on veut quand on appuie:
    - change l'image par une autre
    - Fait l'évènement demandé, exp: full screen/ désactiver le son
'''

class Bouton_volume(Entity):
    def __init__(self, window_size: tuple[int, int], ratio_taille: float, pos: tuple[int,int]=(0,0), background_size=False, se_dessinner: bool = True):
        super().__init__(window_size, VOLUME_ON, ratio_taille, pos)
        self.imgs = [ 
            self.img,
            load(VOLUME_OFF).convert_alpha()
        ]
        self.img_index = 0
        self.volume = True

    def action_volume(self, window_size):
        
        self.volume = not self.volume
        self.img_index= 0 if self.volume else 1
        mixer.music.set_volume(1 if self.volume else 0)
        self.image_og = self.imgs[self.img_index]
        self.fit_image(window_size)

class Bouton_screen(Entity):
    def __init__(self, window_size: tuple[int, int], ratio_taille: float, pos: tuple[int,int]=(0,0), background_size=False, se_dessinner: bool = True):
        super().__init__(window_size, FULLSCREEN_OFF, ratio_taille, pos)
        self.imgs = [ 
            self.img,
            load(FULLSCREEN_ON).convert_alpha()            
        ]
        self.img_index = 0
        self.screen = True

    def action_screen(self, window_size):
        
        self.screen = not self.screen
        self.img_index= 0 if self.screen else 1
        display.toggle_fullscreen()
        self.image_og = self.imgs[self.img_index]
        self.fit_image(window_size)