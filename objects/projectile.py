from objects.falling_object import FallingObject


class Projectile(FallingObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dmg = kwargs.pop("damage_amount", 0)
        self.throwing_count = kwargs.pop("throwing_count", 1)
        self.thrown = False
        self.owner = kwargs.pop("owner")  # Un living object, pour indiquer à qui le projectile appartient

        self.init_xvel = self.velocity[0]
        self.init_yvel = self.velocity[1]

    def update(self, delta):
        if self.thrown:
            super().update(delta)

            if self.is_on_ground():
                self.thrown = False

    def fall(self, gravity, delta):
        if self.thrown:
            super().fall(gravity, delta)

    def collides_with(self, obj):
        if not self.thrown:
            return False
        return super().collides_with(obj)

    def draw(self, window, cam):
        if self.thrown:
            super().draw(window, cam)

    def hurt(self, player):
        self.thrown = False
        player.damage(self.dmg)

    def damage(self):
        return self.dmg

    def throw(self):
        if self.throwing_count == 0:
            return
        self.rect.x = self.owner.collision_rect.x + (self.owner.collision_rect.w if self.owner.facing_side == 1 else 0)
        self.rect.y = self.owner.collision_rect.y + self.owner.collision_rect.h / 2

        self.velocity = [self.init_xvel * (-1 if self.owner.facing_side == 0 else 1), self.init_yvel]

        self.thrown = True

    def reload(self):
        print("munition +1 !")
        self.throwing_count += 1
