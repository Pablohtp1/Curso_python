# Na verdade, você pode usar pop () para remover um item de qualquer posição em uma lista se incluir o índice do item que vocÊ deseja remover entre parênteses.

# Considere a lista de motocicletas novamente e vamos remover o segundo item da lista, que é 'suzuki':

motorcycles0 = ['honda', 'suzuki', 'yamaha']
print(motorcycles0)
first_owned = motorcycles0.pop(0)
print (f"Primeira motocicleta do nosso site {first_owned.title()}.")

motorcycles1 = ['honda', 'suzuki', 'yamaha']
print(motorcycles1)
first_owned = motorcycles1.pop(1)
print (f"Segunda motocicleta do nosso site {first_owned.title()}.")

motorcycles2 = ['honda', 'suzuki', 'yamaha']
print(motorcycles2)
first_owned = motorcycles2.pop(2)
print (f"Terceira motocicleta do nosso site {first_owned.title()}.")


# começamos fazendo uma pop da primeira motocicleta da lista em 1 e, então, exibimos uma mensagem sobre essa motocicleta em 2. A saida é uma frase simples.