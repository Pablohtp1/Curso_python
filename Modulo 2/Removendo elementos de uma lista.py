# Com frequência, você vai querer remover um item ou um conjunto de itens uma lista. Por exemplo, quando um jogador atirar em um alienigena, você provavelmente vai querer remover o alienigena da lista de alienigenas.
# Se um usuario decide cancelar a conta em sua aplicação web, você vai querer remover esse usuário da lista de usuários ativos. Você pode remover um item de acordo com sua posição na lista ou seu valor.

# Removendo um item usando a instrução del
# Se a posição do item que você quer remover de uma lista for conhecida, a instrução del poderá ser usada.
# Veja um exemplo de como remover um item de uma lista de motocicletas:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)  # ['yamaha', 'suzuki']

#O código em 1 usa del para remover um itme de qualquer posição em uma lista usando a instrução del, se souber qual é seu indice.
# Por exemplo, eis o modo de remover o segundo item, 'yamaha', da lista:
motorcycles = ['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']

# VocÊ pode remover um item de qualquer posição em uma lista usando a instrução del, se souber qual é o seu indice. Por exemplo, eis o modo de remover o segundo item, 'yamaha', da lista:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)  # ['honda', 'suzuki']

# Nós dois exemplos não podemos mais acessar o valor que foi removido da lista após a instrução del ter sido usada.