# Nama: Alysa Meliana
# NIM: F1D02310035
# Kelas: D

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Konversi Suhu")
        self.resize(400, 250)  

        self.setStyleSheet("background-color: #fff0f5;")  

        main_layout = QVBoxLayout()
        main_layout.setSpacing(8)

        judul = QLabel("KONVERSI SUHU")
        judul.setAlignment(Qt.AlignCenter)
        judul.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #d147a3;
            margin: 5px;
        """)
        main_layout.addWidget(judul)

        label_input = QLabel("Masukkan Suhu (dalam satuan celsius):")
        label_input.setStyleSheet("color: #a64d79; font-weight: bold;")
        main_layout.addWidget(label_input)

        self.input_suhu = QLineEdit()
        self.input_suhu.setPlaceholderText("Contoh: 100")
        self.input_suhu.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ffb6c1;
                border-radius: 5px;
                padding: 4px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #ff69b4;
            }
        """)
        main_layout.addWidget(self.input_suhu)

        tombol_layout = QHBoxLayout()

        self.btn_f = QPushButton("Fahrenheit")
        self.btn_f.setStyleSheet("""
            QPushButton {
                background-color: #ffb6c1;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff99aa;
            }
            QPushButton:pressed {
                background-color: #ff7f8f;
            }
        """)
        tombol_layout.addWidget(self.btn_f)

        self.btn_k = QPushButton("Kelvin")
        self.btn_k.setStyleSheet("""
            QPushButton {
                background-color: #ffb6c1;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff99aa;
            }
            QPushButton:pressed {
                background-color: #ff7f8f;
            }
        """)
        tombol_layout.addWidget(self.btn_k)

        self.btn_r = QPushButton("Reamur")
        self.btn_r.setStyleSheet("""
            QPushButton {
                background-color: #ffb6c1;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff99aa;
            }
            QPushButton:pressed {
                background-color: #ff7f8f;
            }
        """)
        tombol_layout.addWidget(self.btn_r)

        main_layout.addLayout(tombol_layout)

        self.hasil = QLabel("Hasil Konversi:")
        self.hasil.setStyleSheet("""
            background-color: #ffe0f0;
            padding: 8px;
            border-radius: 5px;
            color: #a64d79;
            font-weight: bold;
        """)
        self.hasil.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.hasil)

        self.setLayout(main_layout)

        self.btn_f.clicked.connect(self.konversi_fahrenheit)
        self.btn_k.clicked.connect(self.konversi_kelvin)
        self.btn_r.clicked.connect(self.konversi_reamur)

    def ambil_input(self):
        teks = self.input_suhu.text()
        if not teks:
            QMessageBox.warning(self, "Error", "Input tidak boleh kosong!")
            return None
        try:
            return float(teks)
        except:
            QMessageBox.warning(self, "Error", "Input harus berupa angka!")
            return None

    def konversi_fahrenheit(self):
        c = self.ambil_input()
        if c is not None:
            f = (c * 9/5) + 32
            self.hasil.setText(f"{c:.2f} Celsius = {f:.2f} Fahrenheit")

    def konversi_kelvin(self):
        c = self.ambil_input()
        if c is not None:
            k = c + 273.15
            self.hasil.setText(f"{c:.2f} Celsius = {k:.2f} Kelvin")

    def konversi_reamur(self):
        c = self.ambil_input()
        if c is not None:
            r = c * 4/5
            self.hasil.setText(f"{c:.2f} Celsius = {r:.2f} Reamur")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())
