import json

from objects.tile import Tile
from objects.tileset import TileSet


class TileMapLoader:
    """This is the map loader. We provide the level as a list of list of strings directly,
    otherwise we can use maps in JSON format:

    {
        "tileset": "my_spritesheet.png",
        "tile_width": 23,
        "tile_height": 23,
        "tileset_colorkey": [0, 0, 0, 0],
        "map": [
            {
                "type": "ground",
                "tile_x": 1,
                "tile_y": 3,

                "x": 10,
                "y": 10

            },
            {
                "type": "platform",
                "tile_x": 10,
                "tile_y": 2,

                "x": 11,
                "y": 10
            }
        ]
    }

    Coordinates for the tiles are multiplied by the tile width and height, so you provide only their
    emplacement in a grid.

    Tiles coordinates are their coordinates in the sprite sheet.
    """

    def __init__(self, game, level, *, raw=False):
        self.game = game
        if raw:
            self.pattern = level
        else:
            with open("levels/{}.json".format(level), "r") as f:
                self.pattern = json.load(f)

        try:
            self.tileset = TileSet(self.pattern["tileset"], self.pattern["tile_width"], self.pattern["tile_height"],
                                   colorkey=self.pattern["tileset_colorkey"])

            if not self.pattern["enable_padding"]:
                self.tileset.set_padding(self.pattern["tile_padding_width"], self.pattern["tile_padding_height"])
        except KeyError as e:
            print("Error loading tileset infos. Please check your map file. Exiting : {}".format(e))
            self.game.stop()

    def load(self, tilemap):
        print("Loading tileset...")
        self.tileset.generate()
        print("Tiles generated.")

        print("Generating map...")
        tile_size = self.tileset.get_tile_size()
        tile_w = tile_size[0]
        tile_h = tile_size[1]

        for t in self.pattern["map"]:
            tilemap[t["x"], t["y"]] = Tile(t["x"] * tile_w, t["y"] * tile_h,
                                           game=self.game,
                                           tile_x=t["x"],
                                           tile_y=t["y"],
                                           type=t["type"],
                                           raw_surface=self.tileset.get_tile(t["tile_x"],
                                                                             t["tile_y"]))
        print("Map generated.")
