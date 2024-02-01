from entity import Entity
from typing import List
from pygame import Surface

# Todo : add layers
class Scene:
    def __init__(self):
        self.entities: List[Entity] = []

    def draw(self, ecran: Surface):
        for entity in self.entities:
            if entity.se_dessinner:
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

    def fit_image(self, window_size: tuple[int, int]):
        for entity in self.entities:
                entity.fit_image(window_size)


    def isPresent(self, actor: Entity) -> bool:
        return actor in self.entities