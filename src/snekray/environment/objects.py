import snekray

Point = snekray.Point
Vector = snekray.Vector


class PObject:
    __name__ = "PObject"

    def __init__(self, position: Point = None, direction: Vector = None) -> None:
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

    def __init__(
        self, position: Point = None, direction: Vector = None, magnitude: float = None
    ) -> None:
        super().__init__(position, direction)
        if magnitude is not None:
            self.velocity = self.velocity * magnitude
