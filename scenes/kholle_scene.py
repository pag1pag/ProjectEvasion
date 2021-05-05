import json
import random

from gui.button import Button
from gui.label import Label
from gui.progressbar import ProgressBar
from objects.camera import Camera
from objects.sprite import Sprite
from scenes.base_scene import BaseScene


# Placer le fichier "tests.txt" dans un repertoire parent nommé "questions"


class KholleScene(BaseScene):
    """This is the scene which will hold the 'kholle' event"""

    def __init__(self, game, kholleur, *, result_callback):
        """Creating all we need here"""
        super().__init__(game)
        self.progress = ProgressBar(0, 650)
        self.kholleur = kholleur

        self.success_hook = result_callback

        self.back = Sprite(0, -150, texture="chalkboard.jpg", game=self.game)

        self.button_hg = Button(200, 200, "Button", game=self.game, font='crumble.ttf', fontsize=48,
                                textcolor=(245, 220, 236), textcolor_hover=(58, 245, 162), draw_back=False)
        self.button_hd = Button(700, 200, "Button", game=self.game, font='crumble.ttf', fontsize=48,
                                textcolor=(245, 220, 236), textcolor_hover=(58, 245, 162), draw_back=False)
        self.button_bg = Button(200, 400, "Button", game=self.game, font='crumble.ttf', fontsize=48,
                                textcolor=(245, 220, 236), textcolor_hover=(58, 245, 162), draw_back=False)
        self.button_bd = Button(700, 400, "Button", game=self.game, font='crumble.ttf', fontsize=48,
                                textcolor=(245, 220, 236), textcolor_hover=(58, 245, 162), draw_back=False)
        self.button = [self.button_hg, self.button_hd, self.button_bg, self.button_bd]

        self.entete = Label(0, 70, "Label", font='whatever.ttf', fontsize=72, textcolor=(255, 255, 255))

        self.percent = 0
        self.formulaire = None  # récupère les questions

        self.cam = Camera(self.game, self.game.get_width(), self.game.get_height())

        self.entete.center_horizontal(self.game.get_width())
        self.progress.center_horizontal(self.game.get_width())

    def what_is_the_question(self):
        with open("questions/tests.txt", "r") as file:  # Les questions sont entreposées dans un fichier txt à part
            text = list()
            for ligne in file:
                text.append(ligne)
        question = random.choice(text)
        return question

    def on_start(self):
        """Initialisation of all the stuff here"""
        self.formulaire = json.loads(self.what_is_the_question())
        self.entete.set_text(self.formulaire['Question'])
        self.entete.center_horizontal(self.game.get_width())

        for i in range(0, 4):
            self.init_button(self.button[i], i)

    def init_button(self, button, i):
        """Create the button"""
        alphabet = ["A : "+self.formulaire['A'], "B : "+self.formulaire['B'], "C : "+self.formulaire['C'],
                    "D : "+self.formulaire['D']]
        button.set_text(alphabet[i])
        button.set_on_click_listener(self.has_clicked)

    def has_clicked(self, sender):
        """Check if the player has clicked on a button"""
        for i in range(0, 4):
            if sender is self.button[i]:  # Instance de l'objet qui a appel l'évenement
                self.button[i].set_enabled(False)  # On ne peut plus cliquer sur le bouton
                self.finish_him()  # ferme la fenêtre
                self.good_answer(self.button[i].string[0])  # Permet de savoir si on a la bonne réponse

    def good_answer(self, answer):
        """Check the answer provided by the player"""
        self.success_hook(answer == self.formulaire['Reponse'], self.kholleur)

    def finish_him(self):
        """This is the end, hold your breath and count to ten..."""
        self.quit()

    def on_update(self, delta):
        """Update all variables here"""
        # Update the Progress bar
        self.percent += delta*(60/(1000*20))
        if self.percent >= 100:
            self.finish_him()
            self.success_hook(False, self.kholleur)
        self.progress.set_progress(self.percent)

        # 4 petits boutons
        for i in range(0, 4):
            self.button[i].handler(self)

    def on_draw(self):
        """Draw all the things that have to be drawn on this scene"""
        self.clear()
        self.back.draw(self.window, self.cam)
        self.progress.draw(self.window)
        self.entete.draw(self.window)

        for i in range(0, 4):
            self.button[i].draw(self.window)

        self.display()

    def on_events(self, ev_list):
        """Get the input"""
        pass
