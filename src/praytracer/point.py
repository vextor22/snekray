from __future__ import annotations
from .ptuple import PTuple
import praytracer.vector as vector


class Point(PTuple):
    W = 1.0

    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z)
        self.w = self.W

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o) and isinstance(__o, Point)

    def __add__(self, tup: PTuple) -> Point:
        if isinstance(tup, vector.Vector):
            new_point = super().__add__(tup)
            return Point(new_point.x, new_point.y, new_point.z)
        return self
