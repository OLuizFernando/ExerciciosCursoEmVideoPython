nm = str(input('Digite seu nome completo: '))
nome = nm.strip()
print('Seu nome com todas as letras maiúsculas:', nome.upper())
print('Seu nome com todas as letras minúsculas:', nome.lower())
nomesplit = nome.split()
lensplit = len(nomesplit)
len1 = len(nomesplit[0])
len = len(nome.replace(' ', ''))
print('Quantidade de letras:', len)
print('Quantidade de letras do primeiro nome:', len1)