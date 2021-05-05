from gui.widget import Widget
from resources import manager


class Label(Widget):
    def __init__(self, x, y, text, **kwargs):
        super().__init__()
        self.fontsize = kwargs.pop('fontsize', kwargs.pop("fontsize", 14))
        self.string = text
        self.textColor = kwargs.pop("textcolor", (0, 255, 0, 0))

        self.font = manager.get_font(kwargs.pop("font", 'main.ttf'), self.fontsize)
        self.text = self.font.render(self.string, True, self.textColor)

        self.x = x
        self.y = y
        self.w = self.text.get_size()[0]
        self.h = self.text.get_size()[1]

    def set_text_color(self, r, g, b, a=0):
        self.textColor = (r, g, b, a)
        self._render_text()

    def set_text(self, string):
        self.string = string
        self._render_text()
        self._recompute_size()

    def draw(self, window):
        window.blit(self.text, (self.x, self.y))

    def center_horizontal(self, w, offset=0):
        self.x = offset + w / 2 - self.w / 2

    def center_vertical(self, h, offset=0):
        self.y = offset + h / 2 - self.h / 2

    def _recompute_size(self):
        size = self.font.size(self.string)
        self.w = size[0]
        self.h = size[1]

    def _render_text(self):
        self.text = self.font.render(self.string, True, self.textColor)
