from Utility.Settings import *

class Debug:
    def __init__(self, variable_getter, screen, name=None):
        self.var_getter = variable_getter
        self.screen = screen
        self.name = name if name else "Variable"

    def show(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f"{self.name}: {self.var_getter():.1f}", True, (255, 255, 255))
        self.screen.blit(text, (0, 0))
