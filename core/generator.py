import json


class FlatGenerator:
    def __init__(self, tile_x, tile_y, number, altitude):
        self.data = {
            "tileset": "main_sheet.png",
            "tile_width": 23,
            "tile_height": 23,

            "tileset_colorkey": [94, 129, 162, 0],
            "map": [],
            "tile_padding_width": 1,
            "tile_padding_height": 1,
            "enable_padding": False
        }
        self.number = number
        self.alt = altitude
        self.tx = tile_x
        self.ty = tile_y

    def generate(self):
        for i in range(self.number):
            self.data["map"].append({
                "type": "ground",
                "tile_x": self.tx,
                "tile_y": self.ty,
                "x": i,
                "y": self.alt
            })

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.data, f, indent=2)


if __name__ == '__main__':
    gen = FlatGenerator(3, 4, 500, 50)

    print("Generating...")
    gen.generate()
    print("Generated. Saving...")
    gen.save("flat.json")
    print("Saved.")
