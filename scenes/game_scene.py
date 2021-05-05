from pygame.locals import *

from objects.camera import Camera
from objects.kholleur import Kholleur
from objects.player import Player
from objects.sprite import Sprite
from objects.tilemap import TileMap
from scenes.base_scene import BaseScene
from scenes.game_over_scene import GameOverScene
from scenes.kholle_scene import KholleScene


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.gravity = 0.001

        self.kholleurs = [Kholleur(640, 330, game=self.game), Kholleur(1760, 338, game=self.game)]

        self.map = TileMap(self.game, "linear")

        # self.background_music = self.game.create_music("Ragtime_1")

        self.player = Player(0, 0, game=self.game)

        self.background = Sprite(0, 0, texture="background.jpg", game=self.game)

        self.cam = Camera(self.game, 7200, 931)

        self.must_restart = False

        # self.snd = Sound("gun.wav")

    def on_start(self):
        self.map.load()
        # self.background_music.play()

    def quit(self):
        # self.background_music.stop()
        super().quit()

    def on_update(self, delta):
        # mouse_pos = self.get_mouse_position()
        # print("MousePos [x={}, y={}]".format(mouse_pos[0], mouse_pos[1]))
        delta = min(delta, 20)

        self.player.update(delta)
        self.player.fall(self.gravity, delta)

        self.player.handle_collisions(self.map)

        for kh in self.kholleurs:
            kh.update(delta)
        # self.kholleur.fall(self.gravity, delta)

        self.cam.update(self.player)

        for kh in self.kholleurs:
            if kh.collides_with(self.player):
                scene = KholleScene(self.game, kh, result_callback=self.on_kholle_result)
                scene.start()

        if self.must_restart:
            self.player.resurrect()
            self.player.set_position(0, 0)
            self.player.set_velocity(0, 0)
            self.must_restart = False

        if self.player.has_fallen_offstage(self.cam):
            self.fail()

    def on_draw(self):
        self.clear()
        self.background.draw(self.window, self.cam)
        self.map.draw(self.window, self.cam)
        for kh in self.kholleurs:
            kh.draw(self.window, self.cam)
        self.player.draw(self.window, self.cam)
        self.display()

    def fail(self, reason=None):
        self.must_restart = True
        self.player.damage(10000)
        over_scene = GameOverScene(self.game, reason)
        over_scene.start()

    def on_events(self, ev_list):
        for e in ev_list:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.quit()
                if e.key == K_UP:
                    self.player.jump()
                    self.player.change_animation_state(0)
                if e.key == K_DOWN:
                    self.player.ground_pound()
                    self.player.change_animation_state(2)
                if e.key == K_q:
                    self.player.begin_charged_jump()
                if e.key == K_f:
                    self.player.snipe()
            elif e.type == KEYUP:
                if e.key == K_q:
                    self.player.release_charged_jump()

        if self.is_key_pressed(K_LEFT):
            self.player.move_left()
            self.player.change_animation_state(1)

        if self.is_key_pressed(K_RIGHT):
            self.player.move_right()
            self.player.change_animation_state(3)

        if self.is_key_just_released(K_RIGHT):
            self.player.stop()

        if self.is_key_just_released(K_LEFT):
            self.player.stop()

        self.player.run_fast(self.is_key_pressed(K_w))

    def on_kholle_result(self, success, kholleur):
        if not success:
            self.fail("Oral foire. On n'a pas la place pour les rates a l'ENS.")
            self.quit()
        else:
            kholleur.damage(100)
