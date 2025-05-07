import sys
import requests
import time
import csv
import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QHeaderView, QHBoxLayout, QCheckBox, QPushButton,
    QMessageBox, QStackedWidget
)
from PyQt5.QtCore import QTimer, Qt

MAX_ROWS = 50

class InicioApp(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: white;
                text-decoration: underline;
            }
            QPushButton {
                background-color: #3b3b5c;
                color: white;
                border-radius: 5px;
                padding: 15px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #4f4f70;
            }
            QWidget {
                background-color: #000000;
            }
        """)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Blockchain Viewer PRO")
        title.setAlignment(Qt.AlignCenter)
        start_btn = QPushButton("Iniciar Visualizador")
        exit_btn = QPushButton("Salir")

        start_btn.clicked.connect(self.ir_a_visualizador)
        exit_btn.clicked.connect(QApplication.quit)

        layout.addWidget(title)
        layout.addSpacing(30)
        layout.addWidget(start_btn)
        layout.addWidget(exit_btn)
        self.setLayout(layout)

    def ir_a_visualizador(self):
        self.main_app.setCurrentIndex(1)


class BlockchainViewer(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Filtros
        self.filter_layout = QHBoxLayout()
        self.filter_label = QLabel("Filtrar transacciones por:")
        self.checkbox_all = QCheckBox("Todas")
        self.checkbox_whales = QCheckBox("Ballenas")
        self.checkbox_fee = QCheckBox("Fee Bajo")
        self.checkbox_mixers = QCheckBox("Mixers")
        self.checkbox_all.setChecked(True)

        self.filter_layout.addWidget(self.filter_label)
        self.filter_layout.addWidget(self.checkbox_all)
        self.filter_layout.addWidget(self.checkbox_whales)
        self.filter_layout.addWidget(self.checkbox_fee)
        self.filter_layout.addWidget(self.checkbox_mixers)
        self.layout.addLayout(self.filter_layout)

        # Botones
        self.control_layout = QHBoxLayout()
        self.start_button = QPushButton("Empezar")
        self.stop_button = QPushButton("Apagar")
        self.export_button = QPushButton("Exportar CSV")
        self.back_button = QPushButton("Volver al inicio")
        self.control_layout.addWidget(self.start_button)
        self.control_layout.addWidget(self.stop_button)
        self.control_layout.addWidget(self.export_button)
        self.control_layout.addWidget(self.back_button)
        self.layout.addLayout(self.control_layout)

        self.start_button.clicked.connect(self.start_fetching)
        self.stop_button.clicked.connect(self.stop_fetching)
        self.export_button.clicked.connect(self.export_to_csv)
        self.back_button.clicked.connect(self.volver_al_inicio)

        # Tabla
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Hash", "Valor (BTC)", "Fee (BTC)", "Hora"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.fetch_real_transactions)

        # Estilo
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
                color: #ffffff;
                font-family: Arial, sans-serif;
            }
            QPushButton {
                background-color: #3b3b5c;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #4f4f70;
            }
            QCheckBox {
                color: #ffffff;
                font-size: 14px;
            }
            QTableWidget {
                background-color: #2e2e47;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QTableWidget::item {
                background-color: #3b3b5c;
            }
        """)

    def start_fetching(self):
        self.timer.start(2000)

    def stop_fetching(self):
        self.timer.stop()

    def volver_al_inicio(self):
        self.stop_fetching()
        self.table.setRowCount(0)
        self.main_app.setCurrentIndex(0)

    def get_active_filters(self):
        if self.checkbox_all.isChecked():
            return ["Todas"]
        filters = []
        if self.checkbox_whales.isChecked():
            filters.append("Ballenas")
        if self.checkbox_fee.isChecked():
            filters.append("Fee Bajo")
        if self.checkbox_mixers.isChecked():
            filters.append("Mixers")
        return filters

    def fetch_real_transactions(self):
        filters = self.get_active_filters()

        try:
            response = requests.get("https://mempool.space/api/mempool/recent")
            if response.status_code != 200:
                print("Error en la respuesta de la API:", response.status_code)
                return

            transactions = response.json()
            transactions_to_add = []

            for tx in transactions:
                txid = tx.get("txid", "")
                value_btc = round(tx.get("value", 0) / 1e8, 8)
                fee_btc = round(tx.get("fee", 0) / 1e8, 8)
                timestamp = time.strftime("%H:%M:%S")

                if "Todas" not in filters:
                    if "Ballenas" in filters and value_btc < 10:
                        continue
                    if "Fee Bajo" in filters and fee_btc > 0.0005:
                        continue
                    if "Mixers" in filters:
                        continue

                transactions_to_add.append((txid, value_btc, fee_btc, timestamp))

            self.animate_transactions(transactions_to_add)

        except Exception as e:
            print("Error al obtener datos reales:", e)

    def animate_transactions(self, transactions):
        if not transactions:
            return

        txid, value_btc, fee_btc, timestamp = transactions.pop(0)

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(txid))
        self.table.setItem(row_position, 1, QTableWidgetItem(str(value_btc)))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(fee_btc)))
        self.table.setItem(row_position, 3, QTableWidgetItem(timestamp))

        if self.table.rowCount() > MAX_ROWS:
            self.table.removeRow(0)

        self.table.scrollToBottom()
        QTimer.singleShot(100, lambda: self.animate_transactions(transactions))

    def export_to_csv(self):
        try:
            filters = self.get_active_filters()

            # Obtener la fecha y hora actual para crear un nombre único
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"transacciones_filtradas_{timestamp}.csv"
            
            print("Exportando CSV...")  # Agregar mensaje de confirmación
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Hash", "Valor (BTC)", "Fee (BTC)", "Hora"])

                for row in range(self.table.rowCount()):
                    txid = self.table.item(row, 0)
                    value_btc = self.table.item(row, 1)
                    fee_btc = self.table.item(row, 2)
                    timestamp = self.table.item(row, 3)

                    if None in (txid, value_btc, fee_btc, timestamp):
                        continue

                    txid_text = txid.text()
                    value_btc_text = value_btc.text()
                    fee_btc_text = fee_btc.text()
                    timestamp_text = timestamp.text()

                    if "Todas" not in filters:
                        if "Ballenas" in filters and float(value_btc_text) < 10:
                            continue
                        if "Fee Bajo" in filters and float(fee_btc_text) > 0.0005:
                            continue
                        if "Mixers" in filters:
                            continue

                    writer.writerow([txid_text, value_btc_text, fee_btc_text, timestamp_text])

            print(f"Archivo CSV exportado: {filename}")  # Confirmar exportación

            self.show_message("Éxito", f"CSV exportado: {filename}", QMessageBox.Information)

        except Exception as e:
            print("Error al exportar CSV:", e)
            self.show_message("Error", "Hubo un problema al exportar a CSV.", QMessageBox.Critical)

    def show_message(self, title, message, icon):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()


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
