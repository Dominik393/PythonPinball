from Utility.Settings import *
from GameObjects.Ball import Ball
from GameObjects.Flipper import Flipper
from Utility.Debug import Debug
from Core.DeltaTime import DeltaTime


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pinball")
    clock = pygame.time.Clock()
    delta_time = DeltaTime(clock)
    running = True

    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    flipper = Flipper(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, 100, 20)
    debug = Debug(flipper.get_angle, screen)
    ball.speed_vector = [1, 0]

    while running:
        screen.fill((80, 80, 100))
        delta_time.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball.update(delta_time.delta_time)
        flipper.update(delta_time.delta_time)
        ball.draw(screen)
        flipper.draw(screen)
        debug.show()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()