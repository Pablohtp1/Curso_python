## Com frequência, você vai querer começar com uma lista existente e criar uma lista 
## totalmente nova com a base na primeira. Vamos explorar o modo de copiar 
## uma lista e analisar uma situação em que copiar uma lista é útil.
# Vamos explorar o modo de copiar uma lista e analisar uma situação em que copiar uma lista é útil.
# Para copiar uma lista, podemos criar uma fatia que inclua a lista original inteira omitindo o primeiro e o segundo indice ([:]) isso diz a Python para criar uma lista que começa no primeiro item e termina no último, gerando uma cópia da lista toda.
# Por exemplo, suponha que temos uma lista de nossos alimentos prediletos e queremos criar uma lista separada de comidas que um amigo gosta. Esse amigo gosta de tudo que está em nossa lista até agora, portanto podemos criar sua lista copiando a nossa.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Em 1 criamos uma lista de alimentos de que gostamos e a chamamos de my_foods.
# Em 2 ciramos uma nova lista chamada friend_foods.
# Fizemos uma cópia de my_foods solicitando uma fatia de my_foods sem especificar qualquer indice e armazenamos a cópia em friend_foods. Quando exibimos cada lista, vemos que as duas contém os mesmo alimentos: My favorite foods are: ['pizza', 'falafel', 'carrot cake'] My friend's favorite foods are: ['pizza', 'falafel', 'carrot cake'].

# Para provar que realmente temos duas listas separadas, acrescentaremos um alimento em cada lista e mostraremos que cada lista mantém um registro apropriado das comidas favoritas de cada pessoa:

my_foods = ['pizza', 'falafel', 'carrot_cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print("\nMy friend's favorite foods are:")
print(friend_foods)
print(my_foods)

# Em 1, copiamos os itens originais em my_foods para a nova lista friend_foods, como fizemos no exemplo anterior. Em seguida, adicionamos um novo alimento em cada lista: em 2, acrescentamos 'cannoli' a my_foods e em 3, adicionamos 'ice cream' em friend_foods. Em seguida, exibimos as duas listas para ver se cada um desses alimentos está na lista apropriado.

# My favorite foods are: ['pizza', 'falafel', 'carrot cake', 'cannoli']
