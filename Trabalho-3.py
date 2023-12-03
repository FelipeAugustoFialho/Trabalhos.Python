# Início da função escolha_servico():
def escolha_servico():
    print('--------SERVIÇOS---------')            #MENU SERVIÇOS
    print('Digitação               | dig')
    print('Impressão Colorida      | ico')
    print('Impressão Preto e Branco| ibo')
    print('Fotocópia               | fot')
    print('--------------------Menu 1 de 3 - Escolha o Serviço Desejado--------------------')
    while True:
        servico = input('Digite o serviço desejado: ')
        if servico != 'dig' and servico!= 'ico' and servico!= 'ibo' and servico!= 'fot':
            print('Você selecionou um serviço inválido! Tente novamente!') #SE O USUARIO DIGITAR ALGO INVALIDO
            continue                                            #RETORNA AO INICIO DO WHILE
        else:
            return servico

# Fim da função escolha_servico


# Início da função num_pagina():
def num_pagina(servico):
    print('--------------------Menu 2 de 3 - Quantidade de Serviço--------------------')
    while True:
        qtd = int(input('Qual a quantidade do serviço: '))

        desconto = 0  # Inicia o desconto como 0
        if qtd < 10:
            desconto = 0

        elif qtd >= 10 and qtd < 100:
            desconto = 10 / 100

        elif qtd >= 100 and qtd < 1000:
            desconto = 15 / 100

        elif qtd >= 1000 and qtd <= 9999:
            desconto = 20 / 100

        elif qtd >= 10000:
            # CASO O USUARIO DIGITE UMA QUANTIDADE ACIMA DA PERMITIDA

            print('Não aceitamos pedidos nessa quantidade, por favor tente uma quantidade menor')
            continue   # RETORNA AO INICIO DO WHILE

        if servico == 'dig':
            preco_pagina = 0.10
        elif servico == 'ico':
            preco_pagina = 1.00
        elif servico == 'ibo':
            preco_pagina = 0.40
        elif servico == 'fot':
            preco_pagina = 0.20

        total = qtd * preco_pagina * (1 - desconto)
        print('Você escolheu {} para {} páginas. Valor do serviço: R${:.2f}'.format(servico, qtd, total))

        return total

# Fim da função num_pagina


# Início da função servico_extra():
def servico_extra() :
    print('--------------------Menu 3 de 3 - Serviços Extras--------------------')
    acumulador = 0
    while True:
        extra = input ('Deseja algum serviço adicional?: \n'
                       '0 - Não desejo serviços extras (encerrar pedido)\n'
                       '1 - Encadernação simples\n'
                       '2 - Encadernação de capa dura\n'
                       '>>')
        if extra == '0':
            return acumulador
        elif extra == '1':
            acumulador = acumulador + 10
        elif extra == '2':
            acumulador = acumulador + 25
        else:
            print('Por favor, escolha uma opção válida (0, 1 ou 2).')

# Fim da função servico_extra

# Programa principal
print('Bem Vindos a Papelaria de Felipe Augusto Fialho')
servico = escolha_servico()
qtd = num_pagina(servico)
extra = servico_extra()

# Associe o serviço a um valor numérico
valor_servico = 0  # Valor inicial, pode ser ajustado conforme necessário
if servico == 'dig':
    valor_servico = 0.10
elif servico == 'ico':
    valor_servico = 1.00
elif servico == 'ibo':
    valor_servico = 0.40
elif servico == 'fot':
    valor_servico = 0.20

total = valor_servico * qtd + extra
print('Valor do serviço por página: R${:.2f}, serviço extra: {}, Total a pagar: R${:.2f}'.format(valor_servico, extra, total))
