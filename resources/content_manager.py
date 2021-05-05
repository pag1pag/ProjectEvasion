import pygame


class ContentManager:
    def __init__(self):
        self.textures = {}
        self.fonts = {}

    def get_texture(self, texture_name):
        if texture_name not in self.textures:
            self.textures[texture_name] = pygame.image.load("img/{}".format(texture_name))

        return self.textures[texture_name]

    def get_font(self, font_name, size):
        if (font_name, size) not in self.fonts:
            self.fonts[font_name, size] = pygame.font.Font("fonts/{}".format(font_name), size)

        return self.fonts[font_name, size]

    def __getitem__(self, item):
        if item in self.textures:
            return self.textures[item]
        if item in self.fonts:
            return self.fonts[item]

        raise KeyError("{} is not a resource.".format(item))

    def __setitem__(self, key, value):
        raise RuntimeError("Operation not allowed")
