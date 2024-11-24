import pygame

class Button:
    def __init__(self, x, y, width, height, color, original_color, hover_color, text, text_color, font_size=36):
        
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.original_color = original_color
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen, mouse_pos):
        #"""Dessine le bouton sur l'écran."""
        # Vérifier si la souris survole le bouton et changer la couleur si nécessaire
        self.update_color(mouse_pos)
        pygame.draw.rect(screen, self.color, self.rect)  # Dessiner le bouton
        screen.blit(self.text_surface, self.text_rect)  # Dessiner le texte sur le bouton

    def update_color(self, mouse_pos):
        #"""Met à jour la couleur du bouton en fonction de la position de la souris."""
        if self.is_hovered(mouse_pos):
            self.color = self.hover_color  # Changer la couleur du bouton au survol
        else:
            self.color = self.original_color # Garder la couleur d'origine

    def is_hovered(self, mouse_pos):
        #"""Vérifie si la souris est au-dessus du bouton."""
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_button):
        #"""Vérifie si le bouton a été cliqué."""
        return self.rect.collidepoint(mouse_pos) and mouse_button == 1
