from entity import Entity
from typing import List
from pygame import Surface
from line import Ligne

# Todo : add layers
class Scene:
    def __init__(self):
        self.entities: List[Entity] = []
        self.lignes: List[Ligne]= []

    def draw(self, ecran: Surface, windowsize):
        for entity in self.entities:
            if entity.se_dessinner:
                entity.draw(ecran, windowsize)
        for ligne in self.lignes:
            if ligne.se_dessinner:
                ligne.draw(ecran)

    def update(self):
        for entity in self.entities:
            entity.update()
        for ligne in self.lignes:
            ligne.update()

    def add_entity(self, entity: Entity, *args: Entity):
        self.entities.append(entity)
        
        for arg in args:
            self.entities.append(arg)

    def remove_entity(self, entity: Entity, *args: Entity):
        self.entities.remove(entity)

        for arg in args:
            self.entities.remove(arg)
    
    def add_ligne(self, ligne: Ligne, *args: Ligne):
        self.lignes.append(ligne)

        for arg in args:
            self.lignes.append(arg)

    def remove_entity(self, ligne: Ligne, *args: Ligne):
        self.lignes.remove(ligne)

        for arg in args:
            self.lignes.remove(arg)

    def fit_image(self, window_size: tuple[int, int]):
        for entity in self.entities:
                entity.fit_image(window_size)
