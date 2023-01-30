import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

main_screen = QWidget()
main_screen.resize(500, 500)
main_screen.setWindowTitle("Agenda com PyQt6 + Sqlite")
main_screen.setStyleSheet("background-color: #22333b; color: #ffffff;")

btn1 = QPushButton("CRIAR", main_screen)
btn1.setGeometry(20, 10, 80, 30)
btn1.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

btn2 = QPushButton("EVENTOS", main_screen)
btn2.setGeometry(400, 10, 80, 30)
btn2.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

label_top = QLabel("DEFINA UM EVENTO", main_screen)
label_top.setGeometry(135, 10, 230, 30)
label_top.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
label_top.setStyleSheet("background-color: none; font-size: 22px; font-family: Arial, Verdana, sans-serif;")

label_titulo = QLabel("TÍTULO:", main_screen)
label_titulo.setGeometry(135, 120, 230, 30)
label_titulo.setStyleSheet("background-color: none; font-size: 22px; font-family: Arial, Verdana, sans-serif;")

line_edit = QLineEdit("", main_screen)
line_edit.setGeometry(135, 160, 230, 50)
line_edit.setStyleSheet("background-color: #ffffff; color: #22333b; font-size: 12px; border: 2px solid #ffffff; border-radius: 5px; font-family: Arial, Verdana, sans-serif;")

label_conteudo = QLabel("CONTEÚDO", main_screen)
label_conteudo.setGeometry(135, 210, 230, 50)
label_conteudo.setStyleSheet("background-color: none; font-size: 22px; font-family: Arial, Verdana, sans-serif;")

line_edit2 = QLineEdit("", main_screen)
line_edit2.setGeometry(135, 260, 230, 80)
line_edit2.setStyleSheet("background-color: #ffffff; color: #22333b; font-size: 12px; border: 2px solid #ffffff; border-radius: 5px; font-family: Arial, Verdana, sans-serif;")

btn3 = QPushButton("SALVAR", main_screen)
btn3.setGeometry(210, 360, 80, 30)
btn3.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")
