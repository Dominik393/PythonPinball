from Utility.Settings import *

class Debug:
    def __init__(self, variable_getter, screen, name=None):
        self.var_getter = variable_getter
        self.screen = screen
        self.name = name if name else "Variable"

    def show(self):
        font = pygame.font.Font(None, 36)

        if type(self.var_getter()) == list:
            value = ", ".join([f"{i:.5f}" for i in self.var_getter()])
        else:
            value = f"{self.var_getter():.5f}"

        text = font.render(f"{self.name}: {value}", True, (255, 255, 255))
        self.screen.blit(text, (0, 0))
