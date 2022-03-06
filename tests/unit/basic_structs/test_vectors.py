from praytracer import Vector, Point


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
