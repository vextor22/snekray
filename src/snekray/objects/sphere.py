from __future__ import annotations
import snekray as sr
import math
from typing import Tuple, Union, cast, Optional


class Sphere(sr.BaseObject):
    def __init__(self, material: Optional[sr.Material] = None) -> None:
        super().__init__()
        self.radius = 1
        self.material = sr.Material() if material is None else material
        self._transform = sr.Matrix.identity_matrix()

    @property
    def transform(self) -> sr.Matrix:
        return self._transform

    @transform.setter
    def transform(self, value: sr.Matrix) -> None:
        self._transform = value

    def intersect(
        self, ray: sr.Ray
    ) -> Union[Tuple[()], Tuple[sr.Intersection, sr.Intersection]]:
        ray = ray.transform(self.transform.inverse())

        sphere_to_ray = cast(sr.Vector, ray.origin - sr.Point(0, 0, 0))
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1

        discriminant = pow(b, 2) - 4 * a * c

        if discriminant < 0:
            return ()

        t1 = (-b - math.sqrt(discriminant)) / (2 * a)

        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return (sr.Intersection(t1, self), sr.Intersection(t2, self))

    def normal_at(self, p: sr.Point) -> sr.Vector:
        p = p.mat_mul(self.transform.inverse())
        object_normal = cast(sr.Vector, p - sr.Point(0, 0, 0)).normalize()
        world_normal = object_normal.mat_mul(self.transform.inverse().transpose())
        return world_normal.normalize()
