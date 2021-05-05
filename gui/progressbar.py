import pygame

from gui.events.signal import Signal
from gui.widget import Widget


class ProgressBar(Widget):
    def __init__(self, x, y, *, initial_position=0):
        super().__init__()
        self.x = x
        self.y = y
        self.w = 350
        self.h = 20
        self.outRectangleColor = (110, 110, 110, 0)
        self.innerRectangleColor = (0, 255, 0, 0)
        self.progress = initial_position
        self.innerH = 18
        self.innerW = self.progress / 100 * (self.w - 2)
        self.Done = Signal()
        self.ProgressChanged = Signal()

    def center_horizontal(self, w, offset=0):
        self.x = offset + w / 2 - self.w / 2

    def set_progress(self, percent):
        if self.progress >= 100:
            self.Done.emit()
            return
        self.ProgressChanged.emit(self.progress, percent)
        self.progress = percent
        self.innerW = self.progress / 100 * (self.w - 2)

    def get_progress(self):
        return self.progress

    def draw(self, window):
        pygame.draw.rect(window, self.outRectangleColor, (self.x, self.y, self.w, self.h), 1)
        pygame.draw.rect(window, self.innerRectangleColor, (self.x + 1, self.y + 1, self.innerW, self.innerH))
