import pygame
import random
from Player import Player
from Ink import Ink_Drop

pygame.init()

WIDTH = 1280
HEIGHT = 720
FONT = pygame.font.SysFont("comicsans", 30)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 2000)


def home_screen():
    screen.fill("white")

    start_text = FONT.render("Press Enter to Start", 1, "black")
    screen.blit(start_text, (WIDTH/2 - 100, HEIGHT/2))

    pygame.display.update()


def draw(player, objects, count):
    screen.fill("white")

    player_sprite = pygame.transform.scale(
        pygame.image.load("assets/Ink_Well.png"), (120, 120))
    screen.blit(player_sprite, (player.x, player.y))

    counter_text = FONT.render(str(count), True, "black")
    text_rect = counter_text.get_rect(center=screen.get_rect().center)
    screen.blit(counter_text, text_rect)

    for object in objects:
        object_sprite = pygame.transform.scale(
            object.image, (object.width, object.height))
        screen.blit(object_sprite, (object.x, object.y))
        object.move()

    pygame.display.update()


def handle_collision(objects, player):
    for i, object, in enumerate(objects):
        if player.x+10 >= object.x and player.x+10 <= object.x+50:
            if player.y <= object.y+50 and player.y+20 >= object.y:
                objects.pop(i)


def handle_movement(keys, player):
    if keys[pygame.K_a]:
        player.move("left")
    if keys[pygame.K_w]:
        player.move("up")
    if keys[pygame.K_d]:
        player.move("right")
    if keys[pygame.K_s]:
        player.move("down")


def main():
    run = True
    countnum = 10

    objects = []
    for drops in range(0, 30, 1):
        objects.append(Ink_Drop(random.randrange(
            20, 1260), random.randrange(-50, 30)))
    # for drops in numdrops:

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        home_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            run = False

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player = Player(round(WIDTH/2), round(HEIGHT/2))

        isrunning = True
        while isrunning:
            keys = pygame.key.get_pressed()
            clock.tick(60)

            draw(player, objects, countnum)
            handle_movement(keys, player)
            handle_collision(objects, player)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isrunning = False
                elif event.type == timer_event:
                    countnum -= 1
                    # counter(countnum)
                    if countnum == 0:
                        pygame.time.set_timer(timer_event, 0)
                        isrunning = False

        run = False

    pygame.quit()


if __name__ == "__main__":
    main()
