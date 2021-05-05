from pygame.constants import K_ESCAPE, KEYDOWN

from gui.button import Button
from gui.label import Label
from objects.camera import Camera
from objects.sprite import Sprite
from scenes.base_scene import BaseScene
from scenes.game_scene import GameScene
from scenes.settings_scene import SettingsScene

QUOTE = ["Je rêve d'un jour où l'égoïsme ne régnera plus dans les sciences, où on s'associera pour étudier, ",
         "au lieu d'envoyer aux académiciens des plis cachetés, on s'empressera de publier",
         "ses moindres observations pour peu qu'elles soient nouvelles, et on ajoutera \"je ne sais pas le reste\"."]


class MainScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)

        self.background = Sprite(0, 0, game=self.game, texture="ulm.png")

        self.quote_labels = [Label(0, 200, QUOTE[0], font='hotel_de_paris.ttf', fontsize=24, textcolor=(0, 255, 255)),
                             Label(0, 230, QUOTE[1], font='hotel_de_paris.ttf', fontsize=24, textcolor=(0, 255, 255)),
                             Label(0, 260, QUOTE[2], font='hotel_de_paris.ttf', fontsize=24, textcolor=(0, 255, 255))]
        self.eva_lbl = Button(1050, 300, "Evariste Galois", font='valeria.ttf', fontsize=24, textcolor=(255, 255, 255),
                              game=self.game)

        # self.background_music = self.game.create_music("Philosophie")

        for lbl in self.quote_labels:
            lbl.center_horizontal(self.game.get_width())

        self.title_lbl = Label(0, 50, "Projet::Evasion", font='valeria.ttf', fontsize=144, textcolor=(0, 0, 0, 0))

        self.play_btn = Button(0, 400, "Play", fontsize=32, textcolor_hover=(162, 58, 244),
                               background_color=(0, 0, 0, 0), textcolor=(255, 255, 255), game=self.game)

        self.options_btn = Button(0, 490, "Options", fontsize=32, textcolor_hover=(162, 58, 244),
                                  background_color=(0, 0, 0, 0), textcolor=(255, 255, 255), game=self.game)

        self.close_btn = Button(0, 580, "Close game", fontsize=32, textcolor_hover=(162, 58, 244),
                                background_color=(0, 0, 0, 0), textcolor=(255, 255, 255), game=self.game)

        self.play_btn.center_horizontal()
        self.options_btn.center_horizontal()
        self.title_lbl.center_horizontal(self.game.get_width())
        self.close_btn.center_horizontal()

        self.cam = Camera(self.game, self.game.get_width(), self.game.get_height())

        self.close_btn.set_on_click_listener(self.on_close_btn_clicked)
        self.play_btn.set_on_click_listener(self.on_play_btn_clicked)
        self.options_btn.set_on_click_listener(self.on_options_btn_clicked)
        self.eva_lbl.set_on_click_listener(self.on_secret_found)

    def on_start(self):
        # self.background_music.play()
        pass

    def quit(self):
        # self.background_music.stop()
        super().quit()

    def on_draw(self):
        self.clear()
        self.background.draw(self.window, self.cam)
        self.title_lbl.draw(self.window)
        for lbl in self.quote_labels:
            lbl.draw(self.window)
        self.eva_lbl.draw(self.window)
        self.play_btn.draw(self.window)
        self.options_btn.draw(self.window)
        self.close_btn.draw(self.window)
        self.display()

    def on_update(self, delta):
        self.play_btn.handler(self)
        self.close_btn.handler(self)
        self.options_btn.handler(self)
        self.eva_lbl.handler(self)

    def on_close_btn_clicked(self, sender):
        self.quit()

    def on_play_btn_clicked(self, sender):
        # self.background_music.stop()
        game_scene = GameScene(self.game)

        game_scene.start()

    def on_options_btn_clicked(self, sender):
        options_scene = SettingsScene(self.game)

        options_scene.start()

    def on_secret_found(self, sender):
        print("Vous avez trouvé le secret ! :^)")

    def on_events(self, ev_list):
        for e in ev_list:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.quit()
