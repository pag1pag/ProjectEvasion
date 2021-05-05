import pygame
from pygame.locals import *

from events.input import Input
from scenes.base_scene import BaseScene


class BallScene(BaseScene):
    def __init__(self, window):
        super().__init__(window)
        self.background = pygame.image.load("img/Evariste_galois.jpg")
        self.coords = [0, 0]
        self.input = Input()

    def on_start(self):
        pass

    def on_draw(self):
        self.clear()
        self.window.blit(self.background, self.coords)
        self.display()

    def on_update(self, delta):
        if not self.input.again():
            self.close()

        if self.input.is_key_pressed(K_ESCAPE):
            self.quit()

        if self.input.is_key_pressed(K_RIGHT):
            if self.coords[0] < 640 - 220:
                self.coords[0] += 0.1 * delta

        if self.input.is_key_pressed(K_LEFT):
            if self.coords[0] > 0:
                self.coords[0] -= 0.1 * delta

        if self.input.is_key_pressed(K_UP):
            if self.coords[1] > 0:
                self.coords[1] -= 0.1 * delta

        if self.input.is_key_pressed(K_DOWN):
            if self.coords[1] < 480 - 284:
                self.coords[1] += 0.1 * delta

    def on_events(self, ev_list):
        self.input.update(ev_list)

