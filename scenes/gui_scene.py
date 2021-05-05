from pygame.locals import *

from gui.button import Button
from gui.label import Label
from gui.progressbar import ProgressBar
from scenes.base_scene import BaseScene


class GuiScene(BaseScene):
    def __init__(self, window):
        super().__init__(window)

        self.btn = Button(string="Clique ici pour voir")
        self.prog = ProgressBar()
        self.lbl = Label()

    def on_update(self, delta):
        self.btn.handler(self)
        self.btn.set_on_click_listener(self.on_button_clicked)

        self.prog.set_progress(self.prog.get_progress() + 0.002 * delta)

    def on_button_clicked(self):
        self.lbl.set_text("Moi aussi j'aime les nouilles.")
        self.btn.set_text("Ben maintenant tu peux plus mdr lol")
        self.btn.set_enabled(False)

    def on_draw(self):
        self.clear()
        self.btn.draw(self.window)
        self.prog.draw(self.window)
        self.lbl.draw(self.window)
        self.display()

    def on_events(self, ev_list):
        for e in ev_list:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.quit()
                if e.key == K_0:
                    self.btn.set_enabled(False)
