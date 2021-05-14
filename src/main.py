import pygame


def main():
    title = "Fort Haron Manager"

    pygame.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode((1000, 800))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
