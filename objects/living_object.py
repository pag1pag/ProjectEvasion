import math

from pygame.rect import Rect

from objects.falling_object import FallingObject
from objects.projectile import Projectile


class LivingObject(FallingObject):
    def __init__(self, *args, **kwargs):
        """This class handles a living entity, such as a mob and the player.
        It uses two different rectangles, one for the graphics, one for the physics.
        It is particularly useful when the frame of the animation is much larger than the character in it.

        -------------------
        |                 |
        |   -----------   |
        |   | Physical|   |  <-- Graphic frame (rect)
        |   |  frame  |   |
        |   -----------   |
        |                 |
        -------------------

        The physics rect is expressed as a Rect, denoting margins between the graphics rect.
        This means that coordinates of the physics rect is expressed in the base of the graphics rect.
        """
        super().__init__(*args, **kwargs)
        self.vcharg_state = False
        self.vcharg = 0

        self.projectiles = [Projectile(0, 0, velocity=[0.3, -0.3], game=self.game, texture="chalk_small.png",
                                       animated=True, animation_width=10, animation_height=10,
                                       looping=True, update_rate=300, owner=self)]

        self.health = kwargs.pop("health", 100)
        self.dead = False

        self.physics_rect = kwargs.pop("collision_rect", Rect(0, 0, self.rect.width, self.rect.height))

        self.collision_rect = self.get_collision_rect()

        self.on_ground = False
        self.sprint = False

        self.facing_side = 1

    def get_collision_rect(self):
        return Rect(self.rect.left + self.physics_rect.left, self.rect.top + self.physics_rect.top,
                    self.physics_rect.width, self.physics_rect.height)

    def update_collision_rect(self):
        self.collision_rect = self.get_collision_rect()

    def jump(self):
        if self.on_ground:
            self.velocity[1] = -0.5
            self.on_ground = False

    def ground_pound(self):
        self.velocity[1] = 1.5

    def reload(self):
        pass

    def update(self, delta):
        super().update(delta)

        for p in self.projectiles:
            p.update(delta)

        if self.vcharg_state and self.vcharg <= 0.8:
            self.vcharg += 0.8 - math.exp(-0.015 * delta)

        previous = self.last_position()

        if self.velocity[0] < 0 and previous.x + self.physics_rect.x < 0:
            self.stop()
            self.rect.x = previous.x

        if self.velocity[0] > 0 and previous.x + previous.w > 7200:
            self.stop()
            self.rect.x = previous.x

        if self.velocity[1] < 0 and previous.y < 0:
            self.velocity[1] = 0
            self.rect.y = previous.y

        self.update_collision_rect()

    def draw(self, window, cam):
        if not self.dead:
            super().draw(window, cam)
        for p in self.projectiles:
            p.draw(window, cam)

    def collides_with(self, obj):
        if self.dead:
            return False
        if not super().collides_with(obj):
            return False
        return obj.rect.colliderect(self.collision_rect)

    def fall(self, gravity, delta):
        if not self.dead:
            super().fall(gravity, delta)
        for p in self.projectiles:
            p.fall(gravity, delta)

    def release_charged_jump(self):
        self.velocity[1] = -self.vcharg
        self.vcharg = 0
        self.vcharg_state = False

    def begin_charged_jump(self):
        self.vcharg_state = True

    def move_left(self):
        self.velocity[0] = -0.15 if not self.sprint else -0.5
        self.facing_side = 0

    def move_right(self):
        self.velocity[0] = 0.15 if not self.sprint else 0.5
        self.facing_side = 1

    def stop(self):
        self.velocity[0] = 0

    def damage(self, damage_amount):
        self.health = max(self.health - damage_amount, 0)
        if self.health == 0:
            print("Dead")
            self.dead = True

    def snipe(self):
        self.projectiles[0].throw()

    def cure(self, heal_amount):
        self.health = max(min(self.health + heal_amount, 100), 0)

    def handle_collisions(self, map):
        for t in map.map.values():
            if self.collides_with(t):
                last_rect = self.last_position()

                if self.velocity[1] > 0 and last_rect.y + last_rect.h - self.physics_rect.y < t.rect.y:
                    self.velocity[1] = 0
                    self.rect.y = t.rect.y - (self.physics_rect.y + self.physics_rect.h)
                    self.on_ground = True
                if self.velocity[1] < 0 and last_rect.y + self.physics_rect.y > t.rect.y + t.rect.h:
                    self.velocity[1] = 0
                    self.rect.y = t.rect.y + t.rect.height - self.physics_rect.y

                if self.velocity[0] > 0:
                    self.stop()
                    self.rect.x = last_rect.x
                if self.velocity[0] < 0:
                    self.stop()
                    self.rect.x = last_rect.x

    def has_fallen_offstage(self, cam):
        return self.rect.y > cam.state.height

    def resurrect(self):
        self.cure(100)
        self.dead = False

    def run_fast(self, sprint):
        self.sprint = sprint
