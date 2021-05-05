from pygame.rect import Rect

from resources import manager


class Sprite:
    def __init__(self, x, y, **kwargs):
        self.game = kwargs.pop("game")
        self.texture = manager.get_texture(kwargs.pop("texture")).convert_alpha() \
            if "raw_surface" not in kwargs else kwargs.pop("raw_surface")

        width = kwargs.pop("animation_width", self.texture.get_size()[0])
        height = kwargs.pop("animation_height", self.texture.get_size()[1])

        self.rect = Rect(x, y, width, height)

        self.textures = dict([(j, [self.texture.subsurface(i * width, j * height, width, height)
                                   for i in range(0, self.texture.get_size()[0] // width)])
                              for j in range(0, self.texture.get_size()[1] // height)])

        # print("{} frame{} loaded.".format(len(self.textures), "" if len(self.textures) == 1 else "s"))

        self.current_texture_index = 0
        self.current_frame_progress = 0
        self.animation_state = 0
        self.update_rate = kwargs.pop("update_rate", 0)  # How fast should the animated sprite go?
        self.animated = kwargs.pop("animated", 0)  # Is this sprite animated?
        self.looping = kwargs.pop("looping", 0)  # Should the animation loop?

        self._animation_running = True

    def draw(self, window, cam):
        window.blit(self.textures[self.animation_state][self.current_texture_index], cam.apply(self))

    def update(self, delta):
        if self.animated and self._animation_running:
            self.current_frame_progress += delta
            if self.current_frame_progress >= self.update_rate:
                self.current_texture_index += 1
                self.current_frame_progress = 0

            if self.current_texture_index == len(self.textures[self.animation_state]):
                self.current_texture_index = 0
                if not self.looping:
                    self.stop_animation()

    def change_animation_state(self, i):
        self.animation_state = i

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_position(self):
        return self.rect.topleft

    def get_size(self):
        return self.textures[self.animation_state][self.current_texture_index].get_size()

    def stop_animation(self):
        self._animation_running = False

    def reset_animation(self):
        self.current_frame_progress = 0
        self.current_texture_index = 0

    def restart_animation(self):
        self._animation_running = True
        self.reset_animation()
