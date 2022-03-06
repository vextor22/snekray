from __future__ import annotations
from typing import Union
from .ptuple import PTuple
import praytracer


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

    def __sub__(self, tup: PTuple) -> Vector:
        new_vec = super().__sub__(tup)
        if isinstance(tup, Vector):
            return Vector(new_vec.x, new_vec.y, new_vec.z)
        return self

    def __neg__(self) -> Vector:
        tup = super().__neg__()
        return Vector(tup.x, tup.y, tup.z)
