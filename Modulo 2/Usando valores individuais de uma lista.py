# Você pode usar valores individuais de uma lista, exatamente como faria com qualquer outra variável. Por exemplo, podemos usar concatenação para criar uma mensagem com base em um valor de uma lista.
# Vamos tentar obter a primeira bicicleta da lista e compor uma mensagem usando esse valor

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "Minha primeira bicicleta é " + bicycles[0].title() + "."
print (message)

# Em vez de simplesmente imprimir o nome da bicicleta, estamos usando o valor para compor uma mensagem. A saída é uma mensagem que inclui o nome da primeira bicicleta da lista:
