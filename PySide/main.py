import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QRect
from zoneAffichage import ZoneAffichage
from bouton import Button


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scores")
        self.setGeometry(100, 100, 1000, 1000)

        # Conteneur principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Chargement de l'image de fond
        self.background_label = QLabel(self.central_widget)
        self.pixmap = QPixmap("volleyball-2.jpg")

        # Scores et états
        self.scoreGauche = 0
        self.scoreDroite = 0
        self.scoreSetGauche = 0
        self.scoreSetDroit = 0
        self.nombreSet = 0

        # Création des widgets
        self.create_widgets()

    def create_widgets(self):
        # Boutons
        self.moins_gauche = Button(self.central_widget, " - ", self.update_score_gauche, -1)
        self.plus_gauche = Button(self.central_widget, " + ", self.update_score_gauche, 1)
        self.moins_droite = Button(self.central_widget, " - ", self.update_score_droite, -1)
        self.plus_droite = Button(self.central_widget, " + ", self.update_score_droite, 1)

        # Zones d'affichage pour les scores
        self.ecran_gauche = ZoneAffichage(self.central_widget, font_size=100)
        self.ecran_droite = ZoneAffichage(self.central_widget, font_size=100)

        # Zones d'affichage pour les sets
        self.set_gauche = ZoneAffichage(self.central_widget)
        self.set_droite = ZoneAffichage(self.central_widget)

        # Résultats
        self.resultats_gauche = [ZoneAffichage(self.central_widget) for _ in range(5)]
        self.resultats_droite = [ZoneAffichage(self.central_widget) for _ in range(5)]

    def resizeEvent(self, event):
        """Gère le redimensionnement de la fenêtre."""
        width, height = self.width(), self.height()

        # Redimensionner l'image de fond
        self.background_label.setGeometry(0, 0, width, height)
        scaled_pixmap = self.pixmap.scaled(width, height, Qt.KeepAspectRatioByExpanding)
        self.background_label.setPixmap(scaled_pixmap)

        # Redimensionner et repositionner les widgets
        self.update_widget_positions(width, height)

    def update_widget_positions(self, width, height):
        """Met à jour les positions et tailles des widgets en fonction de la taille de la fenêtre."""
        # Boutons gauche
        self.moins_gauche.setGeometry(QRect(width * 0.1, height * 0.35, width * 0.05, height * 0.05))
        self.plus_gauche.setGeometry(QRect(width * 0.25, height * 0.35, width * 0.05, height * 0.05))

        # Boutons droite
        self.moins_droite.setGeometry(QRect(width * 0.7, height * 0.35, width * 0.05, height * 0.05))
        self.plus_droite.setGeometry(QRect(width * 0.85, height * 0.35, width * 0.05, height * 0.05))

        # Zones d'affichage des scores
        self.ecran_gauche.setGeometry(QRect(width * 0.1, height * 0.1, width * 0.2, height * 0.2))
        self.ecran_droite.setGeometry(QRect(width * 0.7, height * 0.1, width * 0.2, height * 0.2))

        # Zones des sets
        self.set_gauche.setGeometry(QRect(width * 0.35, height * 0.175, width * 0.075, height * 0.075))
        self.set_droite.setGeometry(QRect(width * 0.575, height * 0.175, width * 0.075, height * 0.075))

        # Résultats
        for i, (resultat_g, resultat_d) in enumerate(zip(self.resultats_gauche, self.resultats_droite)):
            y_offset = height * (0.3 + i * 0.1)
            resultat_g.setGeometry(QRect(width * 0.4, y_offset, width * 0.075, height * 0.075))
            resultat_d.setGeometry(QRect(width * 0.525, y_offset, width * 0.075, height * 0.075))

    def update_score_gauche(self, value):
        self.scoreGauche += value
        self.ecran_gauche.update_score(self.scoreGauche)
        self.check_set("gauche")

    def update_score_droite(self, value):
        self.scoreDroite += value
        self.ecran_droite.update_score(self.scoreDroite)
        self.check_set("droite")

    def check_set(self, side):
        if side == "gauche" and self.scoreGauche >= 25 and self.scoreGauche - self.scoreDroite >= 2:
            self.update_set_score("gauche")
        elif side == "droite" and self.scoreDroite >= 25 and self.scoreDroite - self.scoreGauche >= 2:
            self.update_set_score("droite")

    def update_set_score(self, side):
        if side == "gauche":
            self.scoreSetGauche += 1
            self.set_gauche.update_score(self.scoreSetGauche)
            self.resultats_gauche[self.nombreSet].update_score(self.scoreGauche)
            self.resultats_droite[self.nombreSet].update_score(self.scoreDroite)
        elif side == "droite":
            self.scoreSetDroit += 1
            self.set_droite.update_score(self.scoreSetDroit)
            self.resultats_gauche[self.nombreSet].update_score(self.scoreGauche)
            self.resultats_droite[self.nombreSet].update_score(self.scoreDroite)
        
        self.nombreSet += 1
        self.scoreGauche = 0
        self.scoreDroite = 0
        self.ecran_gauche.update_score(self.scoreGauche)
        self.ecran_droite.update_score(self.scoreDroite)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
