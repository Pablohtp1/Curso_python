# Listas são coleções ordenadas, portanto você pode acessar qualquer elemento de uma lista informando a posição - ou indice - do item desejado ao interpretador Python.
# Para acessar um elemento em uma lista, escreva o nome da lista seguido do indice do item entre colchetes.
# Por exemplo, vamos exibir a primeira bicicleta de nossa lista de bicicletas:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# Esse é o resultado que você quer que seus usuários vejam. Uma saida limpa e organizada que exibe o nome da primeira bicicleta da lista.
# Também podemos usar o método de string do Capitulo 2 em qualquer elemento de uma lista. Por exemplo, podemos formatar o elemento 'trek' de modo mais bonito usando o método title():
# print(bicycles[0].title()) esse exemplo gera a mesma siada do exemplo anterior, exceto pelo fato de 'Trek' começar com uma letra maiúscula.