#Nomes: Armaezene os nomes de alguns de sesus amigos em uma lista chamada names. Exiba o nome d cada pessoa acessando cada elemento da lista, um de cada vez:

names = ['Pablo', 'Pedro', 'Robinho', 'Fabio',]
print (names)

#Saudações: Comece com a lista usando no exercicio acima, mas em vez de simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas. O Texto de cada mensagem deve ser a mesma, porém cada mensagem deve estar personalizada com o nome da pessoa.

message = "Olá\t" + names[-1].title() + "\tvocê é um cara muito legal"
print(message)

# Sua própria lista: Pense em seu meio de transporte preferido, como motocicleta ou carro e crie uma lista que armazene vários exemplos. Utilize sua lista para exibir uma série de frases sobre esses itens, como "Gostaria de ter uma moto Honda".

transportes = ['moto', 'carro', 'bicicleta', 'caminhão', 'Pablo']
name = 'Pablo '
Pablo = name + "Gostaria de ter uma " + transportes[0].title() + "\tHonda"
print(Pablo)   
