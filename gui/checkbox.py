import pygame
from pygame.rect import Rect

from gui.events.signal import Signal
from gui.label import Label
from gui.widget import Widget


class Checkbox(Widget):
    def __init__(self, x, y, checkbox_text, *, initial_state=False):
        super().__init__()

        self.rect = Rect(x, y, 0, 40)
        self.checked = initial_state

        self.box_rect = Rect(x, y, 40, 40)

        self.checked_rect = Rect(x + 5, y + 5, 31, 31)

        self.checkbox_label = Label(x + 50, 0, checkbox_text)
        self.checkbox_label.center_vertical(40, y)

        self._update_width()

        self.hover = False

        self.Checked = Signal()
        self.Checked.attach(self.on_checkbox_checked)

    def draw(self, window):
        pygame.draw.rect(window, (120, 120, 255) if self.hover else (110, 110, 110, 0), self.box_rect, 2)
        if self.checked:
            pygame.draw.rect(window, (156, 67, 232, 0), self.checked_rect)
        self.checkbox_label.draw(window)

    def handler(self, scene):
        mouse_pos = scene.get_mouse_position()
        if self.box_rect.contains(Rect(mouse_pos[0], mouse_pos[1], 1, 1)):
            self.hover = True
            if scene.is_mouse_clicked(0):
                self.checked = not self.checked
                self.Checked.emit(checked=self.checked)
        else:
            self.hover = False

    def on_checkbox_checked(self, *, checked):
        self.checkbox_label.set_text("On" if checked else "Off")
        self._update_width()

    def _update_width(self):
        self.rect.w = self.box_rect.w + 10 + self.checkbox_label.w
