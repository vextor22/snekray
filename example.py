from time import sleep
from dotenv import load_dotenv

load_dotenv(override=True)

import os

print(os.environ.get("PYTHONPATH", "none"))
from snekray import SnekRay, Point, Vector
from snekray.environment import Environment, Projectile

tracer = SnekRay()

print(f"Render at: {tracer.get_dimensions()}")


# Example Projectile


projectile = Projectile(direction=Vector(1, 1, 0).normalize(), magnitude=2)
env = Environment()
env.register_object(projectile)

while env.tick() > 0:
    if env.tick_count % 50 == 0:
        print(f"Current tick: {env.tick_count}, {projectile}", end="\r")
        sleep(0.5)
    pass

print(f"We got to {projectile.position} at a final tick of {env.tick_count}")
