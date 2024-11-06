import sqlite3
import PySimpleGUI as sg

# Conectando ao banco de dados ou criando-o caso ele não exista
conexão = sqlite3.connect('meu_banco.db')
cursor = conexão.cursor()

# Criando a tabela, se ela ainda não existir





def inserção_de_dados( pessoas, nome, data):
    # Conectando ao banco de dados
    conexão = sqlite3.connect('meu_banco.db')
    cursor = conexão.cursor()

    # Cria a tabela se não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pessoas INT,
        nome TEXT NOT NULL,
        data DATE NOT NULL
    )
    ''')

    # Insere os dados na tabela
    cursor.execute('''
        INSERT INTO reservas (pessoas, nome, data)
        VALUES (?, ?, ?)
    ''', ( pessoas, nome, data))

   
    

    # Commitando as alterações e fechando a conexão
    conexão.commit()
    conexão.close()





def alimentando_aplicação():

    # Conectando ao banco de dados ou criando-o caso ele não exista
    conexão = sqlite3.connect('meu_banco.db')
    cursor = conexão.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pessoas INT,
        nome TEXT NOT NULL,
        data DATE NOT NULL
    )
    ''')

    cursor.execute('SELECT * FROM reservas')
    dados = cursor.fetchall()
   

    return dados


def atualização():
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

""" 







cursor.execute('DROP TABLE IF EXISTS reservas')
conexão.commit()

"""