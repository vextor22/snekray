from __future__ import annotations
import snekray as sr


class Ray:
    def __init__(self, origin: sr.Point, direction: sr.Vector) -> None:
        self.origin = origin
        self.direction = direction

    def position(self, t: float) -> sr.Point:
        return self.origin + self.direction * t

    def transform(self, m: sr.Matrix) -> Ray:
        return Ray(self.origin.mat_mul(m), self.direction.mat_mul(m))
