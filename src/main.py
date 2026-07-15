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
def adicionar_usuario():
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
        
def mostrar():
    usuarios = cursor.execute("SELECT nome, idade, email FROM usuarios ORDER BY nome ASC")
    usuarios = cursor.fetchall()
    print(usuarios)
    conexao.commit()

def maiores():
    maior_idade = cursor.execute("SELECT nome, idade, email FROM usuarios WHERE idade > 18")
    maior_idade = cursor.fetchall()
    print(maior_idade)

def menores():
    menor_idade = cursor.execute("SELECT nome, idade, email FROM usuarios WHERE idade < 18")
    menor_idade = cursor.fetchall()
    print(menor_idade)
opcao = input(""" Oque deseja fazer?
1. Adicionar usuario
2. Exibir usuario
2.1. Exibir Usuarios maiores de idade
2.2. Exibir Usuarios menores de idade
""")
match opcao:
    case "1":
        adicionar_usuario()
    case "2":
        mostrar()
    case "2.1":
        maiores()
    case "2.2":
        menores()