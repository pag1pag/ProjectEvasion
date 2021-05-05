from objects.living_object import LivingObject


class Bot(LivingObject):
    """Classe permettant de définir les comportements des bots"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.radius = kwargs.pop("radius", 0)
        self.x1 = kwargs.pop("x1", 0)
        self.x2 = kwargs.pop("x2", 0)
        self.y1 = kwargs.pop("y1", 0)
        self.y2 = kwargs.pop("y2", 0)
        self.jump = kwargs.pop("jump", 0)

    def shooting(self, radius):
        pass

    def parkour_1(self):
        pass

# Dans cette partie du code on va définir les movements du bot
