from __future__ import annotations
from typing import Union
from .ptuple import PTuple
import praytracer.point


class Vector(PTuple):
    W = 0.0

    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z)
        self.w = self.W

    def __eq__(self, p2: object) -> bool:
        return super().__eq__(p2) and isinstance(p2, Vector)

    def __add__(self, tup: PTuple) -> Union[Vector, praytracer.Point]:
        new_values = super().__add__(tup)
        if isinstance(tup, Vector):
            return Vector(new_values.x, new_values.y, new_values.z)
        else:
            return praytracer.Point(new_values.x, new_values.y, new_values.z)
