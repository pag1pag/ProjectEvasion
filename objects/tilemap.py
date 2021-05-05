from resources.map_loader import TileMapLoader


class TileMap:
    def __init__(self, game, map_title):
        self.loader = TileMapLoader(game, map_title)
        self.map = {}

    def load(self):
        self.loader.load(self.map)

    def draw(self, window, cam):
        for tile in self.map.values():
            tile.draw(window, cam)

    def get_tiles_around(self, x, y, radius):
        pass

    def collision(self, player):
        for tile in self.map:
            if tile.collides_with(player):
                print("Collision!")
