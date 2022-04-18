from __future__ import annotations
from typing import Union
from .ptuple import PTuple
import snekray


class Color(PTuple):
    __name__: str = "Color"
    W = 0.0

    def __init__(self, red: float, green: float, blue: float) -> None:
        super().__init__(red, green, blue)
        self.w = self.W

    @property
    def red(self):
        return self.x

    @property
    def green(self):
        return self.y

    @property
    def blue(self):
        return self.z

    def hadamard(self, other: Color) -> Color:
        return Color(
            self.red * other.red, self.green * other.green, self.blue * other.blue
        )
