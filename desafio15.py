dias = int(input(' Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
dias = dias * 60
valkm = Km * 0.15
print('O total a pagar é de {}'.format(dias + valkm))
