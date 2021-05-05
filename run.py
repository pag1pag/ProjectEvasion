from core.game import Game

FPS = 60


def main():
    g = Game("Project::Evasion", 1280, 720, fps=60)
    g.run()


if __name__ == '__main__':
    main()
