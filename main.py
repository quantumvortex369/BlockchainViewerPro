import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from ui.inicio_app import InicioApp
from ui.blockchain_viewer import BlockchainViewer

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.inicio = InicioApp(self)
        self.visualizador = BlockchainViewer(self)
        self.addWidget(self.inicio)
        self.addWidget(self.visualizador)
        self.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.setWindowTitle("Blockchain Viewer PRO")
    main_app.resize(800, 500)
    main_app.show()
    sys.exit(app.exec_())
