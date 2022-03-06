from __future__ import annotations
from typing import cast
import math


class PTuple(object):
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, p2: object) -> bool:
        if issubclass(type(p2), PTuple):
            p2 = cast(PTuple, p2)
            if all(
                [
                    math.isclose(p2.x, self.x),
                    math.isclose(p2.y, self.y),
                    math.isclose(p2.z, self.z),
                ]
            ):
                return True

        return False

    def __add__(self, tup: PTuple) -> PTuple:
        return PTuple(self.x + tup.x, self.y + tup.y, self.z + tup.z)

    def __sub__(self, tup: PTuple) -> PTuple:
        return PTuple(self.x - tup.x, self.y - tup.y, self.z - tup.z)

    def __neg__(self) -> PTuple:
        return PTuple(-self.x, -self.y, -self.z)
