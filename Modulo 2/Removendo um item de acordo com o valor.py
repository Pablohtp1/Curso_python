# Ás vezes, vocÊ não saberá a posição do valor que quer remover de uma lista. Se conhecer apenas o valor do item que deseja remover, o metódo remove() poderá ser usado.
# Por exemplo, vamos remover o valor 'ducati' da lista de motocicletas:

motorcycles = ['honda', 'suzuki', 'yamaha', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


# O código em 1 diz a Python para descobrir em qual lugar 'ducati' aparece na lista e remover esse elemento: ['honda', 'suzuki', 'yamaha', 'ducati'].

# Também podemos usar o método remove() para trabalhar com um valor que está sendo removido de uma lista. Vamos remover o valor 'ducati' e exibir um motivo para removê-lo da lista.

motorcycles = ['honda', 'suzuki', 'yamaha', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print  (f"\nA {too_expensive.title()} é muito cara para mim.")

# Apos definir a lista em 1, armazenamos o valor 'ducati' em uma variável chamada too_expensive. Então utilizaremos essa variável para dizer a Python qual valor deve ser removido da lista em 1. Em 4 'ducati' é removido da lista e, em 5, exibimos uma mensagem que explica o motivo da remoção. A saida é uma frase simples que explica que a Ducati é muito cara para o autor.

#NOTA: O método remove() apaga apenas a primeira ocorrência do valor que você especificar. Se houver a possibilidade de o valor aparecer mais de uma vez na lista, será necessário usar um laço para determinar se todas as ocorrências desse valor foram removidas.
# Aprenderemos a fazer isso em Laços e listas em Python.
