from entity import Entity
from pygame.image import load
from pygame import mouse
from constants import CAROTTE, NUAGE

class Mouse(Entity):
    # on reprend le constructeur de Entity
    # pour passer tout les paramètres à Entity
    # puisque Mouse hérite de Entity
    # sauf pour l'image qu'on va définir nous-même à l'intérieur de cette classe
    def __init__(self, window_size: tuple[int, int], ratio_taille: float, pos: tuple[int,int]=(0,0), background_size=False, se_dessinner: bool = True):
        super().__init__(window_size, CAROTTE, ratio_taille, pos, background_size, se_dessinner)
        
        # ceci est une liste des différentes images de la souris
        self.imgs = [ # tu noteras le s à la fin de img qui n'est pas pareil que self.img qui est l'image courante modifiée par le resize
            self.img, # carotte
            load(NUAGE).convert_alpha() # nuage
        ]

        self.img_index = 0 # index de l'image courante dans la liste des images

        # par défaut, self.img est donc carotte2.png (ligne 10)

    def updateState(self, window_size: tuple[int, int]):
        (mouse_x, mouse_y) = mouse.get_pos()

        limit_left = 7/24 * window_size[0]
        limit_right = 149/200 * window_size[0]

        is_in_limits = mouse_x >= limit_left and mouse_x <= limit_right

        # si la souris est dans les limites et que l'image courante est la carotte
        # on change en nuage        
        if is_in_limits and self.img_index == 0:
            self.img_index = 1
            self.img = self.imgs[self.img_index]
            self.fit_image(window_size)

        # si la souris n'est pas dans les limites et que l'image courante est le nuage
        # on change en carotte
        elif not is_in_limits and self.img_index == 1:
            self.img_index = 0
            self.img = self.imgs[self.img_index]
            self.fit_image(window_size)

        # Remarque : On ne CHANGE PAS l'image courante si elle est déjà la bonne
        # ce qui évite de blink. C'est pour ça qu'on fait toujours 2 vérifications :
        # 1. est-ce que la souris est dans les limites ?
        # 2. est-ce que l'image courante est déjà celle voulue ou non ?
