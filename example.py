from time import sleep
from dotenv import load_dotenv
import math

load_dotenv(override=True)
import os

print(os.environ.get("PYTHONPATH", "none"))

from snekray import SnekRay, Point, Vector, Color, Canvas
from snekray.environment import Environment, Projectile

tracer = SnekRay()

print(f"Render at: {tracer.get_dimensions()}")


# Example Projectile


projectile = Projectile(direction=Vector(1, 1.8, 0).normalize(), magnitude=11)
env = Environment()
env.register_object(projectile)
projectile_color = Color(1, 0.4, 0.6)
c_y = 550
c_x = 900
canvas = Canvas(c_x, c_y)
while env.tick() > 0:
    x = math.ceil(projectile.position.x)
    y = math.ceil(projectile.position.y)
    try:
        canvas.write_pixel(x, c_y - y - 1, projectile_color)
    except:
        print("Attempting to write: ", x, y, c_x, c_y)
        raise
    if env.tick_count % 50 == 0:
        print(f"Current tick: {env.tick_count}, {projectile}", end="\r")
        sleep(0.5)
    pass


print(f"We got to {projectile.position} at a final tick of {env.tick_count}")

with open("output.ppm", "w") as f:
    f.write(canvas.to_ppm())


print("Test time to fill 1024x768 grid")
c1 = Color(1.0, 0.5, 0.5)

canvas = Canvas(1024, 768, fill=c1)
