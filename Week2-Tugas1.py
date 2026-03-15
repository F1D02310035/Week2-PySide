# Nama: Alysa Meliana
# NIM: F1D02310035
# Kelas: D

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox
)

class FormBiodata(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setFixedSize(350, 570)  

        main_layout = QVBoxLayout()
        main_layout.setSpacing(6)

        self.nama = QLineEdit()
        self.nama.setPlaceholderText("Masukkan Nama Lengkap Anda!")

        self.univ = QLineEdit()
        self.univ.setPlaceholderText("Universitas")

        self.prodi = QLineEdit()
        self.prodi.setPlaceholderText("Program Studi")

        self.kelas = QLineEdit()
        self.kelas.setPlaceholderText("Contoh: Informatika-D")

        self.nim = QLineEdit()
        self.nim.setPlaceholderText("Masukkan NIM Anda!")

        self.kelamin = QComboBox()
        self.kelamin.addItems(["Laki-laki", "Perempuan"])

        self.btn_tampil = QPushButton("Tampilkan")
        self.btn_reset = QPushButton("Reset")

        self.btn_tampil.setObjectName("btnTampil")
        self.btn_reset.setObjectName("btnReset")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_tampil)
        button_layout.addWidget(self.btn_reset)

        self.hasil = QLabel("DATA BIODATA")
        self.hasil.setWordWrap(True)
        self.hasil.setObjectName("hasilbox")

        main_layout.addWidget(QLabel("Nama Lengkap:"))
        main_layout.addWidget(self.nama)

        main_layout.addWidget(QLabel("Universitas:"))      
        main_layout.addWidget(self.univ)

        main_layout.addWidget(QLabel("Program Studi:"))    
        main_layout.addWidget(self.prodi)

        main_layout.addWidget(QLabel("Kelas:"))            
        main_layout.addWidget(self.kelas)

        main_layout.addWidget(QLabel("NIM:"))             
        main_layout.addWidget(self.nim)

        main_layout.addWidget(QLabel("Jenis Kelamin:"))
        main_layout.addWidget(self.kelamin)

        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.hasil)

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget {
                font-size: 12px;
            }

            QLineEdit {
                background-color: #ffdbd1;
                padding: 4px;
                border-radius: 7px;
                border: 1px solid #999;
            }

            QLabel {
                margin-top: 2px;
            }

            QPushButton {
                padding: 4px;
                border-radius: 7px;
                font-weight: bold;
            }

            QPushButton#btnTampil {
                background-color: #4da6ff;
                color: white;
            }

            QPushButton#btnTampil:hover {
                background-color: #1a8cff;
            }

            QPushButton#btnReset {
                background-color: #d9d9d9;
                color: black;
            }

            QPushButton#btnReset:hover {
                background-color: #bfbfbf;
            }

            QLabel#hasilbox {
                background-color: #ffdbd1;
                padding: 8px;
                border-radius: 7px;
                border: 1px solid #999;
            }
        """)

        self.btn_tampil.clicked.connect(self.tampilkan_data)
        self.btn_reset.clicked.connect(self.reset_form)

    def tampilkan_data(self):
        nama = self.nama.text()
        nim = self.nim.text()
        kelas = self.kelas.text()
        prodi = self.prodi.text()        
        univ = self.univ.text()           
        kelamin = self.kelamin.currentText()

        if nama == "" or nim == "" or kelas == "" or prodi == "" or univ == "":
            QMessageBox.warning(self, "Peringatan", "Harap mengisi semua field!")
            return

        data = f"""
DATA BIODATA

Nama: {nama}
Universitas: {univ}
Program Studi: {prodi}
Kelas: {kelas}
NIM: {nim}
Jenis Kelamin: {kelamin}
"""
        self.hasil.setText(data)

    def reset_form(self):
        self.nama.clear()
        self.nim.clear()
        self.kelas.clear()
        self.prodi.clear()      
        self.univ.clear()
        self.kelamin.setCurrentIndex(0)
        self.hasil.setText("DATA BIODATA")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())
