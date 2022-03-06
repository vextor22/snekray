from __future__ import annotations
from typing import Union
from .ptuple import PTuple
import praytracer


class Vector(PTuple):
    W = 0.0

    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z)
        self.w = self.W

    def __eq__(self, other: object) -> bool:
        return super().__eq__(other) and isinstance(other, Vector)

    def __add__(self, tup: PTuple) -> Union[Vector, praytracer.Point]:
        new_dims = super().__add__(tup).dims
        if isinstance(tup, Vector):
            return Vector(*new_dims)
        else:
            return praytracer.Point(*new_dims)

    def __sub__(self, tup: PTuple) -> Vector:
        if isinstance(tup, Vector):
            return Vector(*super().__sub__(tup).dims)
        return self

    def __neg__(self) -> Vector:
        return Vector(*super().__neg__().dims)
