from objects.falling_object import FallingObject

""" A rajouter dans Gravity_scene.py, dans 'on_update'
self.coeur = Heal(400, 0, texture="coeur.png", heal_points=30)


if self.coeur.collides_with(self.player1):
    self.coeur.heal(self.player1)
    #del self.coeur
"""


class Heal(FallingObject):
    """Create a heal object, allowing the player to recover some life points"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heal_point = kwargs.pop("heal_points", 0)
        self.pop = True

    def make_pop(self):
        self.pop = True
        self.coords[0] = 300
        self.coords[1] = 300

    def draw(self, window, cam):
        """affiche le coeur"""
        if self.pop:
            super().draw(window, cam)

    def collides_with(self, obj):
        """verifie si le coeur est touché par le joueur"""
        if not self.pop:
            return False
        return super().collides_with(obj)

    def heal(self, player):
        self.pop = False
        player.cure(self.heal_point)

    def fall(self, gravity, delta):
        if self.pop:
            super().fall(gravity, delta)

