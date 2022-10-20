import pygame
import os
import random

pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bird Fly!")

FPS = 60
BIRD_WIDTH, BIRD_HEIGHT = 55, 40
PILLAR_WIDTH, PILLAR_HEIGHT = 50, 400
BIRD_FALL_VEL = 30
FLY_VEL = 30
PILLAR_VEL = 30
WHITE = (255, 255, 255)

FAIL_FONT = pygame.font.SysFont('comicsans', 100)
SCORE_FONT = pygame.font.SysFont('comicsans', 40)

PILLAR_MOVE = pygame.USEREVENT + 1
PILLAR_MOVE_TIME = 500
pygame.time.set_timer(PILLAR_MOVE, PILLAR_MOVE_TIME)
PILLAR_ADD = pygame.USEREVENT + 2
PILLAR_ADD_TIME = 3000
pygame.time.set_timer(PILLAR_ADD, PILLAR_ADD_TIME)
BIRD_FALL = pygame.USEREVENT + 3
BIRD_FALL_TIME = 500
pygame.time.set_timer(BIRD_FALL, BIRD_FALL_TIME)

BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join('fly_bird/figures', 'background.png')), (WIDTH, HEIGHT))
BIRD = pygame.transform.scale(
    pygame.image.load(os.path.join('fly_bird/figures', 'bird.png')), (BIRD_WIDTH, BIRD_HEIGHT))
PILLAR = pygame.transform.scale(
    pygame.image.load(os.path.join('fly_bird/figures', 'pillar.png')), (PILLAR_WIDTH, PILLAR_HEIGHT))


def add_random_pillar(pillars):
    up_pillar = random.randint(-300, -100)
    down_pillar = up_pillar + PILLAR_HEIGHT + BIRD_HEIGHT * 3
    pillar = pygame.Rect(WIDTH - PILLAR_WIDTH,
                         up_pillar, PILLAR_WIDTH, PILLAR_HEIGHT)
    pillars.append(pillar)
    pillar = pygame.Rect(WIDTH - PILLAR_WIDTH,
                         down_pillar, PILLAR_WIDTH, PILLAR_HEIGHT)
    pillars.append(pillar)

def draw_window(bird, pillars, score):
    WIN.blit(BACKGROUND, (0, 0))

    for pillar in pillars:
        WIN.blit(PILLAR, (pillar.x, pillar.y))

    score_text = SCORE_FONT.render("Score: " + str(score), 1,
                                            WHITE)
    WIN.blit(score_text, (10, 10))

    WIN.blit(BIRD, (bird.x, bird.y))


    pygame.display.update()


def draw_game_fail():
    fail_text = "Game Failed"
    draw_text = FAIL_FONT.render(fail_text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2,
                         HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(2000)  # 几秒后重新开始游戏


def main():
    bird = pygame.Rect(20, HEIGHT//2, BIRD_WIDTH, BIRD_HEIGHT)
    pillars = []
    bird_die = False
    score = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == BIRD_FALL:
                bird.y += BIRD_FALL_VEL
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    bird.y -= FLY_VEL

            if event.type == PILLAR_MOVE:
                for pillar in pillars:
                    pillar.x -= PILLAR_VEL

                    if bird.colliderect(pillar):
                        bird_die = True
                        break
                        

                for pillar in pillars:
                    if pillar.x < 0:
                        score += 0.5
                        pillars.remove(pillar)
                        

            if event.type == PILLAR_ADD:
                add_random_pillar(pillars)

        if bird.y + BIRD_HEIGHT > HEIGHT or bird.y < 0:
            bird_die = True

        if bird_die:
            draw_game_fail()
            break

        draw_window(bird, pillars, int(score))

    main()


if __name__ == "__main__":
    main()
