from resources import manager
from scenes.base_scene import BaseScene


class FPSScene(BaseScene):
    def __init__(self, window):
        super().__init__(window)
        self.font = manager.get_font("main.ttf", 28)
        self.text = self.font.render("FPS : 0", True, (255, 255, 255))

    def on_start(self):
        pass

    def on_update(self, delta):
        self.text = self.font.render("FPS : {0:.1f}".format(1000 / delta), True, (255, 255, 255))

    def on_draw(self):
        self.clear()
        self.window.blit(self.text, (10, 10))
        self.display()

    def on_events(self, e):
        pass
