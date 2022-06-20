from snekray import Point, Matrix, Vector
import math


def test_multiple_by_translation():
    tmatrix = Matrix.translation(5, -3, 2)
    p = Point(-3, 4, 5)

    t_p = p.mat_mul(tmatrix)
    assert t_p == Point(2, 1, 7)


def test_multiple_by_translation_inverse():
    tmatrix = Matrix.translation(5, -3, 2)
    i_tmatrix = tmatrix.inverse()
    p = Point(-3, 4, 5)

    t_p = p.mat_mul(i_tmatrix)
    assert t_p == Point(-8, 7, 3)


def test_vector_translation():
    tmatrix = Matrix.translation(5, -3, 2)
    v = Vector(-3, 4, 5)

    assert v == v.mat_mul(tmatrix)


def test_point_scaling():
    smatrix = Matrix.scaling(2, 3, 4)
    p = Point(-4, 6, 8)

    assert p.mat_mul(smatrix) == Point(-8, 18, 32)


def test_vector_scaling():
    smatrix = Matrix.scaling(2, 3, 4)
    v = Vector(-4, 6, 8)

    assert v.mat_mul(smatrix) == Vector(-8, 18, 32)


def test_vector_scaling_inverse():
    smatrix = Matrix.scaling(2, 3, 4)
    v = Vector(-4, 6, 8)

    assert v.mat_mul(smatrix.inverse()) == Vector(-2, 2, 2)


def test_reflection_by_negative_scalar():
    smatrix = Matrix.scaling(-1, 1, 1)
    v = Vector(-4, 6, 8)

    assert v.mat_mul(smatrix) == Vector(4, 6, 8)


def test_rotation_x():
    p = Point(0, 1, 0)
    hq = Matrix.rotation_x(math.pi / 4)
    fq = Matrix.rotation_x(math.pi / 2)

    assert p.mat_mul(hq) == Point(0, math.sqrt(2) / 2, math.sqrt(2) / 2)
    assert p.mat_mul(fq) == Point(0.0, 0.0, 1.0)


def test_rotation_y():
    p = Point(0, 0, 1)
    hq = Matrix.rotation_y(math.pi / 4)
    fq = Matrix.rotation_y(math.pi / 2)

    assert p.mat_mul(hq) == Point(math.sqrt(2) / 2, 0, math.sqrt(2) / 2)
    assert p.mat_mul(fq) == Point(1, 0, 0)


def test_rotation_z():
    p = Point(0, 1, 0)
    hq = Matrix.rotation_z(math.pi / 4)
    fq = Matrix.rotation_z(math.pi / 2)

    assert p.mat_mul(hq) == Point(-math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
    assert p.mat_mul(fq) == Point(-1, 0, 0)


def test_shear_x_y():
    shear = Matrix.shearing(1, 0, 0, 0, 0, 0)
    p = Point(2, 3, 4)

    assert p.mat_mul(shear) == Point(5, 3, 4)


def test_shear_x_z():
    shear = Matrix.shearing(0, 1, 0, 0, 0, 0)
    p = Point(2, 3, 4)

    assert p.mat_mul(shear) == Point(6, 3, 4)


def test_shear_y_x():
    shear = Matrix.shearing(0, 0, 1, 0, 0, 0)
    p = Point(2, 3, 4)

    assert p.mat_mul(shear) == Point(2, 5, 4)


def test_shear_y_z():
    shear = Matrix.shearing(0, 0, 0, 1, 0, 0)
    p = Point(2, 3, 4)

    assert p.mat_mul(shear) == Point(2, 7, 4)


def test_shear_z_x():
    shear = Matrix.shearing(0, 0, 0, 0, 1, 0)
    p = Point(2, 3, 4)

    assert p.mat_mul(shear) == Point(2, 3, 6)


def test_shear_z_y():
    shear = Matrix.shearing(0, 0, 0, 0, 0, 1)
    p = Point(2, 3, 4)

    assert p.mat_mul(shear) == Point(2, 3, 7)


def test_transforms_in_sequence():
    p = Point(1, 0, 1)
    rotate = Matrix.rotation_x(math.pi / 2)
    scale = Matrix.scaling(5, 5, 5)
    translate = Matrix.translation(10, 5, 7)
    p2 = p.mat_mul(rotate)
    assert p2 == Point(1, -1, 0)

    p3 = p2.mat_mul(scale)
    assert p3 == Point(5, -5, 0)

    p4 = p3.mat_mul(translate)
    assert p4 == Point(15, 0, 7)


def test_chained_transforms():
    p = Point(1, 0, 1)
    rotate = Matrix.rotation_x(math.pi / 2)
    scale = Matrix.scaling(5, 5, 5)
    translate = Matrix.translation(10, 5, 7)

    scrombler = translate * scale * rotate

    assert p.mat_mul(scrombler) == Point(15, 0, 7)
