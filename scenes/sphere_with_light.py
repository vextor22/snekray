import snekray as sr
from typing import cast


def render():
    canvas = sr.Canvas(300, 300)
    m = sr.Material(sr.Color(1, 0, 0.3))
    s = sr.Sphere(material=m)
    light = sr.PointLight(sr.Point(-8, 8, -10), sr.Color(1, 1, 1))
    s.transform = (
        sr.Matrix.translation(150, 150, 125)
        * sr.Matrix.shearing(1, 0, 0, 1, 0, 0)
        * sr.Matrix.scaling(110, 110, 110)
    )
    c = sr.Color(0.75, 0.2, 0)
    origin = sr.Point(150, 150, -400)
    for x in range(300):
        print(f"{x}/300 lines")
        for y in range(300):
            r = sr.Ray(
                origin, cast(sr.Vector, (sr.Point(x, y, 0) - origin)).normalize()
            )
            hits = s.intersect(r)
            if len(hits) > 0:
                hit = hits[0]
                point = r.position(hit.t)
                normal = hit.object.normal_at(point)
                eye = r.direction * -1
                c = s.material.lighting(light, point, eye, normal)

                canvas.write_pixel(x, y, c)

    with open("scenes/sphere_with_light.ppm", "w") as f:
        f.write(canvas.to_ppm())


render()
