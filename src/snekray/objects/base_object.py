from __future__ import annotations

import snekray as sr
from typing import Tuple, Union


class BaseObject:
    def __init__(self) -> None:
        self.origin = sr.Point(0, 0, 0)

    def intersect(
        self, ray: sr.Ray
    ) -> Union[Tuple[()], Tuple[sr.Intersection, sr.Intersection]]:
        raise NotImplemented
