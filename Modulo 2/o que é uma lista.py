# Uma lista é uma coleção de itens em uma ordem em particular. Podemos criar uma lista que inclua as letras do alfabeto, os digitos de 0 a 9 ou os nomes de todas as pessoas de sua família.
# Você pode colocar qualquer informação que quiser em uma lista e os itens de sua lista não precisam estar relacionados de nenhuma maneira em particular.
# Como uma lista geralmente contém mais de um elemento, é uma boa prática usar um nome no plural para a lista, como letras, digitos ou nomes. (Sempre bom deixar em plural) para informar que a variável é uma lista.
# Em Python, colchetes ([]) indicam uma lista e os elementos individuais da lista são separados por virgulas. Vamos dar uma olhada em uma lista simples que contém alguns tipos de bicicletas:


name = 'Pablo'
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] + [name]
print (bicycles)

# Se você pedir a Python que exiba uma lista, ela devolverá a representação da lista, incluindo os colchetes: ['trek', 'cannondale', 'redline', 'specialized']

# Como essa não é a saida que você quer seus usúarios vejam, vamos aprender a acessar os elementos individuais de uma lista.