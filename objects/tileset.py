import pygame

from resources import manager


class TileSet:
    def __init__(self, spritesheet, tilewidth, tileheight, **kwargs):
        self.spritesheet = spritesheet
        self.tilesize = [tilewidth, tileheight]
        self.tile_padding_width = 0
        self.tile_padding_height = 0
        self.color_key = kwargs.pop("colorkey", (0, 0, 0, 0))

        self._sheet = None
        self.tiles = []

    def set_padding(self, w, h):
        self.tile_padding_width = w
        self.tile_padding_height = h

    def generate(self):
        self._sheet = manager.get_texture(self.spritesheet).convert()
        self._sheet.set_colorkey(self.color_key)
        number_of_tiles_width = self._sheet.get_size()[0] // self.tilesize[0]
        number_of_tiles_height = self._sheet.get_size()[1] // self.tilesize[1]

        for x in range(number_of_tiles_width):
            for y in range(number_of_tiles_height):
                r = pygame.Rect(x * self.tilesize[0] + self.tile_padding_width,
                                y * self.tilesize[1] + self.tile_padding_height,
                                self.tilesize[0] - self.tile_padding_width,
                                self.tilesize[1] - self.tile_padding_height)

                self.tiles.append(self._sheet.subsurface(r))
        print("{} tiles loaded.".format(len(self.tiles)))

    def get_tile(self, x, y):
        return self.tiles[(x * self._sheet.get_size()[1] // self.tilesize[1]) + y]

    def get_tile_size(self):
        return self.tilesize[0] - 2 * self.tile_padding_width,\
               self.tilesize[1] - 2 * self.tile_padding_height
