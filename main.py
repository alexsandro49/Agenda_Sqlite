import sys
import screen1
import screen2
import db_connection
from PyQt6.QtWidgets import QApplication


def listar_eventos():
    screen1.main_screen.close()
    screen2.events_screen.show()

def criar_eventos():
    screen2.events_screen.close()
    screen1.main_screen.show()


app = QApplication(sys.argv)

screen1.btn2.clicked.connect(listar_eventos)
screen2.btn1.clicked.connect(criar_eventos)
screen1.btn3.clicked.connect(db_connection.salvar_dados)

screen1.main_screen.show()
app.exec()
