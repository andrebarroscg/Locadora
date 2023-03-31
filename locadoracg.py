from operacoesbd import *

conexao = abrirBancoDados("localhost","root","1546490","locadora")






def listarFilmes(conexao):



        consultar = "select *from filmes"
        filmes = listarBancoDados(conexao,consultar)

        for filme in filmes:
            print("Codigo", filme[0],"Título",filme[1],"Sinops",filme[2],"Ano Lançamento",filme[3])



def inserirFilme(conexao):
    titulo = input('Digite o nome do novo filme: ')
    sinops = input('Digite a sinops do novo filme: ')
    anoLancamento= int(input("Digite o ano de Lanaçamento do Filme: "))

    inserir = "insert into filmes (titulo, sinops,ano_lancamento)values(%s,%s,%s)"
    dados = (titulo,sinops,anoLancamento)
    insertNoBancoDados(conexao,inserir,dados)
    print('Filme cadastrado com sucesso!')

def pesquisarCodigo(conexao):



        codigo = input('Digite o codigo do filme: ')

        consultaPesquisar = 'select * from filmes where codigoFilme = ' + codigo

        listaDeFilmes = listarBancoDados(conexao, consultaPesquisar)

        if len(listaDeFilmes) == 0:
            print('Codigo não existente! ')
        else:
            for item in listaDeFilmes:
                print(item)




def excluirFilme(conexao):


    codigo = int(input('Digite o codigo do filme '))
    consultaExclusao = 'delete from filmes where codigoFilme = %s '
    dados = (codigo,)
    linhasExcluidas = excluirBancoDados(conexao,consultaExclusao,dados)

    if linhasExcluidas == 0:
        print("codigo nao existente! ")
    else:
        print("Filme excluido com sucesso!")




