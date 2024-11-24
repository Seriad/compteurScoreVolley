import pygame

class Screen:
    # Classe de base pour un écran
    def __init__(self, screen):
        self.screen = screen

    def handle_events(self, events):
        # Méthode pour gérer les événements
        pass

    def update(self):
        # Méthode pour mettre à jour l'écran
        pass

    def draw(self):
        # Méthode pour dessiner l'écran
        pass


class MainMenu(Screen):
    # Écran d'accueil
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(None, 50)
        self.title = self.font.render("Écran d'Accueil", True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche
                    return "game"  # Passer à l'écran de jeu

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fond noir
        self.screen.blit(self.title, (250, 100))  # Afficher le titre
        pygame.display.flip()

class GameScreen(Screen):
    # Écran de jeu
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render("Jeu en cours", True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche
                    return "main_menu"  # Retour à l'écran principal

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 255))  # Fond bleu
        self.screen.blit(self.text, (250, 100))  # Afficher le texte du jeu
        pygame.display.flip()