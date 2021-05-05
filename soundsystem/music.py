class Music:
    """Classe pour gérer les musiques (long et en bakground)"""

    def __init__(self, sys, filename):
        self.musique = sys.system.create_stream(filename)
        self.channel = None
        self.playing = False

    def play(self):
        """jouer une musique"""
        self.channel = self.musique.play()
        self.playing = True

    def stop(self):
        """arrêter une musique"""
        if self.channel is not None and self.is_playing():
            self.channel.stop()
            self.playing = False

    def loop(self):
        if self.channel is not None:
            self.channel.loop_count = -1

    def is_playing(self):
        return self.playing
