import sqlite3
import screen1

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
        screen1.line_edit2.clear()
        
        print("Banco modificado com sucesso!")
    except sqlite3.Error as erro:
        print(f"Houve um erro: {erro}")

def mostrar_dados():
    banco = sqlite3.connect('banco_de_dados.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM eventos")  
    return cursor.fetchall()
