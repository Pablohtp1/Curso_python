# As vezes, você vai querer usar o valor de um item depois de removê-lo de uma lista. O método pop() remove o item da lista e permite que você trabalhe com ele depois da remoção.
# Por exemplo, talvez você queira obter as posições x e y de um alienigena que acabou de ser atingido para que possa desenhar uma explosão nessa posição.
# Em uma aplicação web, você poderia remover um usuário de uma lista de membros ativos e entao adicioná-lo a uma lista de membros inativos.
# O método pop() é particularmente útil quando você trabalha com listas que armazenam elementos em uma ordem específica.
# O termo pop deriva de pensar em uma lista como se fosse uma pilha de itens e remover um item (fazer um pop) do topo da pilha. Nessa analogia, o topo da pilha corresponde ao final da lista.
# Vamos fazer um pop de uma motocicleta da lista de motocicletas:

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()  # ['honda', 'yamaha']
print(motorcycles)
print(popped_motorcycle)  # suzuki

# Começamos definindo e exibindo a lista motorcycles. em 1, em 2 fazemos pop de um valor da lista e o armazenamos na variável popped_motorcycle.
# Exibimos a lista em 1 para mostrar que um valor foi removido da lista. Então exibimos o valor removido em 4 para provar que ainda temos acesso ao valor removido.
# A saída mostra que o valor 'suzuki' foi removido do final da lista e agora está armazenando na variável popped_motorcycle.
# Como esse método pop() poderia ser útil? Supnha que as motocicletas da lista estejam armazenadas em ordem cronológica, de acordo com a época em que fomos seus proprietários. Se for esse o caso, podemos usar o método pop() para exibir uma afirmação sobre a última motocicleta que compramos:

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Em 1, removemos o último item da lista e o armazenamos na variável last_owned. Em 2, exibimos uma mensagem que inclui a última motocicleta que possuímos.