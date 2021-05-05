from gui.button import Button
from gui.label import Label
from objects.camera import Camera
from objects.sprite import Sprite
from scenes.base_scene import BaseScene


class GameOverScene(BaseScene):
    def __init__(self, game, rip_text=None):
        super().__init__(game)

        self.back = Sprite(0, 0, texture="polytech.png", game=self.game)

        self.rip_text = rip_text or "Recale a l'ecrit, il n'y a plus d'espoir pour l'ENS..."

        self.over_label = Label(0, 100, self.rip_text, font="valeria.ttf",
                                fontsize=48, textcolor=(0, 0, 0, 0))
        self.over_label.center_horizontal(self.game.get_width())

        self.sarcastic_label = Label(0, 200, "Va pas falloir finir là-bas hein ! Allez, on révise !", fontsize=24,
                                     textcolor=(225, 138, 53))
        self.sarcastic_label.center_horizontal(self.game.get_width())

        self.retry_button = Button(0, 630, "Se réinscrire aux concours", game=self.game, fontsize=48,
                                   textcolor_hover=(162, 58, 244), background_color=(0, 0, 0, 0),
                                   textcolor=(255, 255, 255))

        self.retry_button.center_horizontal()
        self.retry_button.set_on_click_listener(self.on_retry_button_clicked)

        self.cam = Camera(self.game, self.game.get_width(), self.game.get_height())

    def on_draw(self):
        self.clear()
        self.back.draw(self.window, self.cam)
        self.over_label.draw(self.window)
        self.sarcastic_label.draw(self.window)
        self.retry_button.draw(self.window)
        self.display()

    def on_update(self, delta):
        self.retry_button.handler(self)

    def on_events(self, ev_list):
        for e in ev_list:
            pass

    def on_retry_button_clicked(self, sender):
        self.quit()
