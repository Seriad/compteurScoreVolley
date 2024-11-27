from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class ZoneAffichage(QLabel):
    def __init__(self, parent, font_size=36):
        super().__init__(parent)

        # Style par défaut
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: white; border: 1px solid black;")
        self.font_size = font_size
        self.score = 0
        self.update_score(self.score)

    def update_score(self, score):
        """Met à jour le score affiché."""
        self.score = score
        self.setText(str(score))
        self.adjust_font()

    def adjust_font(self):
        """Ajuste dynamiquement la taille de la police en fonction des dimensions du widget."""
        width, height = self.width(), self.height()
        font_size = min(width, height) // 3
        font = QFont("Arial", font_size)
        self.setFont(font)
