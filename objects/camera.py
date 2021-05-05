from pygame.rect import Rect


class Camera:
    def __init__(self, game, width, height):
        self.game = game
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.complex_camera(self.state, target.rect)

    def complex_camera(self, camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t, _, _ = -l + self.game.get_width()//2, -t + self.game.get_height()//2, w, h

        l = min(0, l)  # stop scrolling at the left edge
        l = max(-(camera.width - self.game.get_width()), l)  # stop scrolling at the right edge
        t = max(-(camera.height - self.game.get_height()), t)  # stop scrolling at the bottom
        t = min(0, t)  # stop scrolling at the top
        return Rect(l, t, w, h)
