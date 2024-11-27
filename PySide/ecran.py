from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class Screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setup_label(self, text, font_size=20):
        """Créer un label générique."""
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", font_size))
        label.setStyleSheet("color: white;")
        return label
