altura = float(input(' Qual é a altura da parede '))
largura = float(input(' Qual é a largura da parede '))
area = altura * largura

print('Altura da parede é {} metros a largura è {} metros , a area é {} metros'.format(altura, largura, area))
print('Precisa de {:.1f} litros para pintar essa parede'.format(area/2))
