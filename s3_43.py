nome = str(input('Digite seu primeiro nome: '))
encontrar = str(input('Digite o que você deseja encontrar: '))
if encontrar in nome:
    print('{} está em {}!'.format(nome, encontrar))
else:
    print('{} não está em {}'.format(nome, encontrar))
    
    
    
