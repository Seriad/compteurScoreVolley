from PySide6.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self, parent, text, callback, value):
        super().__init__(text, parent)
        self.callback = callback
        self.value = value

        # Style du bouton
        self.setStyleSheet("""
            QPushButton {
                background-color: lightgray;
                border: 1px solid gray;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: darkgray;
            }
        """)

        # Connecter le clic à l'action
        self.clicked.connect(self.on_click)

    def on_click(self):
        """Action exécutée lors du clic."""
        self.callback(self.value)
