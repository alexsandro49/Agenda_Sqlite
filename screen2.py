import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

events_screen = QWidget()
events_screen.resize(500, 500)
events_screen.setWindowTitle("Agenda com PyQt6 + Sqlite")
events_screen.setStyleSheet("background-color: #22333b; color: #ffffff;")

btn1 = QPushButton("CRIAR", events_screen)
btn1.setGeometry(20, 10, 80, 30)
btn1.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

btn2 = QPushButton("EVENTOS", events_screen)
btn2.setGeometry(400, 10, 80, 30)
btn2.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

label_top = QLabel("EVENTOS", events_screen)
label_top.setGeometry(135, 10, 230, 30)
label_top.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
label_top.setStyleSheet("background-color: none; font-size: 22px; font-family: Arial, Verdana, sans-serif;")
