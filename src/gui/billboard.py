from src.gui.icon import Icon
from src.gui.square_box import SquareBox
from src.gui.textbox import TextBox


class BillBoard(SquareBox):
    def __init__(self, xpos, ypos, xlength, ylength):
        super().__init__(xpos, ypos, xlength, ylength)
        self.text_boxes = []
        self.icons = []
        self.buttons = []
        self.font_size = 15

    """
    positions are now relative to the icon positions
    """
    def add_icon(self, xpos, ypos, xlength, ylength, pygame_image):
        new_xpos = self.xpos + xpos
        new_ypos = self.ypos + ypos
        new_icon = Icon(new_xpos, new_ypos, xlength, ylength, pygame_image)
        self.icons.append(new_icon)

    def add_text_box(self, xpos, ypos, xlength, ylength, text):
        new_xpos = self.xpos + xpos
        new_ypos = self.ypos + ypos
        new_text_box = TextBox(new_xpos, new_ypos, xlength, ylength, text, self.font_size)

    def render(self, surface):
        super().render(surface)
        for text in self.text_boxes:
            text.render(surface)
        for icon in self.icons:
            icon.render(surface)

