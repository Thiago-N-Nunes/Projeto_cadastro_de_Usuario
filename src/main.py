import sqlite3
import os
from random import randint
# Conexão com o banco de dados SQLite
conexao = sqlite3.connect('./src/users.db')
cursor = conexao.cursor()

#Criando a tabela de usuários caso não exista
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL
            )""")

# Loop para cadastro de usuários, se o usuário digitar um nome vazio, o cadastro é finalizado
def cadastrar():
    while True:
        nome = input('Digite o nome: ')   
        idade = int(input('Digite sua idade: '))
        email  = input('Digite seu email: ')
        cursor.execute("INSERT INTO usuarios(nome,idade,email) VALUES(?,?,?)", (nome,idade,email))
        conexao.commit()
        escolha = input('Deseja continuar? [S/N]')
        escolha = escolha.upper() 
        if escolha == 'N':
            os.system('cls')
            print('Cadastro finalizado!')    
            break
       

def consultar():
    cursor.execute("SELECT * FROM usuarios ORDER BY nome ASC")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        id, nome, idade, email = usuario
        print(usuario)
    conexao.commit()

def de_maior():
    cursor.execute("SELECT * FROM usuarios WHERE idade > 18")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        id, nome, idade, email = usuario
    print(usuario)
    conexao.commit()

def de_menor():
    cursor.execute("SELECT * FROM usuarios WHERE idade < 18")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        id, nome, idade, email = usuario
        print(usuario)
    conexao.commit()
