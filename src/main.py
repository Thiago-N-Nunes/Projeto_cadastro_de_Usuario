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
while True:
    nome = input('Digite o nome: ')   
    if len(nome) == 0:
        os.system('cls')
        print('Cadastro finalizado!')
        break
    idade = int(input('Digite sua idade: '))
    email  = input('Digite seu email: ')
    cursor.execute("INSERT INTO usuarios(nome,idade,email) VALUES(?,?,?)", (nome,idade,email))
conexao.commit()        

def gerador_de_id():
    #gera um numero aleatorio de 1 a 999
    return str(randint(0,999))

def criar_id_final():
    #gera um numero aleatorio de 1 a 999
    nomes = cursor.execute("SELECT nome FROM usuarios")
    nomes = nomes.fetchall()
    nomes = list(nomes)
    print(nomes)
    
    for i in range(len(nomes)):
        id_gerado

    
