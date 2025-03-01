# A abordagem descrita antes para gerar a lista "SQUARES" usou três ou quatro linhas de código. Uma "LIST COMPREHENSION" ( Abrangência de lista) permite gerar essa mesma lista com apenas uma linha de código.
# Uma list comprehension combina o laço "for" e a criação de novos elementos em uma linha, e concatena cada novo elemento automaticamente.
# As "list comprehensions" nem sempre são apresentadas ao iniciantes, mas eu as inclui aqui porque é bem provavél que você veja assim que começar a analisar códigos de outras pessoas.

# O exemplo a seguir cria a mesma lista de quadrados perfeitos que vimos antes, porém utiliza uma "list comprehension"

square = [value**2 for value in range(1,11)]
print(square)

# Para usar a sintaxe, comece com um nome descritivo para a lista, por exemplo, squares. Em seguida, insira um colchete de abertura e defina a expressão para os valores que você quer armazenar na nova lista.
# Nesse exemplo, a expressão é value**2, que eleva o valor ao quadrado. Então escreva um laço "for" para gerar os números que você quer fornecer á expressão e insira um colchete de fechamento. O laço "for" nesse exemplo é "for value in range(1,11), que fornece os valores de 1 a 10 á expressão value**2. Observe que não usamos dois-pontos no final da instrução "FOR"

# O resultado é a mesma lista de valores ao quadrado antes: [1, 4, 9, 16 [...], 100]

# Escrever suas próprias "LIST COMPREHENSIONS" exige um pouco de prática, mas você vera que vale a pena conhecê-las depois que se sentir à vontade para criar listas comnuns.
# Quando escrever três ou quatro linhas de código para gerar listas e isso começar a parecer repetitivo, considere escrever suas próprias list comprehensions.

# Exercícios
