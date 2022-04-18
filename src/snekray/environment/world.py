from typing import Optional, List
from snekray import Vector

from .objects import PObject


class Environment:
    def __init__(
        self,
        gravity: Optional[Vector] = None,
        wind: Optional[Vector] = None,
        obj_list: Optional[List[PObject]] = None,
    ) -> None:
        self.gravity = gravity or Vector(0, -0.1, 0)
        self.wind = wind or Vector(-0.01, 0, 0)
        self.registered_objects: list[PObject] = obj_list or []
        self.tick_count: int = 0

    def register_object(self, obj: PObject):
        self.registered_objects.append(obj)

    def tick(self) -> int:
        objects_encountered = 0
        self.tick_count += 1
        for obj in filter(lambda x: x.position.y > 0, self.registered_objects):
            obj.update(self.gravity, self.wind)
            objects_encountered += 1
        return objects_encountered
