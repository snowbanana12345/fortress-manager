import pygame
from src.gui.textbox import TextBox

def main():
    title = "Fort Haron Manager"


    pygame.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode((1000, 800))

    labels = ["ECONOMY", "ARMY", "DEFENCES", "RESEARCH", "MAGIC", "MAP", "PORTAL"]
    spacing = 37.5
    xlength = 100
    ylength = 50
    ypos = 40
    xpos = 0
    buttons = []
    fontsize = 15
    for label in labels:
        xpos += spacing
        button = TextBox(xpos, ypos, xlength, ylength, label, fontsize)
        buttons.append(button)
        xpos += xlength

    running = True
    while running:
        for button in buttons:
            button.render(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

if __name__ == "__main__":
    main()