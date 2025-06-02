import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    # ЗВУК


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0


    score = 0 
    font = pygame.font.SysFont(None, 36)


    lives = 3 
    is_alive = True
    respawn_timer = 0

    background_image = pygame.image.load("275248.jpg").convert()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        if not is_alive:
            respawn_timer -= dt
            if respawn_timer <= 0:
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                is_alive = True

        for asteroid in asteroids:
            if is_alive and  asteroid.collides_with(player):
                lives -= 1
                is_alive = False
                respawn_timer = 2
                player.kill()

                if lives <= 0 :
                    print("Гамовер")
                    sys.exit()


            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score +=100

        screen.blit(background_image, (0, 0))

        for obj in drawable:
            obj.draw(screen)

        score_surface = font.render(f"Score: {score}", True, "white")
        screen.blit(score_surface, (10, 10))
        lives_surface = font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_surface, (10, 50))
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()