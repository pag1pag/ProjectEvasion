from copy import deepcopy

import pygame
from pygame import joystick
from pygame.locals import *

from utils.deprecation import deprecated


@deprecated("Do not use this anymore.")
class Input:
    def __init__(self, *, use_joystick_1=False, number_joystick_1=0,
                 use_joystick_2=False, number_joystick_2=0):
        self.joystick_count = 0
        if use_joystick_1 and joystick.get_count() > number_joystick_1:
            self.joystick_count += 1

        if use_joystick_2 and number_joystick_2 != number_joystick_1 \
                and joystick.get_count() > number_joystick_2:
            self.joystick_count += 1

        if self.joystick_count > 0:
            joystick.init()
            self.joysticks = []

            for i in range(self.joystick_count):
                self.joysticks.append({
                    "joystick": joystick.Joystick(number_joystick_1 if i == 0 else number_joystick_2),
                    "numero": number_joystick_1 if i == 0 else number_joystick_2,
                    "boutons": [],
                    "axes": [],
                    "chapeaux": []
                })

                self.joysticks[i]["boutons"] = [False] * self.joysticks[i]["joystick"].get_numbuttons()
                self.joysticks[i]["axes"] = [0] * self.joysticks[i]["joystick"].get_numaxes()
                self.joysticks[i]["chapeaux"] = [0] * self.joysticks[i]["joystick"].get_numhats()
        else:
            self.joysticks = None

        self.touches_mapped = [False] * K_LAST
        self.sourisX = 0
        self.sourisY = 0
        self.sourisXRel = 0
        self.sourisYRel = 0

        self.boutons_souris = [False] * 8

        self.done = False

    def __del__(self):
        if self.joysticks:
            for joy in self.joysticks:
                joy["joystick"].quit()

            pygame.joystick.quit()

    def update(self, ev_list):
        self.sourisXRel = 0
        self.sourisYRel = 0

        for e in ev_list:
            if e.type == KEYDOWN:
                self.touches_mapped[e.key] = True
            elif e.type == KEYUP:
                self.touches_mapped[e.key] = False
            elif e.type == MOUSEMOTION:
                self.sourisX = e.pos[0]
                self.sourisY = e.pos[1]

                self.sourisXRel = e.rel[0]
                self.sourisYRel = e.rel[1]
            elif e.type == MOUSEBUTTONDOWN:
                self.boutons_souris[e.button] = True
            elif e.type == MOUSEBUTTONUP:
                self.boutons_souris[e.button] = False
            elif e.type == QUIT:
                self.done = True

            if self.joysticks:
                if self.joysticks[0]["numero"] == e.jbutton.which \
                        or self.joysticks[0]["numero"] == e.jaxis.which \
                        or self.joysticks[0]["numero"] == e.jhat.which \
                        or self.joysticks[1]["numero"] == e.jbutton.which \
                        or self.joysticks[1]["numero"] == e.jaxis.which \
                        or self.joysticks[1]["numero"] == e.jhat.which:
                    if e.type == JOYBUTTONDOWN:
                        self.joysticks[e.jbutton.which]["boutons"][e.jbutton.button] = True
                    elif e.type == JOYBUTTONUP:
                        self.joysticks[e.jbutton.which]["boutons"][e.jbutton.button] = False
                    elif e.type == JOYAXISMOTION:
                        self.joysticks[e.jaxis.which]["axes"][e.jaxis.axis] = e.jaxis.value
                    elif e.type == JOYHATMOTION:
                        self.joysticks[e.jhat.which]["chapeaux"][e.jhat.hat] = e.jhat.value

    def get_snapshot(self):
        return InputSnapshot(fields=deepcopy(self.__dict__))


class InputSnapshot:
    def __init__(self, *, fields):
        self.__dict__.update(fields)

    def is_key_pressed(self, key):
        return getattr(self, "touches_mapped")[key]

    def is_mouse_button_pressed(self, button):
        return getattr(self, "boutons_souris")[button]

    def get_mouse_position(self):
        return getattr(self, "sourisX"), getattr(self, "sourisY")

    def get_mouse_position_relative(self):
        return getattr(self, "sourisXRel"), getattr(self, "sourisYRel")

    def is_joystick_hat_triggered(self, joystick, hat, hat_position):
        joysticks = getattr(self, "joysticks")
        return joysticks[joystick]["chapeaux"][hat] == hat_position if joysticks else False

    def get_joystick_hat_position(self, joystick, hat):
        joysticks = getattr(self, "joysticks")
        return joysticks[joystick]["chapeaux"][hat] if joysticks else None

    def is_joystick_button_pressed(self, joystick, button):
        joysticks = getattr(self, "joysticks")
        return joysticks[joystick]["boutons"][button] if joysticks else False

    def get_joystick_axis_value(self, joystick, axis):
        joysticks = getattr(self, "joysticks")
        return joysticks[joystick]["axes"][axis]

    def again(self):
        return not getattr(self, "done")

    def number_of_joysticks(self):
        joysticks = getattr(self, "joysticks")
        return len(joysticks) if joysticks else 0

    def quit(self) -> object:
        setattr(self, "done", True)
