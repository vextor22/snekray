import math
from snekray import Point, Vector, Ray, Sphere, Matrix
from snekray.objects.intersection import Intersection


def test_sphere_intersection():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()

    xs = s.intersect(r)

    assert len(xs) == 2
    assert xs[0].t == 4.0
    assert xs[1].t == 6.0


def test_sphere_intersection_at_tangent():
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = Sphere()

    xs = s.intersect(r)

    assert len(xs) == 2
    assert xs[0].t == 5.0
    assert xs[1].t == 5.0


def test_ray_misses_sphere():
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
    s = Sphere()

    xs = s.intersect(r)

    assert len(xs) == 0


def test_ray_origin_in_sphere():
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    s = Sphere()

    xs = s.intersect(r)

    assert len(xs) == 2
    assert xs[0].t == -1.0
    assert xs[1].t == 1.0


def test_sphere_behind_ray():
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = Sphere()

    xs = s.intersect(r)

    assert len(xs) == 2
    assert xs[0].t == -6.0
    assert xs[1].t == -4.0


def test_intersect_sets_object():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)

    assert len(xs) == 2
    assert xs[0].object == s
    assert xs[1].object == s


def test_sphere_default_transformation():
    s = Sphere()
    assert s.transform == Matrix.identity_matrix()


def test_sphere_transform_assignment():
    s = Sphere()
    t = Matrix.translation(2, 3, 4)
    s.transform = t

    assert s.transform == t


def test_intersect_with_scaled_sphere():
    s = Sphere()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    xs = s.intersect(r)

    assert len(xs) == 2
    assert xs[0].t == 4
    assert xs[1].t == 6
    s.transform = Matrix.scaling(2, 2, 2)
    xs = s.intersect(r)

    assert len(xs) == 2
    assert xs[0].t == 3
    assert xs[1].t == 7


def test_intersect_with_translated_sphere():
    s = Sphere()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    xs = s.intersect(r)

    assert len(xs) == 2
    assert xs[0].t == 4
    assert xs[1].t == 6
    s.transform = Matrix.translation(5, 0, 0)
    xs = s.intersect(r)

    assert len(xs) == 0


def test_intersect_with_translated_scaled_sphere():
    s = Sphere()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    xs = s.intersect(r)

    assert len(xs) == 2
    assert xs[0].t == 4
    assert xs[1].t == 6
    s.transform = Matrix.translation(3, 0, 0) * Matrix.scaling(3, 3, 3)
    xs = s.intersect(r)

    assert len(xs) == 2
    assert math.isclose(xs[0].t, 5.0)
    assert math.isclose(xs[1].t, 5.0)
