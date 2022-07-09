from __future__ import annotations
import snekray as sr
from typing import cast
import math


class Material:
    def __init__(
        self,
        color: sr.Color = None,
        ambient: float = 0.1,
        diffuse: float = 0.9,
        specular: float = 0.9,
        shininess: float = 200.0,
    ) -> None:
        """Initialize a Phong material.

        Args:
            color (sr.Color, optional): A color for the material. Defaults to sr.Color(1, 1, 1).
            ambient (float, optional): Ambient light, typically 0-1. Defaults to 0.1.
            diffuse (float, optional): Diffuse brightness, 0-1. Defaults to 0.9.
            specular (float, optional): Specular reflection, 0-1. Defaults to 0.9.
            shininess (float, optional): Shininess modifier smaller values are larger, 10-200. Defaults to 200.
        """
        self.color = color if color is not None else sr.Color(1, 1, 1)
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def lighting(
        self,
        light: sr.PointLight,
        position: sr.Point,
        eye: sr.Vector,
        normal: sr.Vector,
    ) -> sr.Color:
        effective_color = self.color.hadamard(light.intensity)
        lightv = (light.position - position).normalize()

        ambient = effective_color * self.ambient

        light_dot_normal = lightv.dot(normal)
        if light_dot_normal < 0:
            diffuse = sr.Color(0, 0, 0)
            specular = sr.Color(0, 0, 0)

        else:
            diffuse = effective_color * self.diffuse * light_dot_normal
            reflectv = (lightv * -1).reflect(normal)
            reflect_dot_eye = reflectv.dot(eye)
            if reflect_dot_eye <= 0:
                specular = sr.Color(0, 0, 0)
            else:
                factor = math.pow(reflect_dot_eye, self.shininess)
                specular = sr.Color(*(light.intensity * self.specular * factor).dims)
        return sr.Color(*(diffuse + specular + ambient).dims)

    def __eq__(self, __o: object) -> bool:
        if type(self) == type(__o):
            other = cast(Material, __o)
            return (
                other.color == self.color
                and other.ambient == self.ambient
                and other.diffuse == self.diffuse
                and other.specular == self.specular
                and other.shininess == self.shininess
            )
        return False
