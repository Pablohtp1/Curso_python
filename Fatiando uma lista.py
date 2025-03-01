# Para criar uma fatia, especifique o índice do primeiro e do último elemento com os quais você quer trabalhar. Como ocorre na função range(), Python para em um item antes do segundo índice que você especificar.
# Para exibir os três primeiros elementos de uma lista, solicite os índices de 0 a 3; os elementos 0,1 e 2 serão devolvidos.

# O exemplo a seguir envolve uma lista de jogadores de um time: 

players = ['charles', 'martina', 'michael', 'florence', 'eli' ,' maria', 'Pedro']
print(players[0:3])

# O código exibe uma fatia dessa lista, que inclui apenas os três primeiros jogadores. A saida mantém a estrutura de lista e inclui o três primeiros jogaodres: ['charles', 'martina', 'michael'].

# Você pode gerar qualquer subconjunto de uma lista. Por exemplo, se quiser o segundo, o terceiro e o quarto itens de uma lista, comece a fatia no índice 1 e termine no indice 4: 

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'maria', 'Pedro']
print(players[1:4])

# Dessa vez, a fatia começam com 'martina' e termina com 'florence': ['martina', 'michael', 'florence'].

# Se o primeiro índice de uma fatia for omitido, Python começará sua fatia automaticamente no início da lista: players = ['charles', 'martina', 'michael', 'florence', 'eli', 'maria', 'Pedro']

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'maria', 'Pedro']
print(players[:4])

# Uma sintaxe semelhante funcionará se vocÊ quiser uma fatia que inclua o final de uma lista. Por exemplo, se quiser todos os itens do terceiro até o último item, podemos começar com o índice 2 e omitir o segundo índice: 

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'maria', 'Pedro']
print(players[2:])

# Python devolve todos os itens, do terceiro item até o final da lista: ['michael', 'florence', 'eli', 'maria', 'Pedro'].

# Essa sintaxe permite apresentar todos os elementos a partir de qualquer ponto de sua lista até o final, independentemente do tamanho da lista. Lembre-se de que um índice negativo devolve um elemento a uma determinada distância do final de uma lista.

# Por exemplo, se quisermos apresentar os três últimos jogadores da lista, podemos usar a fatia:

player = ['charles', 'martina', 'michael', 'florence', 'eli', 'maria', 'Pedro']
print(players[-3:])

# Esse código exibe os nomes dos três últimos jogadores e continuaria a funcionar à medida que a lista de jogadores mudar de tamanho.

