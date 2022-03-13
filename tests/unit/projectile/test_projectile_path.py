from snekray.environment import Environment, Projectile
from snekray import Point, Vector


def test_projectile_end():
    projectile = Projectile(direction=Vector(1, 1, 0).normalize(), magnitude=2)
    env = Environment()
    env.register_object(projectile)

    while env.tick() > 0:
        pass

    assert env.tick_count == 31

    assert Point(38.07640687119284, -0.07359312880715763, 0.0) == projectile.position
