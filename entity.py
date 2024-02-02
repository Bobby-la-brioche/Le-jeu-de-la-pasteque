from pygame import Surface, transform
from pygame.image import load
from image import fitImageScale
from pygame.locals import SRCALPHA


class Entity:
    def __init__(self, window_size: tuple[int, int], image: str, ratio_taille: float, pos: tuple[int,int]=(0,0), background_size=False, se_dessinner: bool = True):
        self.img = load(image).convert_alpha()
        self.image_og = load(image).convert_alpha()
        self.pos = pos
        self.se_dessinner = se_dessinner
        self.ratio = ratio_taille
        self.background_size = background_size
        self.l_x, self.l_y=self.img.get_size()
        self.rect=self.img.get_rect()

        self.fit_image(window_size)

    def fit_image(self, window_size: tuple[int, int]):

        if self.background_size:        
            w, h = self.image_og.get_size()
            ratio = w/h
            W, H = window_size
            img_ratio_w= W/w
            img_ratio_h=H/h
            true_ratio= min(img_ratio_w, img_ratio_h)

            if true_ratio==img_ratio_w:
                newW = int(window_size[0] * self.ratio)
                newH = int(newW / ratio)
            
            else:
                newH = int(window_size[1]*self.ratio)
                newW = int(newH*ratio)

            img = Surface((w, h), flags=SRCALPHA)
            self.pos=((window_size[0]-newW)/2, 0)
            img.blit(self.image_og, (0, 0))
            self.img = transform.scale(img, (newW, newH))

            
        else:
            self.img = fitImageScale(self.image_og, window_size, self.ratio)


    def update(self):
        pass

    def draw(self, ecran: Surface):
        ecran.blit(self.img, self.pos)