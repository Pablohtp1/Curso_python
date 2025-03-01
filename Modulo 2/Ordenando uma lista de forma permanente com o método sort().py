# o método sort() de Python faz com que seja relativamente fácil ordenar uma lista. Suponha que temos uma lista de carros e queremos alterar a ordem da lista para armazenar os itens em ordem alfabética.
# Para simplificar essa tarefa, vamos supor que todos os valores da lista usam letras minúsculas. Aqui está como podemos ordenar a lista:

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# O método sort() mostrando em 1 altera a ordem da lista de forma permanente. Os carros agora estão em ordem alfabética e não podemos mais retornar á ordem original.

['audi', 'bmw', 'subaru', 'toyota']

# Também podemos ordenar essa lista em ordem alfabética inversa passando o argumento reverse=True para o método sort().
# O exemplo a seguir ordena a lista de carros em ordem alfabética inversa: 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Novamente, a ordem da lista foi permanentemente alterada: ['toyota', 'subaru', 'bmw', 'audi'].

