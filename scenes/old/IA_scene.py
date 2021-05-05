import pygame
from pygame.locals import *

from events.input import Input
from scenes.base_scene import BaseScene


# from scenes.deplacementIA import move

class IAScene(BaseScene):
    " pour gérer l'IA des adversaires"

    def __init__(self, window):
        super().__init__(window)
        self.background = pygame.image.load("img/Evariste_galois.jpg")
        self.coords = [0, 480 - 284]
        self.input = Input()
        self.x = 0
        self.y = 0
        self.begin = True
        self.end = False
        self.trig = False
        self.position = False
        self.cycle = True
        self.epsilon = 1

    def on_start(self):
        pass

    def on_draw(self):
        self.clear()
        self.window.blit(self.background, self.coords)
        self.display()

    def on_update(self, delta):

        # position = False
        # trigger = False
        # cycle = True
        # start = True
        # end = False
        if not self.snap.again():
            self.close()

        if self.snap.is_key_pressed(K_ESCAPE):
            self.quit()

        if self.trig == False and self.position == False and self.cycle == True:
            self.deplacement_cycle(delta)
            print('cycle [x={}]'.format(self.coords[0]))

        if self.is_mouse_clicked(1):
            self.x = self.snap.get_mouse_position()[0]
            self.y = self.snap.get_mouse_position()[1]
            self.trig = True
            self.cycle = False
            print('trigger')

        if self.trig == True and self.coords[0] != self.x and self.coords[1] != self.y:
            self.deplacement(delta)
            print('pos[x={}, y={}]'.format(self.coords[0], self.coords[1]))

        if self.trig == True and abs(self.coords[0] - self.x) <= self.epsilon and abs(
                self.coords[1] - self.y) <= self.epsilon:
            self.trig = False
            self.position = True
            print('position')

        if self.trig == False and self.position == True:  # and x != 0 and y != 480-284:
            self.replacement(delta)
            print('retour')

        if self.trig == False and self.position == True and self.x == 0 and self.y == 480 - 284:
            self.position = False
            self.cycle = True
            print('retour2')

    def deplacement_cycle(self, delta):

        c_image = self.background.get_size()[0]
        if self.begin == True and self.end == False:
            # self.x = 640-220
            if self.coords[0] < 640 - c_image:
                self.coords[0] += 0.1 * delta
            # self.begin = False

        if abs(self.x - 640 + c_image) < self.epsilon and self.begin == True and self.end == False:
            self.end = True
            self.begin = False

        if self.begin == False and self.end == True:
            # self.x = 0
            # self.end = False
            if self.coords[0] > 0:
                self.coords[0] += 0.1 * delta

        if self.x < self.epsilon and self.begin == False and self.end == False:
            self.begin = True
            self.end = False
        # if self.coords[0] < self.x:
        # self.coords[0] += 0.1 * delta

    #
    # if self.coords[0] > self.x:
    # self.coords[0] -= 0.1 * delta

    # if self.coords[1] > self.y:
    # self.coords[1] -= 0.1 * delta
    #
    # if self.coords[1] < self.y:
    # self.coords[1] += 0.1 * delta

    def deplacement(self, delta):

        if self.coords[0] < self.x:
            self.coords[0] += 0.1 * delta

        if self.coords[0] > self.x:
            self.coords[0] -= 0.1 * delta

        if self.coords[1] > self.y:
            self.coords[1] -= 0.1 * delta

        if self.coords[1] < self.y:
            self.coords[1] += 0.1 * delta

    def replacement(self, delta):

        if self.coords[0] < 0:
            self.coords[0] += 0.1 * delta

        if self.coords[0] > 0:
            self.coords[0] -= 0.1 * delta

        if self.coords[1] > 480 - 284:
            self.coords[1] -= 0.1 * delta

        if self.coords[1] < 480 - 284:
            self.coords[1] += 0.1 * delta
