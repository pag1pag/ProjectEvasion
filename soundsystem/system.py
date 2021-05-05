import pyfmodex


class System:
    """Classe d'initialisation du système de pyfmodex. Ne doit être lancé qu'une fois en initialisation."""

    def __init__(self):
        self.system = pyfmodex.System()
        self.system.init()

    def __del__(self):
        self.system.close()
        self.system.release()
