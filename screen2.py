import sys
import db_connection
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt

def update_table():
    data = db_connection.show_data()

    if len(data) <= 12:
        data_table.setRowCount(12)
    else:
        data_table.setRowCount(len(data))

    #data = data[::-1]
    for i in range(0, len(data)):
        data_table.setItem(i, 0, QTableWidgetItem(data[i][0]))
        data_table.setItem(i, 1, QTableWidgetItem(data[i][1]))


def delete_data():
    data = db_connection.show_data()  
    linha = data_table.currentRow()
    data_table.removeRow(linha)
    titulo = data[linha][0]
    db_connection.delete_data(titulo)

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

btn3 = QPushButton("INVERTER", events_screen)
btn3.setGeometry(310, 460, 80, 30)
btn3.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

btn4 = QPushButton("DELETAR", events_screen)
btn4.setGeometry(400, 460, 80, 30)
btn4.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

label_top = QLabel("EVENTOS", events_screen)
label_top.setGeometry(135, 10, 230, 30)
label_top.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
label_top.setStyleSheet("background-color: none; font-size: 22px; font-family: Arial, Verdana, sans-serif;")

data_table = QTableWidget(events_screen)
data_table.setGeometry(20, 60, 460, 390)
data_table.setColumnCount(2)
data_table.setHorizontalHeaderLabels(["TÍTULO", "CONTEÚDO"])
data_table.setColumnWidth(0, 140)
data_table.setColumnWidth(1, 320)

update_table()