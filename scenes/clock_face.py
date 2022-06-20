from time import sleep
from dotenv import load_dotenv
import math

load_dotenv(override=True)
import os

print(os.environ.get("PYTHONPATH", "none"))

from snekray import SnekRay, Point, Vector, Color, Canvas, Matrix
from snekray.environment import Environment, Projectile

tracer = SnekRay()
print(f"Render at: {tracer.get_dimensions()}")

p_start = Point(0, 1, 0)

translate = Matrix.translation(150, 150, 0)
scale = Matrix.scaling((3 / 8) * 300, (3 / 8) * 300, 0)
scale_and_translate = translate * scale
canvas = Canvas(300, 300)
for i in range(1, 13):
    rotate = Matrix.rotation_z(i * (math.pi / 6))
    p = p_start.mat_mul(rotate)
    p = p.mat_mul(scale_and_translate)

    canvas.write_pixel(math.ceil(p.x), math.ceil(p.y), Color(1, 1, 1))
    print(f"Printing point: {p}")
    p = p.mat_mul(rotate)
with open("scenes/clock.ppm", "w") as f:
    f.write(canvas.to_ppm())
