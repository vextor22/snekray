import math
from snekray import Point, Vector, Ray, Sphere, Matrix, Material, Color


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


def test_normal_on_x_axis():
    s = Sphere()
    n = s.normal_at(Point(1, 0, 0))

    assert n == Vector(1, 0, 0)


def test_normal_on_y_axis():
    s = Sphere()
    n = s.normal_at(Point(0, 1, 0))

    assert n == Vector(0, 1, 0)


def test_normal_on_z_axis():
    s = Sphere()
    n = s.normal_at(Point(0, 0, 1))

    assert n == Vector(0, 0, 1)


def test_normal_at_non_axial_point():
    s = Sphere()
    n = s.normal_at(Point(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3))

    assert n == Vector(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3)


def test_normal_is_normalized():
    s = Sphere()
    n = s.normal_at(Point(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3))

    assert n == Vector(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3).normalize()


def test_normal_on_translated_sphere():
    s = Sphere()
    s.transform = Matrix.translation(0.0, 1.0, 0.0)
    n = s.normal_at(Point(0, 1.70711, -0.70711))

    assert n == Vector(0, 0.70711, -0.70711)


def test_normal_on_transformed_sphere():
    s = Sphere()
    s.transform = Matrix.scaling(1, 0.5, 1) * Matrix.rotation_z(math.pi / 5)
    n = s.normal_at(Point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2))

    assert n == Vector(0, 0.97014, -0.24254)


def test_a_sphere_has_default_material():
    s = Sphere()
    m = s.material
    assert m == Material()


def test_a_sphere_can_get_custom_material():
    s = Sphere(Material(Color(1, 2, 3)))
    assert s.material == Material(Color(1, 2, 3))
