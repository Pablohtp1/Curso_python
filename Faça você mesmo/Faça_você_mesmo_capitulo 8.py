# Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene esses nomes dessa pizzas,e então utilize um laço "for" para exibir o nome de cada pizza.

Pizza = ['da casa', 'frango com catupiry', 'calabresa']

# º Modifique seu laço 'for' para mostrar uma frase usando o nome da pizza em vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha na saida contendo uma frase simples como " Gosto de pizza sabor"

for pizza in Pizza:
    print("Gosto de pizza sabor", pizza)

# º Acrescente uma linha no final de seu programa, fora do laço "for", que informe quanto você gosta de pizza. A saida deve ser constituida de três ou mais linhas sobre os tipos de pizza que você gosta e de uma frase adicional, por exemplo, "Eu realmente adoro pizza!".

print("Eu realmente adoro!", pizza[1].title())


# Animais: Pense em pelo menos três tipos de animais diferentes. Armazene os nomes desses animais em uma lista e então, utilize um laço 'for' para exibir o nome de cada animal.

Animais = ['cachorro', 'gato', 'papagaio']

# º Modifique seu programa para exibir uma frase sobre cada animal, por exemplo, "Um cachorro seria um ótimo animal de estimação".

for animal in Animais:
    print("Um", animal, "seria um ótimo animal de estimação")

# º Acrescente uma linha no final de seu programa que informe o que esses animais tem em comum. Você poderia exibir uma frase como "Qualquer um desses animais seria um ótimo animal de estima

print("Qualquer um desses" , animal, "seria um ótimo animal de estimação")
