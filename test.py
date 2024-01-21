import pygame, random

class Fruit :
    def __init__(self, rayon: int, nature:str):
        self.rayon= rayon
        self.nature= nature
        #self.image= pygame.image.load(nature+".png").convert_alpha()

class Tomate(Fruit):
    def __init__(self, rayon: int):
        super().__init__(rayon, "tomate")     

class Melon(Fruit):
    def __init__(self, rayon: int):
        super().__init__(rayon, "Melon")
       
class Poire(Fruit):
    def __init__(self, rayon: int):
        super().__init__(rayon, "Poire")



Ma_tomate= Tomate(10)
pygame.display(Ma_tomate.image)