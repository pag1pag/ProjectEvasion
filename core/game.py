import pygame
from pygame.constants import DOUBLEBUF, HWSURFACE

from scenes.main_scene import MainScene
from soundsystem.music import Music
# from soundsystem.system import System


class Game:
    """This class holds the game itself. It manages the sound system, the content manager, the user settings
    (such as keybindings, user preferences, and the like). It should be accessible anywhere in the code."""
    def __init__(self, name, width, height, *, fps=60):
        self.window_name = name  # The name of the window, displayed in the title bar. Easy.
        self.width = width  # The width of the window. Who said that coding games was difficult?
        self.height = height  # The height of the window. Straightforward, ain't it?
        self.fps = fps  # The Frame rate per Second. Usually 60 FPS, i.e. every 16 milliseconds, the scene is redrawn.
        self.window = None  # The main SDL Surface that acts as a window. Yes, PyGame still uses SDL 1.2. Sad.

        # self.audio_system = System()

        self.startup_scene = None  # We shall start off with the Main Menu scene later. Hang on tight.

        pygame.init()  # Let's initialise all this stuff.

    def run(self):
        """Let's head off right into business! Show me some skill mate!"""
        self.window = pygame.display.set_mode((self.width, self.height), HWSURFACE | DOUBLEBUF)
        pygame.display.set_caption(self.window_name)

        # This must be done here, otherwise the scene wouldn't know of the newly born window.
        self.startup_scene = MainScene(self)

        self.startup_scene.start()

    # def create_music(self, filename):
    #     return Music(self.audio_system, "musics/{}.wav".format(filename))

    def get_width(self):
        """I won't even bother to explain what this does."""
        return self.width

    def get_height(self):
        """Neither will I say anything here."""
        return self.height

    def stop(self):
        """Ouch, something has gone wrong if you resort to call that."""
        self.startup_scene.close()  # Forcefully closes the game.

    def __del__(self):
        """We gotta clean up the mess we created. We're leaving it nice and neat."""
        pygame.quit()
