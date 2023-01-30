import sys
import sqlite3
import screen1
import screen2
from PyQt6.QtWidgets import QApplication

def salvar_dados():
    try:
        banco = sqlite3.connect('banco_de_dados.db')
        cursor = banco.cursor()

        titulo = screen1.line_edit.text()
        conteudo = screen1.line_edit2.text()
        
        cursor.execute(f"INSERT INTO eventos VALUES('{titulo}', '{conteudo}');")

        banco.commit()
        banco.close()

        screen1.line_edit.clear()
        screen2.line_edit2.clear()
        
        print("Banco modificado com sucesso!")
    except sqlite3.Error as erro:
        print(f"Houve um erro: {erro}")

def mostrar_dados():
    banco = sqlite3.connect('banco_de_dados.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM eventos")  
    print(cursor.fetchall())

def listar_eventos():
    screen1.main_screen.close()
    screen2.events_screen.show()

def criar_eventos():
    screen2.events_screen.close()
    screen1.main_screen.show()


app = QApplication(sys.argv)

screen1.btn2.clicked.connect(listar_eventos)
screen2.btn1.clicked.connect(criar_eventos)
screen1.btn3.clicked.connect(salvar_dados)

screen1.main_screen.show()
app.exec()
