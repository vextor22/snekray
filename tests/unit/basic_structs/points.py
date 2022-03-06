from praytracer import Point


def declare_point(x, y, z):
    return Point(x, y, z)


def test_point():
    t = (4.1, 5.6, -2.1)
    x, y, z = t

    p = declare_point(4.1, 5.6, -2.1)
    assert x == p.x
    assert y == p.y
    assert z == p.z

    assert type(p) == Point.__name__
