class Sound:
    """Classe pour gérer les sons (court et instantané)"""

    def __init__(self, sys, filename):
        self.sound = sys.system.create_sound(filename)
        self.channel = None

    def play(self):
        """jouer un son"""
        self.channel = self.sound.play()

    def stop(self):
        """arreter un son. il n'est pas toujours nécessaire d'arrêter de jouer le son"""
        if self.channel is not None:
            self.channel.stop()
