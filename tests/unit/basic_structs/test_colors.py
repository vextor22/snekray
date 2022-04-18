from snekray import Color


def test_color_instance():
    c = Color(-0.5, 0.4, 1.7)

    assert c.red == -0.5
    assert c.green == 0.4
    assert c.blue == 1.7


def test_color_addition():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)

    assert c1 + c2 == Color(1.6, 0.7, 1.0)


def test_color_subtraction():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)

    assert c1 - c2 == Color(0.2, 0.5, 0.5)


def test_color_scalar():
    c1 = Color(0.9, 0.6, 0.75)

    assert c1 * 2 == Color(1.8, 1.2, 1.5)


def test_color_hadamard_product():
    c1 = Color(1, 0.2, 0.4)
    c2 = Color(0.9, 1, 00.1)

    assert c1.hadamard(c2) == Color(0.9, 0.2, 0.04)
