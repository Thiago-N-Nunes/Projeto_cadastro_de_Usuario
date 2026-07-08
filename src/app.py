import main
import os

print('=' * 35)
print('BEM VINDO AO SISTEMA DE CADASTRO')
print('=' * 35)
escolha = int(input("""O que deseja fazer?
1. Cadastrar
2. Consultar
3. Atualizar
4. Sair\n"""))

match escolha:
    case 1:
        main.cadastrar()
    case 2:
        main.consultar()
    case 3:
        main.alterar()
    case 4:
        os.system('cls')
        print('Até a próxima!')

