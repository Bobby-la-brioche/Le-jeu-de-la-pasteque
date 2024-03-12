from entity import Entity


class Movable(Entity):
    def __init__(self, window_size: tuple[int, int], image: str, ratio_taille: float, pos: tuple[int, int] = ..., background_size=False, se_dessinner: bool = True, hitbox: bool = False, accroche: bool = False):
        super().__init__(window_size, image, ratio_taille, pos, background_size, se_dessinner, hitbox, accroche)
        self.vitesse_y=0
        self.accroche= accroche
        self.chute=False
        self.hitbox= 0
        self.draw_hitbox= True

    def statique(self):
        self.vitesse_y= 0
        self.accroche= True

    def update(self, viewbox: tuple[int, int, int, int], deltaTime: float):
        self.applyForces(viewbox, deltaTime)

    def applyForces(self, viewbox: tuple[int, int, int, int], deltaTime: float):
        # faire des choses physiques ici