                       #MENU TELA INICIAL
print('Bem vindo a Sorveteria de Felipe Augusto Fialho!!')
print('---------------MENU---------------')
print('Produto|----|Tamanho|------|Valor|')
print('Açai----------P----------R$ 12,00')
print('Cupuaçu-------P----------R$ 10,00')
print('Açai----------M----------R$ 17,00')
print('Cupuaçu-------M----------R$ 15,00')
print('Açai----------G----------R$ 21,00')
print('Cupuaçu-------G----------R$ 29,00')
print('CP = cupuaçu | AC= açai')

#ACUMULADOR
acumulador = 0


while True:
        # OPÇÃO DE TAMANHO
        tamanho = input('Entre com o tamanho do sorvete(P/M/G):')
        tamanho = tamanho.upper()


        if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
                print('Tamanho Inválido!Tente novamente!(P, M ou G ) ')
                continue                # se o usuario digitar algo invalido volta para o começo do while

                        # OPÇÃO DE SABORES

        sabor = input('Entre com o sabor do sorvete(AC ou CP):')
        sabor = sabor.upper()
        if sabor != 'AC' and sabor != 'ac' and sabor != 'CP' and sabor != 'cp':
                print('Sabor Invalido!Tente novamente!(AC ou CP) ')
                continue                # se o usuario digitar algo invalido volta para o começo do while


                # PEDIDOS AÇAI

        elif sabor == 'AC' and (tamanho == 'P'):
                print('voce escolheu açai tamanho P ')
                acumulador = acumulador + 12                    # pegue o valor que tinha no acumulador e some com 12

        elif sabor == 'AC' and tamanho == 'M':
                print('voce escolheu açai tamanho M')
                acumulador = acumulador + 17                     # pegue o valor que tinha no acumulador e some com 17

        elif sabor == 'AC' and tamanho == 'G':
                print('voce escolheu açai tamanho G')
                acumulador = acumulador + 21                    # pegue o valor que tinha no acumulador e some com 21

                # PEDIDOS CUPUAÇU

        elif sabor == 'CP' and tamanho == 'P':
                print('voce escolheu cupuaçu tamanho P')
                acumulador = acumulador + 10                    # pegue o valor que tinha no acumulador e some com 10

        elif sabor == 'CP' and tamanho == 'M':
                print('voce escolheu cupuaçu tamanho M ')
                acumulador = acumulador + 15                    # pegue o valor que tinha no acumulador e some com 15

        elif sabor == 'CP' and tamanho == 'G':
                print('voce escolheu cupuaçu tamanho G ')
                acumulador = acumulador + 29                    # pegue o valor que tinha no acumulador e some com 29



                # SE DESEJAR MAIS PEDIDOS,VOLTA AO COMEÇO DO WHILE,SE NAO, O PROGRAMA REALIZA O BREAK COM VALOR TOTAL

        adicionais = input(
                'Deseja pedir mais algum sorvete? (S para sim ou digite outra tecla para finalizar seu pedido!):')
        adicionais = adicionais.upper()
        if adicionais == 'S':
                continue
        else:
                print('o valor total é de de :R${}'.format(acumulador))
                break
