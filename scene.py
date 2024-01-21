from entity import Entity
from typing import List

class Scene:
    def __init__(self):
        self.entities: List[Entity] = []

    def draw(self):
        for entity in self.entities:
            entity.draw()

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