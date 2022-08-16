
from numpy import append


def tamanho_list():
    '''
    Função
    ----------
    Retorna o tamanho desejado pelo usuario para a criação da lista

    Parâmetros
    ----------
    Sem passagem de parâmentros

    Retorno
    ----------
    Retorno: int
    Descrição: Retorna o tamanho desejado
    '''
    tam = int(input("Digite o tamanho que deseja da lista: "))
    return tam

def criar_list(tamanho):
    '''
    Função
    ----------
    Criar uma lista com base no tamanho passado pelo usúario

    Parâmetros
    ----------
    tamanho: int
    Descrição: Tamanho da lista

    Retorno
    ----------
    Retorno: list
    Descrição: Retorna a lista com o tamanho passado pelo usúario
    '''
    lista = list(range(tamanho))
    return lista

def popular(lista):
    '''
    Função
    ----------
    Popular a lista com os números que o usúario digitar, conforme o tamanho da lista

    Parâmetros
    ----------
    lista: list
    Descrição: a Lista já com o tamanho

    Retorno
    ----------
    Retorno: list
    Descrição: Retorna a lista populada com os dados já inseridos pelo usúario
    '''
    i = 0
    while(i < len(lista)):
        lista [i] = int(input(f"Digite o {i+1}° número para colocar na lista:"))
        i += 1
    print("\n")
    return lista

def imprimir(lista):
    i = 0
    while(i < len(lista)):
        print(f"O {i + 1}° Elemento é: {lista[i]}")
        i += 1


def pares(lista):
    par = []
    i = 0
    while(i < len(lista)):
        if(lista[i] % 2 == 0):
            par.append(lista[i])
        i += 1
    return par




def main():
    '''
    Função
    ----------
    Imprimir todos os números da lista

    Parâmetros
    ----------
    Sem passagem de parâmentros

    Retorno
    ----------
    Sem retorno
    '''
    tamanho = tamanho_list()
    lista = criar_list(tamanho)
    popular(lista)
    imprimir(lista)
    print("------------------")
    

main()

