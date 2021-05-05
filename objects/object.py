from objects.sprite import Sprite


class Object(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def collides_with(self, obj):
        """AABB Collision management.
        """
        if not obj.collidable():
            return False
        obj_pos = obj.get_position()
        x = self.rect.x
        y = self.rect.y
        w = self.get_size()[0]
        h = self.get_size()[1]

        x2 = obj_pos[0]
        y2 = obj_pos[1]
        w2 = obj.get_size()[0]
        h2 = obj.get_size()[1]

        return not (x2 >= x + w or x2 + w2 <= x or y2 >= y + h or y2 + h2 <= y)

    def collidable(self):
        return True
