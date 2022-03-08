from time import sleep
from typing import Optional, Sequence
from dotenv import load_dotenv

load_dotenv(override=True)

import os

print(os.environ.get("PYTHONPATH", "none"))
from snekray import SnekRay, Point, Vector


tracer = SnekRay()

print(f"Render at: {tracer.get_dimensions()}")


# Example Projectile


class PObject:
    __name__ = "PObject"

    def __init__(self, position=None, direction=None) -> None:
        self.position = position or Point(0, 1, 0)
        self.velocity = direction or Vector(1, 1, 0).normalize()

    def apply_velocity(self):
        self.position += self.velocity

    def update(self, *forces):
        self.apply_velocity()
        self.velocity += sum(forces, start=Vector(0, 0, 0))

    def __repr__(self) -> str:
        return f"{self.__name__} is at {self.position} with a speed of {self.velocity.magnitude()}"


class Projectile(PObject):
    __name__ = "Projectile"

    def __init__(self, position=None, direction=None, magnitude=None) -> None:
        super().__init__(position, direction)
        if magnitude is not None:
            self.velocity = self.velocity * magnitude


class Environment:
    def __init__(
        self,
        gravity: Optional[Vector] = None,
        wind: Optional[Vector] = None,
        obj_list: Optional[list[PObject]] = None,
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


projectile = Projectile(direction=Vector(0.75, 1, 0), magnitude=20)
env = Environment()
env.register_object(projectile)

while env.tick() > 0:
    if env.tick_count % 50 == 0:
        print(f"Current tick: {env.tick_count}, {projectile}", end="\r")
        sleep(0.5)
    pass

print(f"We got to {projectile.position} at a final tick of {env.tick_count}")
