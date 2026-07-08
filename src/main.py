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
    usuarios = cursor.execute("SELECT * FROM usuarios")
    usuarios = usuarios.fetchall()
    id, nome, idade, email = usuarios
    print('CONSULTAR')
    consultado = int(input("""Qual seria o interesse da consulta?
1. NOME
2. IDADE
3. EMAIL\n"""))
    match consultado:
        case 1:
            print('.' + nome)
        case 2:
            print()
def alterar():
    ...
    
