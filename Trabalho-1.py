                                            # TELA DE BOAS VINDAS
print('--------------------------------------------')
print('Bem vindo a loja de Felipe Augusto Fialho!\n')
print('--------------------------------------------')


            #VARIAVEIS

produto = float(input('Digite o valor do produto R$:'))
qtd = int(input('Digite a quantidade do produto:'))
per = 0                                       #percentual de desconto

                        #S/DESCONTO
if qtd < 1000:
    des=0.00
                        #3% DESCONTO
elif (qtd >= 1000) and (qtd < 3000):
    per=3
    des=(produto*per* qtd) // 100
                         #5%DESCONTO

elif (qtd >= 3000) and (qtd < 5000):
    per=5
    des = (produto * per * qtd) // 100
                     #8%DESCONTO
else:
    qtd >= 5000
    per=8
    des = (produto * qtd * per ) // 100

                         #CALCULO SOMATÓRIO

total_bruto= (produto*qtd)
                      #CALCULO COM DESCONTO

total_des= (produto*qtd)-des

            #PRINT's Finais,com valor bruto desconto,e total a pagar.

print('valor total bruto é de R$ {}'.format(total_bruto))
print('desconto de {}%,({} R$)'.format (per,des))
print( 'valor total com desconto é de R$ {}'.format(total_des,per,des))
