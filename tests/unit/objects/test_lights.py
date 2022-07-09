from snekray import PointLight, Point, Color


def test_light_creation():
    intensity = Color(1, 1, 1)
    position = Point(0, 0, 0)

    light = PointLight(position, intensity)

    assert light.position == position
    assert light.intensity == intensity
