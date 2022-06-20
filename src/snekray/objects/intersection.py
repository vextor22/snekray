from __future__ import annotations
from typing import List, Optional
import snekray as sr


class Intersection:
    def __init__(self, t: float, bo: sr.BaseObject) -> None:
        self.t = t
        self.object = bo

    @classmethod
    def sorted(cls, *intersections: Intersection) -> List[Intersection]:
        return sorted(intersections, key=lambda x: x.t)

    @classmethod
    def hit(cls, intersections: List[Intersection]) -> Optional[Intersection]:
        return next((i for i in intersections if i.t > 0), None)
