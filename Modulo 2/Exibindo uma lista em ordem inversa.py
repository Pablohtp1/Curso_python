# Para inverter a ordem original de uma lista, podemos usar o método reverse(). Se armazenamos originalmente a lista de carros em ordem cronológica.
# De acordo com a época em que fomos seus proprietários, poderemos facilmente reorganizar a lista em ordem cronológica inversa:

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# Observe que reverse() não reorganiza em ordem alfabética inversa; ele simplesmente inverte a ordem da lista: ['bmw, 'audi', 'toyota', 'subaru'].
# ['subaru', 'toyota', 'audi', 'bmw'].

# O método reverse() muda a ordem de uma lista de forma permanente, mas podemos restaurar a ordem original a qualquer momento aplicando reverse() á mesma lista uma segunda vez.
# Por exemplo, para restaurar a ordem original da lista de carros, basta aplicar reverse() á lista uma terceira vez:
