from __future__ import annotations
import snekray as sr


class PointLight(sr.BaseObject):
    def __init__(self, position: sr.Point, intensity: sr.Color) -> None:
        super().__init__(position)
        self.intensity = intensity

    @property
    def position(self):
        return self.origin
