import pygame

from events.input import K_LAST


class BaseScene:
    """A class implementing the principle of a scene.
    A scene starts, and then indefinitely receives events, updates, and draws itself
    on the screen. You simply have to subclass this class, and specialize the callbacks
    to your content."""

    def __init__(self, game):
        """Class constructor. Nothing much is being done here."""
        self.clock = pygame.time.Clock()  # FPS-management
        self.exited = False  # Are we leaving the scene?
        self.closed = False  # Are we closing the game?
        self.game = game  # The game the scene is in. Singletons are shit in Python, so we pass it everywhere
        self.window = game.window  # The window the game uses. Kept for backwards compatibility.

        # self.input = Input()  # The event input class. Deprecated. Do not use.
        # self.snap = None  # Current snapshot of inputs. Useful to detect triggers.
        # self.last_snap = None  # Snapshot of last frame. Used with the current one to compare states.

        self.keyboard_state = [False] * K_LAST  # The last keyboard state. Useful to detect triggers.
        self.last_keyboard_state = [False] * K_LAST  # Current keyboard state. Used with the last one to compare states.
        self.mouse_state = [False] * 3  # Same as keyboard, but for the mouse.
        self.last_mouse_state = [False] * 3  # Same as above.

    def start(self):
        """Start the scene. Off we go!"""
        # We signal to your scene that it has started, load your assets (images, sounds) here.
        self.on_start()

        while (not self.exited) and (not self.closed):  # Semi-endless loop
            t = self.clock.tick(self.game.fps)  # We pause the game for ~1000/FPS ms to prevent CPU overloading

            self.last_keyboard_state = pygame.key.get_pressed()
            self.last_mouse_state = pygame.mouse.get_pressed()

            ev_list = pygame.event.get()

            self.keyboard_state = pygame.key.get_pressed()
            self.mouse_state = pygame.mouse.get_pressed()

            # --- Deprecated ---
            # self.last_snap = self.input.get_snapshot()
            # self.input.update(ev_list)
            # self.snap = self.input.get_snapshot()

            # We update the scene logic, perform your computations (position and size updates)
            # here.
            self.on_update(t)

            self.on_events(ev_list)  # Manage events in your own scene here.

            # We draw the scene on the screen. Perform all your drawing stuff (draw textures)
            # here.
            self.on_draw()

    def quit(self):
        """Exit the scene. I'm done!"""
        self.exited = True  # We requested that the scene should end.

    def close(self):
        """Close the window. I just recalled I had friends..."""
        self.closed = True  # We requested that the game should close.

    def clear(self):
        """Clear the screen. Ready for the new scenery!"""
        self.window.fill((0, 0, 0))  # Convenience method for clearing the window surface.

    def display(self):
        """Bring forth the scene!"""
        pygame.display.flip()  # Convenience method for updating the window surface.

    def is_key_just_released(self, key):
        return not self.keyboard_state[key] and self.last_keyboard_state[key]

    def is_key_just_pressed(self, key):
        return self.keyboard_state[key] and not self.last_keyboard_state[key]

    def is_key_pressed(self, key):
        return self.keyboard_state[key]

    def is_mouse_pressed(self, mouse_button):
        return self.mouse_state[mouse_button]

    def is_mouse_clicked(self, mouse_button):
        return self.mouse_state[mouse_button] and \
               not self.last_mouse_state[mouse_button]

    def is_mouse_released(self, mouse_button):
        return not self.mouse_state[mouse_button] and \
               self.last_mouse_state[mouse_button]

    def get_mouse_position(self):
        return pygame.mouse.get_pos()

    """This part concerns callbacks for the scene.
    
    Bon ok j'arr??te de troller avec l'anglais."""

    def on_start(self):
        """Callback for when the scene begins.
        This method is pretty much designed for you to load some heavy resources into memory,
        such as textures needed for the scene.

        Ici, comme indiqu?? plus haut, il faut surcharger (red??finir) cette m??thode dans
        la sc??ne cr????e. Ce qui se fait dans cette m??thode est plut??t de l'ordre du chargement
        d'assets, dans le style images, sons, musiques, polices, etc.
        """
        return NotImplemented

    def on_update(self, delta):
        """Callback for updating the scene's physics.
        Do all your physics stuff in here. You're not roughly obligated though, but it's
        a good practice to separate the computing from the drawing stuff.

        Ici sera impl??ment?? la 'logique physique' de la sc??ne. Les positions physiques des
        sprites devront ??tre mises ?? jour ici, comme les forces appliqu??es si c'est d'un
        corps pesant dont il s'agit de mettre ?? jour, ou plus g??n??ralement, les coordonn??es
        des sprites pour les faire bouger dans la sc??ne.

        L'argument delta repr??sente le temps en millisecondes ??coul?? depuis la derni??re
        frame. Typiquement, ce temps correspond ?? `1000 / FPS` millisecondes."""
        return NotImplemented

    def on_draw(self):
        """Callback for drawing stuff on the screen.
        Draw your textures here. Again, I won't hunt you down if you don't, but it's still
        a good practice. Keep things organized.

        Ici, on dessine tous les sprites de la sc??ne. On pensera ??galement ?? nettoyer la sc??ne
        au d??but pour ??viter de redessiner par-dessus la frame pr??c??dente, ainsi que d'afficher
        la sc??ne ?? la fin pour pouvoir voir quelque chose, accessoirement.

        Note: ce comportement est classique, cependant il n'est pas toujours voulu: ainsi,
        l'??tape nettoyage/affichage de la sc??ne est ?? la charge de la sc??ne fille."""
        return NotImplemented

    def on_events(self, ev_list):
        """Callback for taking into account events from the player.
        The actions of the player are to be handled here, since the input snapshot described
        by `e` isn't likely te be valid anymore on the next frame.

        Ici, on traite les ??v??nements qui parviennent ?? la sc??ne. Il vient que les ??tats clavier
        (touches enfonc??es, rel??ch??es, position de la souris, boutons appuy??s) doivent ??tre
        sauvegard??s dans l'instance de la classe pour pouvoir ??tre utilis??s dans
        :meth:`on_update`.

        Note: je pense impl??menter un syst??me de classe ?? ??tats qui stockera l'??tat des inputs
        ?? l'instant t. Ainsi, il n'y aura qu'?? update ces ??tats pour s'en servir dans le callback
        :meth:`on_update`."""
        return NotImplemented
