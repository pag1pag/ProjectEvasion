from objects.object import Object


class Tile(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = kwargs.pop("type")
        self.tile_x = kwargs.pop("tile_x")
        self.tile_y = kwargs.pop("tile_y")
