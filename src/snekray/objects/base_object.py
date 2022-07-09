from __future__ import annotations

import snekray as sr
from typing import Tuple, Union


class BaseObject:
    def __init__(self, position: sr.Point = None) -> None:
        self.origin = sr.Point(0, 0, 0) if position is None else position

    def intersect(
        self, ray: sr.Ray
    ) -> Union[Tuple[()], Tuple[sr.Intersection, sr.Intersection]]:
        raise NotImplemented

    def normal_at(self, p: sr.Point) -> sr.Vector:
        raise NotImplemented
