import main
import os

print('=' * 35)
print('BEM VINDO AO SISTEMA DE CADASTRO')
print('=' * 35)
escolha = float(input("""O que deseja fazer?
1. Cadastrar
2. Mostrar todos (A - Z)
2.1. Mostrar alunos de maior
2.2. Mostrar alunos de menor
"""))

match escolha:
    case 1:
        main.cadastrar()
    case 2:
        main.consultar()
    case 2.1:
        main.de_maior()
    case 2.2:
        main.de_menor()