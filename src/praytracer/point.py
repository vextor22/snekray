from __future__ import annotations
from typing import Union
from .ptuple import PTuple
import praytracer


class Point(PTuple):
    W = 1.0

    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z)
        self.w = self.W

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o) and isinstance(__o, Point)

    def __add__(self, tup: PTuple) -> Point:
        if isinstance(tup, praytracer.Vector):
            new_point = super().__add__(tup)
            return Point(new_point.x, new_point.y, new_point.z)
        return self

    def __sub__(self, tup: PTuple) -> Union[praytracer.Vector, Point]:
        new_vec = super().__sub__(tup)
        if isinstance(tup, Point):
            return praytracer.Vector(new_vec.x, new_vec.y, new_vec.z)
        else:
            return Point(new_vec.x, new_vec.y, new_vec.z)
