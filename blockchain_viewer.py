from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, 
    QHeaderView, QHBoxLayout, QCheckBox, QPushButton, QMessageBox
)
from PyQt5.QtCore import QTimer
from constants import MAX_ROWS
from api.mempool import fetch_transactions
from utils.exporter import export_to_csv

class BlockchainViewer(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Filters
        self.setup_filters()

        # Buttons
        self.setup_buttons()

        # Table
        self.setup_table()

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_transactions)

        # Style
        self.apply_styles()

    def setup_filters(self):
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

    def setup_buttons(self):
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
        self.export_button.clicked.connect(self.handle_export)
        self.back_button.clicked.connect(self.go_to_home)

    def setup_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Hash", "Valor (BTC)", "Fee (BTC)", "Hora"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

    def apply_styles(self):
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

    def go_to_home(self):
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

    def update_transactions(self):
        filters = self.get_active_filters()
        transactions = fetch_transactions(filters)
        self.animate_transactions(transactions)

    def animate_transactions(self, transactions):
        if not transactions:
            return

        tx = transactions.pop(0)
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(tx['txid']))
        self.table.setItem(row_position, 1, QTableWidgetItem(str(tx['value_btc'])))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(tx['fee_btc'])))
        self.table.setItem(row_position, 3, QTableWidgetItem(tx['timestamp']))

        if self.table.rowCount() > MAX_ROWS:
            self.table.removeRow(0)

        self.table.scrollToBottom()
        QTimer.singleShot(100, lambda: self.animate_transactions(transactions))

    def handle_export(self):
        filters = self.get_active_filters()
        filename, error = export_to_csv(self.table, filters)
        if error:
            self.show_message("Error", f"Hubo un problema al exportar a CSV: {error}", QMessageBox.Critical)
        else:
            self.show_message("Éxito", f"CSV exportado: {filename}", QMessageBox.Information)

    def show_message(self, title, message, icon):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()
