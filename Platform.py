import pygame, random

class Platform:
    def __init__(self, screen, y, option):
        self.screen = screen
        self.width = random.randint(75, 100)
        self.height = 15
        self.x = random.randint(0, screen.get_width() - self.width)
        self.y = y
        self.alpha = 255
        self.color = (80, 99, 13)  # RGB for the platform
        self.options = ["moving", "breakable", "default", "spring"]
        self.option = option
        self.countJumps = 1
        
        # Create a surface for the platform that can handle alpha
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # Create surface with alpha support
        
    def setInvisible(self):
        self.alpha = 0
    
    def draw(self):
        # Set the color with transparency (RGBA)
        rgba_color = (self.color[0], self.color[1], self.color[2], self.alpha)
        
        if self.options[self.option] == "breakable":
            self.surface.fill((0, 0, 0, 0))  
            pygame.draw.rect(self.surface, rgba_color, (0, 0, self.width // 2 - 2, self.height))
            pygame.draw.rect(self.surface, rgba_color, (self.width // 2 + 2, 0, self.width // 2 - 2, self.height))
        else:
            # Fill the surface with the platform color
            self.surface.fill(rgba_color)
        
        # Blit the platform surface to the main screen
        self.screen.blit(self.surface, (self.x, self.y))

