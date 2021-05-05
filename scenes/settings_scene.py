from pygame.constants import K_ESCAPE, KEYDOWN

from gui.checkbox import Checkbox
from gui.label import Label
from gui.slider import Slider
from objects.camera import Camera
from objects.sprite import Sprite
from scenes.base_scene import BaseScene


class SettingsScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)

        self.back = Sprite(0, 0, texture='poly.jpg', game=self.game)

        self.camera = Camera(self.game, self.game.get_width(), self.game.get_height())

        self.settings_lbl = Label(0, 50, "Options", font='valeria.ttf', fontsize=64, textcolor=(255, 255, 255),
                                  game=self.game)
        self.settings_lbl.center_horizontal(self.game.get_width())

        self.slider = Slider(100, 300, initial_position=50)
        self.slider.PositionChanged.attach(self.position_updated)

        self.slider_lbl = Label(100, 350, "Progress : 50 %", game=self.game)

        self.check = Checkbox(100, 500, "Off")

    def position_updated(self, *args, **kwargs):
        pos = kwargs.pop("position")
        self.slider_lbl.set_text("Progress : {} %".format(pos))

    def on_update(self, delta):
        self.slider.handler(self)
        self.check.handler(self)

    def on_draw(self):
        self.clear()
        # self.back.draw(self.window, self.camera)
        self.settings_lbl.draw(self.window)
        self.slider.draw(self.window)
        self.slider_lbl.draw(self.window)
        self.check.draw(self.window)
        self.display()

    def on_events(self, ev_list):
        for e in ev_list:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.quit()

