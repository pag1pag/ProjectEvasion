from objects.bot import Bot


class Kholleur(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, texture='Dragon Rouge.png', animated=True, animation_width=96, animation_height=96,
                         looping=True, update_rate=150, **kwargs)

