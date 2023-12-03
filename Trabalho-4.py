#VARIAVEIS GLOBAIS
lista_livro = []
id_global = 0

            #FIM VARIAVEIS GLOBAIS


        # INICIO FUNÇAO CADASTRAR LIVRO

def cadastrar_livro(id):
    print('Bem vindo ao MENU de cadastrar livro')  #MENU CADASTRAR LIVRO
    titulo = input('entre com o Título do livro:')
    autor = input('entre com o Autor do livro:')
    editora = input('entre com a Editora do livro:')
    dicionario_livro = {'id_global': id_global,
                        'Titulo': titulo,
                        'Autor': autor,
                        'Editora': editora}
    lista_livro.append(dicionario_livro.copy()) #COPIA O LIVRO CADASTRADO PARA O DICIONARIO

            # FIM DA FUNÇÃO CADASTRAR




            # FUNÇÃO CONSULTAR LIVRO

def consultar_livro():
    print('Bem vindo ao MENU de consultar livro')       #MENU CONSULTAR LIVRO
    while True:
        print('1. Consultar Todos')
        print('2. Consultar por ID')
        print('3. Consultar por Autor')
        print('4. Retornar ao menu')
        opcao_consultar= input('>>')
        if opcao_consultar == '1':
            print('voce escolheu a função de consultar todos os livros')

            for livros in lista_livro:                      #livros vai varrer toda lista de livros
                print('-------------------------------')
                for key,value in livros.items():            #VARRER TODOS OS CONJUNTOS CHAVE E VALOR NO DICIONARIO PRODUTO
                    print('{}:{}'.format(key,value))
                    print('----------------------------')




        elif opcao_consultar == '2':
            print('Você escolheu a função de consultar livros por ID') #MENU CONSULTAR LIVROS POR ID
            valor_id = int(input('Digite o ID:'))
            for livro in lista_livro:
                if livro['id_global'] == valor_id:
                    print('------------------------------')
                    for key, value in livro.items():
                        print('{}: {}'.format(key, value))
                    print('----------------------------')
                    return
            print('Livro não encontrado.')  #MENSAGEM CASO O PROGRAMA NAO ENCONTRE O LIVRO BUSCADO


        elif opcao_consultar =='3':
            print('Você escolheu a função de consultar livros por Autor') #MENU CONSULTAR LIVROS POR AUTOR
            autor = input('Digite o Autor:')
            for livros in lista_livro:
                if livros['Autor'] == autor:
                    print('-------------------------------')
                    for key, value in livros.items():
                        print('{}: {}'.format(key, value))
                    print('----------------------------')
        elif opcao_consultar == '4':
            return  # SAI DA FUNÇAO CONSULTAR PRODUTO E VOLTA PARA O MAIN
        else:
            print('Opção Invalida!tente novamente!') #MENSAGEM CASO O USUARIO DIGITE UMA OPÇAO DIFERENTE
            continue                                 #RETORNA AO INICIO DO WHILE



        #FIM FUNÇÃO CONSULTAR LIVRO

            # INICIO FUNÇÃO REMOVER LIVRO
def remover_livro():
    print('Bem vindo ao MENU de remover livro')      #MENSAGEM MENU REMOÇAO DE LIVROS
    valor_desejado = int(input('entre com o ID do produto que deseja remover: '))
    for livros in lista_livro:
        if livros['id_global'] == valor_desejado:
            lista_livro.remove(livros)
            print('Livro removido do sistema!')  #MENSAGEM CONFIRMANDO A REMOÇAO DE UM LIVRO NA BIBLIOTECA


                #PROGRAMA PRINCIPAL



print('Bem vindo a Livraria de FELIPE AUGUSTO FIALHO \n')  #MENSAGEM DE BOAS VINDAS
while True:

    print('Digite a Opção Desejada:\n')
    print('1 - Cadastrar Livro')
    print('2. Consultar Livro')                             #OPCOES DISPONIVEIS NO SISTEMA
    print('3. Remover Livro')
    print('4. Encerrar Programa')

    servico = input('>>')

    if servico == '1':
        id_global = id_global + 1
        cadastrar_livro(cadastrar_livro)

    elif servico == '2':
        consultar_livro()

    elif servico == '3':
        remover_livro()

    elif servico == '4':
        break                            # ENCERRA O PROGRAMA
    else:
        print('Opção invalida digite uma opção entre(1,2,3 ou 4)') #CASO O USUARIO DIGITE ALGO DIFERENTE DAS OPCOES
        continue                                                   #E REINICIA O WHILE



#FIM PROGRAMA PRINCIPAL
