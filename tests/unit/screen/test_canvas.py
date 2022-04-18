from snekray import Canvas, Color


def test_create_canvas():
    c = Canvas(10, 20)
    assert c.width == 10
    assert c.height == 20

    assert all(pixel == Color(0, 0, 0) for pixel in c.pixels)


def test_write_to_canvas():
    c = Canvas(10, 20)
    red = Color(1, 0, 0)

    c.write_pixel(2, 3, red)
    assert c.get_pixel(2, 3) == red


def test_export_to_ppm():
    c = Canvas(5, 3)
    ppm = c.to_ppm().split("\n")

    assert "P3" == ppm[0]
    assert "5 3" == ppm[1]
    assert "255" == ppm[2]


def test_ppm_pixel_data():
    c = Canvas(5, 3)

    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)

    c.write_pixel(0, 0, c1)
    c.write_pixel(2, 1, c2)
    c.write_pixel(4, 2, c3)

    ppm = c.to_ppm().split("\n")

    assert "P3" == ppm[0]
    assert "5 3" == ppm[1]
    assert "255" == ppm[2]

    assert "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0" == ppm[3]
    assert "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0" == ppm[4]
    assert "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255" == ppm[5]


def test_ppm_split_long_lines():

    c1 = Color(1, 0.8, 0.6)
    c = Canvas(10, 2, fill=c1)

    ppm = c.to_ppm().split("\n")

    assert "P3" == ppm[0]
    assert "10 2" == ppm[1]
    assert "255" == ppm[2]

    assert (
        "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204" == ppm[3]
    )
    assert "153 255 204 153 255 204 153 255 204 153 255 204 153" == ppm[6]

    assert "\n" == c.to_ppm()[-1]
