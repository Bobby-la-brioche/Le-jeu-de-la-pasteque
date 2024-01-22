from entity import Entity
from typing import List
from pygame import Surface

# Todo : add layers
class Scene:
    def __init__(self):
        self.entities: List[Entity] = []

    def draw(self, ecran: Surface):
        for entity in self.entities:
            entity.draw(ecran)

    def update(self):
        for entity in self.entities:
            entity.update()

    def add_entity(self, entity: Entity, *args: Entity):
        self.entities.append(entity)
        
        for arg in args:
            self.entities.append(arg)

    def remove_entity(self, entity: Entity, *args: Entity):
        self.entities.remove(entity)

        for arg in args:
            self.entities.remove(arg)