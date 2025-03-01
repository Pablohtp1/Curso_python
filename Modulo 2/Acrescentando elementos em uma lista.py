# Você pode acrescentar um novo elemento em uma lista por diversos motivos. Por exemplo, talvez você queira que novos alienigenas aparecam no jogo.
# Pode querer acrescentar novos dados em uma visualização ou adicionar novos usuários registrados em um site que você criou.
# Python oferece várias maneiras de acrescentar novos dados em listas existentes.

# Concatenando elementos no final de uma lista

# A maneira mais simples de acrescentar um novo elemento em uma lista é concatenar o item na lista.
# Quando concatenamos um item em uma lista, o novo elemento é acrescentando no final. Usando a mesma lista que tinhamos no exemplo anterior.
# Adicionaremos o novo elemento 'ducati' no final da lista: 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)  # ['honda', 'yamaha', 'suzuki', 'ducati']

# O método append() em acrescentar 'ducati' no final da lista sem afetar qualquer outro elemento: ['honda', 'yamaha', 'suzuki', 'ducati'].
# O método append() facilita a construção de listas dinâmicas. Por exemplo, você pode começar com uma lista vazia e, então, acrescentar itens a lista usando uma série de instruções append().
# Usaremos uma lista vazia e acrescentaremos os itens 'honda', 'yamaha' e 'suzuki' a lista:

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']

# Criar listas dessa maneira é bem comum, pois, com frequência, você não conhecerá os dados que seus usuários querem armazenar em um programa até que ele esteja executando.
# Para deixar que seus usuários tenham o controle, comece definindo uma lista vazia que armazenará os valores dos usuários.
# Em seguida, concatene cada novo valor fornecido á lista que vocÊ acabou de criar.

# Inserindo elementos em uma lista
# Você pode adicionar um novo elemento em qualquer posição de uma lista usando o método insert(). Para isso, você especifica o índice do novo elemento e o valor do novo item.

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)  # ['ducati', 'honda', 'yamaha', 'suzuki']

# Nesse exemplo, o código em 0 insere o valor 'ducati' no inicio da lista. O método insert() abre um espaço na posição 0 e armazena o valor 'ducati' no inicio da lista
# Essa operação desloca todos os demais valores da lista uma posição á direita:

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(1, 'ducati') # ['honda', 'ducati', 'yamaha', 'suzuki']

print(motorcycles)