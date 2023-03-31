from locadoracg import *
from operacoesbd import *

conexao = abrirBancoDados("localhost","root","1546490","locadora")

opcao = 6


while opcao != 5:
    print(30 * "=")
    print('Locadora Colombiana')
    print('1) Lista')
    print('2) Inserir')
    print('3) Pesquisar Codigo')
    print('4) Excluir')
    print('5) Sair')
    print(30 * "=")
    opcao = int(input('Escolha umas das opções: '))

    if opcao == 1:

        listarFilmes(conexao)

    elif opcao == 2:

        inserirFilme(conexao)

    elif opcao == 3:

        pesquisarCodigo(conexao)


    elif opcao == 4:

        excluirFilme(conexao)


encerrarBancoDados()