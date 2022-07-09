from snekray import Color, Material, Vector, PointLight, Point
import math


def test_material_creation():
    m = Material(Color(1, 1, 1), 0.1, 0.9, 0.9, 200)
    assert m.color == Color(1, 1, 1)
    assert m.diffuse == 0.9
    assert m.ambient == 0.1
    assert m.specular == 0.9
    assert m.shininess == 200


def test_lighting_with_eye_between_light_and_surface():
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, -10), Color(1, 1, 1))

    result = m.lighting(light, position, eyev, normalv)
    assert result == Color(1.9, 1.9, 1.9)


def test_lighting_with_eye_offset_45_deg():
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, math.sqrt(2) / 2, -math.sqrt(2) / 2)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
    result = m.lighting(light, position, eyev, normalv)
    assert result == Color(1.0, 1.0, 1.0)


def test_lighting_with_light_offset():
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 10, -10), Color(1, 1, 1))
    result = m.lighting(light, position, eyev, normalv)
    assert result == Color(0.7364, 0.7364, 0.7364)


def test_lighting_with_light_and_eye_offset():
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, -math.sqrt(2) / 2, -math.sqrt(2) / 2)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 10, -10), Color(1, 1, 1))
    result = m.lighting(light, position, eyev, normalv)
    assert result == Color(1.6364, 1.6364, 1.6364)


def test_with_light_behind_surface():
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, 10), Color(1, 1, 1))
    result = m.lighting(light, position, eyev, normalv)
    assert result == Color(0.1, 0.1, 0.1)
