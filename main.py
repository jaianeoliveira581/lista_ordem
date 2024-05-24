#lista de nomes
nomes = ('Gabi', 'Pai', 'Mãe', 'Matheus', 'Yuri', 'Yngrid', 'Vitinho', 'Jaiane', 'Gui', 'Ia', 'Python', 'Gustavo', 'Almeida', 'Amazon', 'Wallissonl')


nome = input('Digite o nome a ser pesquisado: ').capitalize()

try:
    indice = nomes.index(nome)
    print(f'nome encontrado. (nome) no indice {indice}.')
except:
    print(f'(nome) não encontrado na lista.')

#.upper permite letras M m



