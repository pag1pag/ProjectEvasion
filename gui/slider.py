import pygame
from pygame.rect import Rect

from gui.events.signal import Signal
from gui.widget import Widget


class Slider(Widget):
    def __init__(self, x, y, *, initial_position=50):
        super().__init__()

        self.rect = Rect(x, y, 300, 50)

        self.position = Rect(self.rect.x + (initial_position / 100) * self.rect.w - 10, y, 20, self.rect.height)
        self.hover = False
        self.clicked = False

        self.PositionChanged = Signal()

    def draw(self, window):
        pygame.draw.line(window, (110, 110, 110, 0), (self.rect.x, self.rect.y + self.rect.h / 2 - 1),
                         (self.rect.x + self.rect.w, self.rect.y + self.rect.h / 2 - 1), 2)
        pygame.draw.rect(window, (162, 58, 224, 0) if (self.hover or self.clicked) else (160, 160, 160, 0),
                         self.position)

    def handler(self, scene):
        mouse_pos = scene.get_mouse_position()
        if self.position.contains(Rect(mouse_pos[0], mouse_pos[1], 1, 1)):
            self.hover = True
            if scene.is_mouse_pressed(0):
                self.clicked = True
            else:
                self.clicked = False
        else:
            self.hover = False
            if not scene.is_mouse_pressed(0):
                self.clicked = False

        if self.clicked:
            self.position.x = min(max(mouse_pos[0] - self.position.w / 2, self.rect.x - self.position.w / 2),
                                  self.rect.x + self.rect.w - self.position.w / 2)
            self.PositionChanged.emit(position=int((self.position.x + self.position.w / 2 - self.rect.x) / self.rect.w * 100))

