from pygame.rect import Rect

from objects.living_object import LivingObject


class Player(LivingObject):
    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, texture="professor.png",
                         animation_width=64,
                         animation_height=64,
                         animated=True,
                         looping=True,
                         update_rate=150,
                         collision_rect=Rect(20, 14, 23, 48),
                         projectile_count=5,
                         **kwargs)


