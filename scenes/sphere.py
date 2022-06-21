import snekray as sr


canvas = sr.Canvas(300, 300)
s = sr.Sphere()
s.transform = sr.Matrix.translation(150, 150, 100) * sr.Matrix.scaling(120, 120, 120)
c = sr.Color(0.75, 0.2, 0)
origin = sr.Point(150, 150, -30)
for x in range(300):
    print(f"{x}/300 lines")
    for y in range(300):
        r = sr.Ray(origin, (sr.Point(x, y, 0) - origin).normalize())
        if len(s.intersect(r)) > 0:
            canvas.write_pixel(x, y, c)

with open("scenes/sphere.ppm", "w") as f:
    f.write(canvas.to_ppm())
