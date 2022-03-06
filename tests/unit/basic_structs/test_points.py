from praytracer import Point, Vector


def declare_point(x, y, z):
    return Point(x, y, z)


def test_point():
    t = (4.1, 5.6, -2.1)
    x, y, z = t

    p = declare_point(*t)
    assert x == p.x
    assert y == p.y
    assert z == p.z

    assert type(p) == Point
    assert p.w == Point.W


def test_point_equality():
    t = (4.1, 5.6, -2.1)
    x, y, z = t

    p = declare_point(*t)
    assert x == p.x
    assert y == p.y
    assert z == p.z
    p2 = declare_point(*t)

    assert type(p2) == Point

    assert p2 == p


def test_point_equality():
    t = (4.1, 5.6, -2.1)
    x, y, z = t

    p = declare_point(*t)
    assert x == p.x
    assert y == p.y
    assert z == p.z
    t2 = (4.1, 5.6, -2.0)
    p2 = declare_point(*t2)

    assert type(p2) == Point

    assert p2 != p


def test_point_vector_inequality():
    t = (4.1, 5.6, -2.1)
    x, y, z = t

    p = declare_point(*t)
    assert x == p.x
    assert y == p.y
    assert z == p.z
    vec = Vector(*t)
    assert x == vec.x
    assert y == vec.y
    assert z == vec.z

    assert type(vec) == Vector

    assert vec != p


def test_point_vector_sum():
    t = (4.3, 5.6, -2.1)
    t2 = (3, -1.6, 8.1)
    sum_t = [sum(x) for x in zip(t, t2)]

    x, y, z = t

    p = Point(*t)
    assert x == p.x
    assert y == p.y
    assert z == p.z
    p2 = Point(*t2)
    v = Vector(*t2)

    sum_point = Point(*sum_t)
    assert p + p2 == p
    assert p + v == sum_point
    assert type(sum_point) == Point


def test_point_vector_diff():
    t = (4.3, 5.6, -2.1)
    t2 = (3, -1.6, 8.1)
    diff_t = [p1 - p2 for p1, p2 in zip(t, t2)]

    p = Point(*t)

    p2 = Point(*t2)
    v = Vector(*t2)

    diff_point = Point(*diff_t)
    diff_vector = Vector(*diff_t)

    assert p - p2 == diff_vector
    assert p - v == diff_point
