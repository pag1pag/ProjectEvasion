from objects.object import Object


class FallingObject(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity = kwargs.pop("velocity", [0, 0])

        self.last_rect = self.rect

        self.dx = 0
        self.dy = 0

    def update(self, delta):
        super().update(delta)

        self.last_rect = self.rect

        self.dx = self.velocity[0] * delta
        self.dy = self.velocity[1] * delta

        self.rect = self.rect.move(self.dx, self.dy)

    def last_position(self):
        return self.rect.move(-self.dx, -self.dy)

    def fall(self, gravity, delta):
        self.velocity[1] += gravity * delta

    def set_velocity(self, vx, vy):
        self.velocity[0] = vx
        self.velocity[1] = vy

    def get_velocity(self):
        return self.velocity[0], self.velocity[1]

    def move(self, dx, dy):
        self.rect.left += dx
        self.rect.top += dy

    def is_on_ground(self):
        return self.rect.y >= self.game.get_height() - self.get_size()[1]
