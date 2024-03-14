from entity import Entity


class Movable(Entity):
    def __init__(self, window_size: tuple[int, int], image: str, ratio_taille: float, pos: tuple[int, int] = ..., background_size=False, se_dessinner: bool = True, hitbox: bool = False, accroche: bool = False):
        super().__init__(window_size, image, ratio_taille, pos, background_size, se_dessinner, hitbox, accroche)
        self.vitesse_y=0
        self.accroche= accroche
        self.chute=False
        self.hitbox= 0

    def statique(self):
        self.vitesse_y= 0
        self.accroche= True

    def update(self, viewbox: tuple[int, int, int, int], deltaTime: float):
        self.y+=self.applyForces(viewbox, deltaTime)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.rect.h = self.img.get_size()[1]
        self.rect.w = self.img.get_size()[0]
        self.rayon = self.rect.width/2
        self.centre = (self.pos[0]+self.l_x/2, self.pos[1]+self.l_y/2)

    def applyForces(self, viewbox: tuple[int, int, int, int], deltaTime: float):
        somme_forces= 0
        if self.chute:
            somme_forces+=5
        return(somme_forces)