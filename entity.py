from pygame import Surface, transform
from pygame.image import load
from image import fitImageScale


class Entity:
    def __init__(self, window_size: tuple[int, int], image: str, ratio_taille: float, pos: tuple[int,int]=(0,0), background_size=False):
        self.img = load(image).convert_alpha()
        self.image_og = load(image).convert_alpha()
        self.pos = pos
        self.ratio = ratio_taille
        self.background_size = background_size
        self.l_x, self.l_y=self.image_og.get_size()
        self.rect=self.img.get_rect()

        self.fit_image(window_size)

    def fit_image(self, window_size: tuple[int, int]):        
        '''if self.background_size:
            ratio_l_x= self.l_x/window_size[0]
            ratio_l_y= self.l_y/window_size[1]
            r= min(ratio_l_x, ratio_l_y)
            new_l_x= r*self.l_x
            new_l_y= r*self.l_y
            self.img = transform.scale(self.img, (new_l_x, new_l_y))'''
        
        self.img = fitImageScale(self.image_og, window_size, self.ratio)


    def update(self):
        pass

    def draw(self, ecran: Surface):
        ecran.blit(self.img, (0,0))