from snekray import Point, Vector, Ray, Sphere, Intersection


def test_intersection_encapsulates_t_and_object():
    s = Sphere()
    i = Intersection(1.5, s)

    assert i.object == s
    assert i.t == 1.5


def test_aggregating():
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)

    xs = Intersection.sorted(i1, i2)

    assert len(xs) == 2
    assert xs[0].t == 1
    assert xs[1].t == 2


def test_hit_positive_intersections():
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)

    xs = Intersection.sorted(i1, i2)
    assert Intersection.hit(xs) == i1


def test_hit_some_negative_t():
    s = Sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(1, s)

    xs = Intersection.sorted(i1, i2)
    assert Intersection.hit(xs) == i2


def test_hit_all_negative_t():
    s = Sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(-2, s)

    xs = Intersection.sorted(i1, i2)
    assert Intersection.hit(xs) == None


def test_lowest_non_negative_t():
    s = Sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)

    xs = Intersection.sorted(i1, i2, i3, i4)
    assert Intersection.hit(xs) == i4
