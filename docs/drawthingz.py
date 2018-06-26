import pygame

class drawLevel:
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    def level1(self, surface):
        pygame.draw.polygon(surface, self.black, ((100, 500), (700, 500), (700, 480), (100, 480)))

    def level2(self, surface):
        pygame.draw.polygon(surface, self.black, ((100, 500), (700, 500), (700, 480), (400, 480), (400, 100), (380, 100), (380, 480), (100, 480)))

    def level3(self, surface):
        pygame.draw.polygon(surface, self.black, ((100, 500), (700, 500), (700, 480), (400, 480), (400, 100), (700, 100), (700, 80), (380, 80), (380, 480), (100, 480)))

    def level4(self, surface):
        pygame.draw.polygon(surface, self.black, ((100, 500), (700, 500), (700, 480), (400, 480), (400, 100), (700, 100), (700, 80), (380, 80), (380, 480), (100, 480)))
        pygame.draw.circle(surface, self.black, (700, 130), 30, 10)

    def level5(self, surface):
        pygame.draw.polygon(surface, self.black, ((100, 500), (700, 500), (700, 480), (400, 480), (400, 100), (700, 100), (700, 80), (380, 80), (380, 480), (100, 480)))
        pygame.draw.circle(surface, self.black, (700, 130), 30, 10)
        pygame.draw.polygon(surface, self.black, ((695, 150), (705, 150), (705, 350), (695, 350)))

    def level6(self, surface):
        pygame.draw.polygon(surface, self.black, ((100, 500), (700, 500), (700, 480), (400, 480), (400, 100), (700, 100), (700, 80), (380, 80), (380, 480), (100, 480)))
        pygame.draw.circle(surface, self.black, (700, 130), 30, 10)
        pygame.draw.polygon(surface, self.black, ((695, 150), (705, 150), (705, 195), (750, 195), (750, 205), (705, 205), (705, 350), (695, 350)))

    def level7(self, surface):
        pygame.draw.polygon(surface, self.black, ((100, 500), (700, 500), (700, 480), (400, 480), (400, 100), (700, 100), (700, 80), (380, 80), (380, 480), (100, 480)))
        pygame.draw.circle(surface, self.black, (700, 130), 30, 10)
        pygame.draw.polygon(surface, self.black, ((695, 150), (705, 150), (705, 195), (750, 195), (750, 205), (705, 205), (705, 350), (695, 350), (695, 205), (650, 205), (650, 195), (695, 195)))

    def level8(self, surface):
        pygame.draw.polygon(surface, self.black, ((100, 500), (700, 500), (700, 480), (400, 480), (400, 100), (700, 100), (700, 80), (380, 80), (380, 480), (100, 480)))
        pygame.draw.circle(surface, self.black, (700, 130), 30, 10)
        pygame.draw.polygon(surface, self.black, ((695, 150), (705, 150), (705, 195), (750, 195), (750, 205), (705, 205), (705, 350), (750, 410), (740, 410), (695, 350), (695, 205), (650, 205), (650, 195), (695, 195)))

    def level9(self, surface):
        pygame.draw.polygon(surface, self.black, ((100, 500), (700, 500), (700, 480), (400, 480), (400, 100), (700, 100), (700, 80), (380, 80), (380, 480), (100, 480)))
        pygame.draw.circle(surface, self.black, (700, 130), 30, 10)
        pygame.draw.polygon(surface, self.black, ((695, 150), (705, 150), (705, 195), (750, 195), (750, 205), (705, 205), (705, 350), (750, 410), (740, 410), (695, 350), (705, 350), (660, 410), (650, 410), (695, 350), (695, 205), (650, 205), (650, 195), (695, 195)))
