from pygame.locals import *

from objects.living_object import LivingObject
# from sounds.musique_classe import *
from scenes.base_scene import BaseScene


class AIScene(BaseScene):
    def __init__(self, window):
        super().__init__(window)
        self.gravity = 0.001
        self.x = 0
        self.y = 0
        self.bot = LivingObject(0, 400, texture="Evariste_galois.jpg")
        self.ulm = LivingObject(0, 0, texture="ulm.PNG")
        self.left_movement = False
        self.right_movement = False
        # self.snd = Sound("gun.wav")

    def on_update(self, delta):
        self.bot.fall(self.gravity, delta)
        self.bot.update(delta)

        if self.bot.get_position()[0] < self.x:
            print(0)
            self.bot.move_right()

        if self.bot.get_position()[0] > self.x:
            print(1)
            self.bot.move_left()

        if self.x + 2 > self.bot.get_position()[0] > self.x - 2:
            print(2)
            self.bot.stop()

    def on_draw(self):
        self.clear()
        self.ulm.draw(self.window)
        self.bot.draw(self.window)
        self.display()

    def on_events(self, ev_list):
        for e in ev_list:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.quit()

            if e.type == MOUSEBUTTONDOWN:
                self.x = self.snap.get_mouse_position()[0]
                self.y = self.snap.get_mouse_position()[1]
                print(self.x, self.y, self.bot.get_position()[0], self.bot.get_position()[1])
