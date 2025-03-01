# Contando até vinto: Use um laço "for" para exibir os números de 1 a 20, inclusive.
"""# Um milhão: Crie uma lista de números de um a um milhão e, então, use um laço "for" para exibir os números. ( Se a saida estiver demorando demais, interrompa pressionando CTRL-C ou feche a janela de saida)"""
"""# Somando um milhão: Crie uma lista de números um a milhão e, em seguida, use min() e max() para garantir que usa lista realmente começa em um e termina em um milhão. Alem disso, utilize a função sum() para ver a rapidez com que Python é capaz de somar um milhão de números. """
"""# Números ímpares: Use o terceiro argumento da função range() para criar uma lista de números impares de 1 a 20. Utilize um laço "for" para exibir todos os números."""
"""# Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use o laço "for" para exibir os números de sua lista."""
"""# Cubos: Um número elevado à terceira potência é chamada de cubo. Por exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10) e utilize um laço "for" para exibir o valor de cada cubo."""
"""# Comprehension: Use uma list comprehension para gerar uma lista dos dez primeiros cubos."""
# Resolução:

# Um milhão: 

list = [value for value in range(1,1000001)]


# Somando um milhão:

print(min(list))
print(max(list))
print(sum(list))

# Números ímpares:

list = [value for value in range(1,21,2)]
print(list)

# Três:

list = [value for value in range (3,31,30)]
print(list)

# Cubos:

list = [value ** 3 for value in range(1,11)]
print(list)

# Comprehension:

list = [value ** 3 for value in range(1,11)]
print(list)
