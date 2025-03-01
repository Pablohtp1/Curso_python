# Para preservar a ordem original de uma lista, mas apresentá-la de forma ordenada, podemos usar a função sorted(). A função sorted() permite exibir sua lista.
# Em uma ordem em particular, mas não afeta a ordem propriamente dita da lista.
# Vamos testar essa função na lista de carros:

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Aqui está a lista original:")
print(cars)

print('\nhere is the sorted list') 
print(sorted(cars))
print("\nAqui está a lista original novamente:") 
print(cars)

# Inicialmente, exibimos a lista em sua ordem original em 1 e depois em ordem alfabética em 2. Depois que a lista é exibida na nova ordem,
# Mostramos que a lista continua armazenada em sua ordem original em 3. 

# Here is the original list:
#ist ['bmw', 'audi', 'toyota', 'subaru']

# Here is the sorted list:
#ist ['audi', 'bmw', 'subaru', 'toyota']

# Here is the original list again:
#ist ['bmw', 'audi', 'toyota', 'subaru']

# Observe que a lista é exibida em ordem alfabética, mas quando exibimos a lista original, ela ainda está armazenada na ordem original.

# NOTA: Ordena uma lista em ordem alfabética é um pouco mais complicado quando todos os valores não utilizam letras minúsculas.
# Há varias maneiras de interpretar letras maiúsculas quando decidimos por uma sequência maior que aquele com que queremos lidar no momento.
# No entanto, a maior parte das abordagens á ordenação terá diretamente como base o que aprendemos nesta seção.
