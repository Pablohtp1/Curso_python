# Se quiser criar uma lista de números, você pode converter os resultados de range() 
# diretamente em uma lista usando a função list(). A saida será uma lista de números.
# No exemplo da seção anterior, simplesmente exibimos uma série de números. Podemos usar list() para converter esse mesmo conjunto de números em uma lista:

numbers = list(range(1,6))
print (numbers)

# Também podemos usar a função range() para dizer a Python que ignore alguns números em um dados. Por exemplo, eis o modo de listar os números pares entre 1 e 10: 

even_numbers = list(range(2,11,2))
print(even_numbers)

# Nesse exemplo, a função range() começa com o valor 2 e então soma 2 a esse valor. O valor 2 é somado repetidamente até o valor final, que é 11. Ser alcançado ou ultrapasado, e o resultado a seguir é gerado: [2, 4, 6, 8, 10].

# Podemos criar praticamente qualquer conjunto de números que quisermos com a função range(). Por exemplo, considere como criaríamos uma lista dos dez primeiros quadrados perfeitos (Isto é, o quadrado de cada inteiro de 1 a 10). Em Python, dois asteriscos (**) representam exponenciais. Eis o modo como podemos colocar as dez primeiros quadrados perfeitos em uma lista:

squares = []
for value in range(1,10):
    square = value**6
    squares.append(square)
print(squares)

# Começamos com uma lista vazia chamada squares em 1. em 2 dizemos a Python para percorrer cada valor de 1 a 10 usando a função range(). No laço, o valor atual é elevado ao quadrado e armazenado na variável square em 1. Em 4, cada novo valor de square é concatenado á lista squares. Por fim, quando o laço acaba de executar, a lista de quadrados é exibida em 4: [1, 64, 729, 4096, 15625, 46656, 117649, 262144, 531441].

# Para escrever esse código de modo mais conciso, omita a variável temporária square e concatene cada novo valor diretamente na lista:

square = []

for value in range(1,11):
    squares.append(value**2)
    print(squares)

# O código em 1 faz a mesma tarefa executada pelas linhas 1 e 4 em "SQUARES". Cada valor do laço é eleveado ao quadrado e, então, é imediatamente concatenado á lista de quadrados.

# Você pode usar qualquer uma dessas duas abordagens quando criar uma lista mais complexas, Ás vezes, usar uma variável temporária deixa o código mais legível; em outras ocasiões, deixa o código desnecessariamente longo. Concentre-se primeiro em escrever um código que você entenda claramente e faça o que quer que ele faça.
# Em seguida, procure abordagens mais eficientes á medida que revisar o seu código.
