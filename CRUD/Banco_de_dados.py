import sqlite3
import PySimpleGUI as sg

# Conexão com o banco ---------------------------------------------------
conexão = sqlite3.connect('meu_banco.db')
cursor = conexão.cursor()


# Adicionando dados do programa ao SQL ---------------------------------------------
def inserção_de_dados(a, b, c, d):

    conexão = sqlite3.connect('meu_banco.db')
    cursor = conexão.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quntidade_pessoas INT,
        data DATE NOT NULL,
        horario TEXT NOT NULL)''')

    cursor.execute('''
        INSERT INTO reservas (nome, quntidade_pessoas, data, horario)
        VALUES (?, ?, ?, ?)
    ''', ( a, b, c, d))
    print("Salvo no banco")
    
    conexão.commit()
    conexão.close()




# Alimentando aplicação com dados do banco ---------------------------------------
def alimentando_aplicação():

    conexão = sqlite3.connect('meu_banco.db')
    cursor = conexão.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quntidade_pessoas INT,
        data DATE NOT NULL,
        horario TEXT NOT NULL)''')

    cursor.execute('SELECT * FROM reservas')
    dados = cursor.fetchall()
   

    return dados



def deleção_no_banco(id):

    conexão = sqlite3.connect('meu_banco.db')
    cursor = conexão.cursor()



    cursor.execute('DELETE FROM reservas WHERE id = ?', (id,))

    conexão.commit()
    conexão.close()

"""

cursor.execute('DROP TABLE IF EXISTS reservas')
conexão.commit()

"""