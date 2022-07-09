import math
from snekray import Vector, Point


def declare_vector(x, y, z):
    return Vector(x, y, z)


def test_vector():
    t = (4.1, 5.6, -2.1)
    x, y, z = t

    v = declare_vector(*t)
    assert x == v.x
    assert y == v.y
    assert z == v.z

    assert type(v) == Vector

    assert v.w == Vector.W


def test_vector_equality():
    t = (4.1, 5.6, -2.1)
    x, y, z = t

    p = Vector(*t)
    assert x == p.x
    assert y == p.y
    assert z == p.z
    p2 = Vector(*t)

    assert type(p2) == Vector

    assert p2 == p


def test_vector_inequality():
    t = (4.1, 5.6, -2.1)
    x, y, z = t

    p = Vector(*t)
    assert x == p.x
    assert y == p.y
    assert z == p.z

    t = (4.1, 5.6, -2.0)
    p2 = Vector(*t)

    assert type(p2) == Vector

    assert p2 != p


def test_vector_sum():
    t = (4.3, 5.6, -2.1)
    t2 = (3, -1.6, 8.1)
    sum_t = (sum(x) for x in zip(t, t2))

    x, y, z = t

    p = Vector(*t)
    assert x == p.x
    assert y == p.y
    assert z == p.z
    p2 = Vector(*t2)

    sum_vector = Vector(*sum_t)

    assert p + p2 == sum_vector


def test_vector_negation():
    t = (4.3, 5.6, -2.1)
    neg_t = [-x for x in t]

    v = Vector(*t)
    neg_v = Vector(*neg_t)
    assert -v == neg_v


def test_vector_magnitude():
    v1 = Vector(0, 0, 1)
    v2 = Vector(0, 1, 0)
    v3 = Vector(1, 0, 0)
    v4 = Vector(1, 2, 3)
    v5 = Vector(-1, -2, -3)

    assert v1.magnitude() == 1
    assert v2.magnitude() == 1
    assert v3.magnitude() == 1
    assert v4.magnitude() == math.sqrt(14)
    assert v5.magnitude() == math.sqrt(14)
    assert v4.magnitude() == (-v4).magnitude()
    assert v1.magnitude() == (-v1).magnitude()


def test_vector_normalize_identities():
    v1 = Vector(4, 0, 0)
    v2 = Vector(0, 4, 0)
    v3 = Vector(0, 0, 4)
    unit1 = Vector(1, 0, 0)
    unit2 = Vector(0, 1, 0)
    unit3 = Vector(0, 0, 1)
    assert v1.normalize() == unit1
    assert v2.normalize() == unit2
    assert v3.normalize() == unit3


def test_vector_normalize_magnitude():

    v = Vector(1, 2, 3)
    assert v.normalize().magnitude() == 1


def test_vector_normalize_constant():

    v = Vector(1, 2, 3)
    assert v.normalize() == Vector(
        1 / math.sqrt(14), 2 / math.sqrt(14), 3 / math.sqrt(14)
    )


def test_vector_dot_product():
    v1 = Vector(1, 2, 3)
    v2 = Vector(2, 3, 4)

    assert v1.dot(v2) == 20


def test_vector_cross_product():
    v1 = Vector(1, 2, 3)
    v2 = Vector(2, 3, 4)
    assert v1.cross(v2) == Vector(-1, 2, -1)
    assert v2.cross(v1) == Vector(1, -2, 1)


def test_reflecting_vector_45_degrees():
    v = Vector(1, -1, 0)
    n = Vector(0, 1, 0)

    r = v.reflect(n)
    r = Vector(1, 1, 0)


def test_reflecting_vector_slanted():
    v = Vector(0, -1, 0)
    n = Vector(math.sqrt(2) / 2, math.sqrt(2) / 2, 0)

    r = v.reflect(n)
    r = Vector(1, 0, 0)
