# A sintaxe para modificar um elemento é semelhante á sintaxe para acessar um elemento de uma lista.
# Para alterar um elemento, use o nome da lista seguido do índice do elemento que você quer modificar e, então,  forneça o novo valor que vocÊ quer que esse item tenha.
# Por exemplo, vamos supor que temos uma lista de motocicletas, e que o primeiro item da lista seja 'honda'. Como mudariamos o valor desse primeiro item?

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# O código em 1 define original, com 'honda' como o primeiro elemento. O codigo em 2 altera o valor do primeiro item para 'ducati'.
# A saida mostra que o primeiro item realmente foi modificado e o restante da lista permaneceu igual: ['honda','yamaha','suzuki'] -> ['ducati','yamaha','suzuki'].
# Você pode mudar o valor de qualquer item de uma lista, e não apenas o primeiro.
