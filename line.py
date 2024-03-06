from pygame import draw, Surface, Rect

class Ligne():
    def __init__(self, start_point: tuple[int,int], end_point:tuple[int,int], color: tuple[int,int,int], sol = False) -> Rect:
        self.start_point= start_point
        self.end_point= end_point
        self.color=color
        self.se_dessinner= True
        self.sol = sol

    def draw(self, ecran: Surface):
        draw.line(ecran, self.color, self.start_point, self.end_point, 1)

    def update(self, WINDOW_SIZE):
        pass