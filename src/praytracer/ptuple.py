from __future__ import annotations
from typing import cast
import math


class PTuple:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.dims = (self.x, self.y, self.z)

    def __eq__(self, other: object) -> bool:
        return all(math.isclose(*d) for d in zip(self.dims, cast(PTuple, other).dims))

    def __add__(self, tup: PTuple) -> PTuple:
        return PTuple(self.x + tup.x, self.y + tup.y, self.z + tup.z)

    def __sub__(self, tup: PTuple) -> PTuple:
        return PTuple(self.x - tup.x, self.y - tup.y, self.z - tup.z)

    def __neg__(self) -> PTuple:
        return PTuple(*(-dim for dim in self.dims))
