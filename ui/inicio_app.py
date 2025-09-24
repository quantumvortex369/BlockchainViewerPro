from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor

class InicioApp(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
            QLabel#title {
                font-size: 48px;
                font-weight: bold;
                color: #000000;
                qproperty-alignment: 'AlignCenter';
            }
            QLabel#subtitle {
                font-size: 18px;
                color: #000000;
                qproperty-alignment: 'AlignCenter';
            }
            QPushButton {
                background-color: transparent;
                color: #000000;
                border: none;
                padding: 15px 30px;
                font-size: 20px;
                font-weight: bold;
                min-width: 200px;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
            QPushButton:pressed {
                color: #333333;
            }
        """)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Title and Subtitle
        title = QLabel("BLOCKCHAIN VIEWER PRO")
        title.setObjectName("title")
        
        subtitle = QLabel("VISUALIZA TRANSACCIONES DE LA BLOCKCHAIN EN TIEMPO REAL")
        subtitle.setObjectName("subtitle")

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        button_layout.setAlignment(Qt.AlignCenter)

        start_btn = QPushButton("INICIAR")
        exit_btn = QPushButton("SALIR")

        start_btn.clicked.connect(self.go_to_viewer)
        exit_btn.clicked.connect(QApplication.quit)

        button_layout.addWidget(start_btn)
        button_layout.addWidget(exit_btn)

        # Add widgets to main layout
        main_layout.addStretch(1)
        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)
        main_layout.addSpacing(50)
        main_layout.addLayout(button_layout)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

    def go_to_viewer(self):
        self.main_app.setCurrentIndex(1)
