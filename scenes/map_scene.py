from pygame.constants import K_ESCAPE, KEYDOWN

from objects.camera import Camera
from objects.tilemap import TileMap
from scenes.base_scene import BaseScene


class MapScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)

        self.tilemap = TileMap(self.game, "ens")

        self.cam = Camera(self.game, 7200, 4080)

    def on_start(self):
        self.tilemap.load()

    def on_draw(self):
        self.clear()
        self.tilemap.draw(self.window, self.cam)
        self.display()

    def on_events(self, ev_list):
        for e in ev_list:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.quit()
