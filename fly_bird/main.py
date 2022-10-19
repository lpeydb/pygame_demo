import pygame
import os
import random

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
BIRD_WIDTH, BIRD_HEIGHT = 55, 40
PILLAR_WIDTH, PILLAR_HEIGHT = 50, 200
FALL_VEL = 2
FLY_VEL = 10
PILLAR_VEL = 30

PILLAR_MOVE = pygame.USEREVENT + 1
PILLAR_MOVE_TIME = 500
pygame.time.set_timer(PILLAR_MOVE, PILLAR_MOVE_TIME)
PILLAR_ADD = pygame.USEREVENT + 2
PILLAR_ADD_TIME = 3000
pygame.time.set_timer(PILLAR_ADD, PILLAR_ADD_TIME)

BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join('fly_bird/figures', 'background.png')), (WIDTH, HEIGHT))
BIRD = pygame.transform.scale(
    pygame.image.load(os.path.join('fly_bird/figures', 'bird.png')), (BIRD_WIDTH, BIRD_HEIGHT))
PILLAR = pygame.image.load(os.path.join('fly_bird/figures', 'pillar.png'))
PILLAR = pygame.transform.scale(
    pygame.image.load(os.path.join('fly_bird/figures', 'pillar.png')), (PILLAR_WIDTH, PILLAR_HEIGHT))


def bird_handle_movement(keys_pressed, bird):
    if keys_pressed[pygame.K_SPACE]:  # FLY
        bird.y -= FLY_VEL


def draw_window(bird, pillars):
    WIN.blit(BACKGROUND, (0, 0))

    WIN.blit(BIRD, (bird.x, bird.y))
    for pillar in pillars:
        WIN.blit(PILLAR, (pillar.x, pillar.y))

    pygame.display.update()


def main():
    bird = pygame.Rect(50, HEIGHT//2, BIRD_WIDTH, BIRD_HEIGHT)
    pillars = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == PILLAR_MOVE:
                for pillar in pillars:
                    pillar.x -= PILLAR_VEL

            if event.type == PILLAR_ADD:
                pillar_len = random.randint(50,300)
                pillar = pygame.Rect(pygame.transform.scale(PILLAR, (PILLAR_WIDTH, pillar_len)

                down_pillar = up_pillar + + PILLAR_HEIGHT +BIRD_HEIGHT * 2
                pillar = pygame.Rect(WIDTH - PILLAR_WIDTH, up_pillar, PILLAR_WIDTH, up_pillar)
                pillars.append(pillar)
                pillar = pygame.Rect(WIDTH - PILLAR_WIDTH, down_pillar, PILLAR_WIDTH, HEIGHT)
                pillars.append(pillar)

        keys_pressed = pygame.key.get_pressed()
        bird_handle_movement(keys_pressed, bird)

        bird.y += FALL_VEL

        draw_window(bird, pillars)


if __name__ == "__main__":
    main()
