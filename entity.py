from pygame import surface
from pygame.image import load
from image import fitImageScale

class Entity:
    def __init__(self, window_size: tuple[int, int], image: str, ratio_taille: float, pos: tuple[int,int]=(0,0), background_size=False):
        self.image= load(image).convert_alpha()
        self.image_og= load(image).convert_alpha()
        self.pos= pos
        self.ratio= ratio_taille
        self.background_size = background_size

        self.fit_image(window_size)

    def fit_image(self, window_size: tuple[int, int]):
        ratio= self.ratio

        if self.background_size=="cover":
            #comparaison des ratios entre fenêtre 
            ratio_f= window_size[0]/window_size[1] 
            # r>1 => x>y
            # r<1 => x<y
            # r=1 => x=y
            if ratio_f==1:
                pass # todo
            
            elif ratio_f<1:
                pass # todo
            
            elif ratio_f>1:
                pass #todo

        elif self.background_size == "contain":
            pass #todo

        self.image= fitImageScale(self.image_og, window_size, ratio)