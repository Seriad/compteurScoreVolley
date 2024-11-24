import pygame

class zoneAffichage:
    def __init__(self, x, y, width, height, color, text_color, score=0, font_size=80):

        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text_color = text_color
        self.score = score  # Stocker le score en tant qu'entier
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen):
        # Convertir le score en chaîne de caractères avant de le rendre
        text = str(self.score)
        text_surface = self.font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        
        # Dessiner la zone
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(text_surface, text_rect)

    def update_score(self, new_score):
        self.score = new_score
