from pygame import Surface, transform, Rect, draw, mouse
from pygame.image import load
from image import fitImageScale
from pygame.locals import SRCALPHA


class Entity():
    def __init__(self, window_size: tuple[int, int], image: str, ratio_taille: float, pos: tuple[int,int]=(0,0), background_size=False, se_dessinner: bool = True, hitbox: bool = False):
        self.img = load(image).convert_alpha()
        self.image_og = load(image).convert_alpha()
        self.pos = pos
        self.se_dessinner = se_dessinner
        self.ratio = ratio_taille
        self.background_size = background_size
        self.l_x, self.l_y=self.img.get_size()
        self.rect=self.img.get_rect()
        self.draw_hitbox= hitbox
        self.trait_nuage= False
        self.fruit = False
        self.rayon = self.rect.x/2
        self.centre = (self.pos[0]+self.l_x/2, self.pos[1]+self.l_y/2)
        
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
        self.l_x, self.l_y=self.img.get_size()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.rect.h = self.img.get_size()[1]
        self.rect.w = self.img.get_size()[0]
        self.rayon = self.rect.width/2
        self.centre = (self.pos[0]+self.l_x/2, self.pos[1]+self.l_y/2)

    def draw(self, ecran: Surface,windowsize):
        if self.trait_nuage:
            draw.line(ecran,(200, 200, 200),(self.pos[0]+self.l_x/2, self.pos[1]+self.l_y/2), (self.pos[0]+self.l_x/2,windowsize[1]), 2)
        ecran.blit(self.img, self.rect)
        if self.draw_hitbox:
            draw.rect(ecran, (255,0,0), Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height),  3)
        if self.fruit:
            self.hitbox =draw.circle(ecran, (0,0,0), self.centre, self.rayon, 1)