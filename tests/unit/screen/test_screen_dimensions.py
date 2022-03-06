from praytracer import PRay


def pray_instance(*args):
    return PRay(*args)


def test_dimensions():
    dimensions = PRay.get_default_dimensions()
    assert pray_instance().get_dimensions()[0] == dimensions[0]
    assert pray_instance().get_dimensions()[1] == dimensions[1]
