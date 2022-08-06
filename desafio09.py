tab = int(input(' Digite um numero para mostra a usa tabuada '))
aux = 0
 
print('o valor da tabuda sera mostra abaixo; ')
print( '-' * 18)
print('tabuda de {}'.format(tab))
print('-' * 18)

while( aux <= 10):
    print('{} X {} = {}'.format(aux, tab, (aux*tab)))
    aux = aux + 1
