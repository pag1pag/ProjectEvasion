import pygame

from gui.widget import Widget
from resources import manager


class Button(Widget):
    def __init__(self, x, y, text, **kwargs):
        super().__init__()
        self.game = kwargs.pop("game")
        self.string = text
        self.font = manager.get_font(kwargs.pop("font", 'main.ttf'), kwargs.pop("fontsize", 25))
        self.text = self.font.render(self.string, True, kwargs["textcolor"])
        self.posX = x
        self.posY = y
        size = self.font.size(self.string)
        self.w = size[0] + 10
        self.h = size[1] + 10
        self.originalBackColor = self.backColor = kwargs.pop("background_color", (255, 0, 0, 0))
        self.originalTextColor = self.textColor = kwargs["textcolor"]
        self.text_color_hover = kwargs.pop("textcolor_hover", self.textColor)
        self.mouseOver = False
        self.on_click_listener = kwargs.pop("listener", None)
        self.enabled = True
        self.draw_back = kwargs.pop("draw_back", False)

    def draw(self, window):
        if self.draw_back:
            pygame.draw.rect(window, self.backColor, (self.posX, self.posY, self.w, self.h))
        window.blit(self.text, ((self.posX + self.w / 2) - self.text.get_size()[0] / 2,
                                (self.posY + self.h / 2) - self.text.get_size()[1] / 2))

    def set_background_color(self, r, g, b, a=0):
        self.backColor = (r, g, b, a)

    def set_text_color(self, r, g, b, a=0):
        self.textColor = (r, g, b, a)
        self._render_text()

    def set_text(self, text):
        self.string = text
        self._render_text()
        self._recompute_size()

    def set_on_click_listener(self, listener):
        self.on_click_listener = listener

    def center_vertical(self):
        self.posY = self.game.get_height() / 2 - self.h / 2

    def center_horizontal(self):
        self.posX = self.game.get_width() / 2 - self.w / 2

    def center_on_screen(self):
        self.center_horizontal()
        self.center_vertical()

    def set_enabled(self, enable):
        self.enabled = enable
        if not self.enabled:
            self.set_background_color(128, 128, 128)
            self.set_text_color(225, 225, 255)
        else:
            self.backColor = self.originalBackColor
            self.text = self.originalBackColor

    def handler(self, scene):
        if not self.enabled:
            return
        mouse_pos = scene.get_mouse_position()
        if self._contains(mouse_pos[0], mouse_pos[1]):
            self.mouseOver = True
            self.set_text_color(*self.text_color_hover)
            if scene.is_mouse_clicked(0):
                if self.on_click_listener is not None:
                    self.on_click_listener(self)
        else:
            self.mouseOver = False
            self.set_text_color(*self.originalTextColor)

    def _recompute_size(self):
        size = self.font.size(self.string)
        self.w = size[0] + 10
        self.h = size[1] + 10

    def _render_text(self):
        self.text = self.font.render(self.string, True, self.textColor)

    def _contains(self, mouse_x, mouse_y):
        return self.posX <= mouse_x <= self.posX + self.w and self.posY <= mouse_y <= self.posY + self.h
