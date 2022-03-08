from snekray import SnekRay


def snek_instance(*args):
    return SnekRay(*args)


def test_dimensions():
    dimensions = SnekRay.get_default_dimensions()
    assert snek_instance().get_dimensions()[0] == dimensions[0]
    assert snek_instance().get_dimensions()[1] == dimensions[1]
