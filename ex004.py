d = input('digite algo: ')
print('esse e alfanumerico', d.isalpha())
print('esse e numerico ', d.isnumeric())
print('esse  e maiusculo', d.isupper())
print('tem so espacos; ', d.isspace())

print('esse e alfanumerico {}'.format(d.isnumeric()))