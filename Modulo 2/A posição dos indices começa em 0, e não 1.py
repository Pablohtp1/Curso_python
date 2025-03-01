# Python considera que o primeiro item de uma lista está na posição 0, não na posição 1. Isso é conhecido como indexação de base zero.
# Isso é valido para a maioria das linguagens de programção, e o motivo tem a ver com o modo como as operações em lista são implementadas em um nivel mais baixo.
# Se estiver recebendo resultados inesperados, verifique se você está conectando um erro simples de deslocamento de um.
# O segundo item de uma lista te índice igual a 1. Usando esse sistema simples de contagem, podemos obter qualquer elemento que quisermos de uma lista subtraindo um de sua posição na lista.
# Por exemplo, para acessar o quarto item de nossa lista de bicicletas, usamos o indice 3:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles[1].title())
# Esse código devolve a segunda e a quarta bicicletas da lista: Cannondale e Specialized.
# Python tem uma sintaxe especial para acessar o último elemento de uma lista. Ao solicitar o item no indice -1, Python sempre deovlve o último item da lista.

print (bicycles[-1].title())

#print (bicycles[-1].title()) Esse código devolve o valor 'Specialized', que é o último item da lista. Essa sintaxe é bem útil, pois, com frequência, você vai querer acessar os últimos itens da lista sem saber exatamente o tamanho dela.
# Essa convenção também se estende a outros valores negativos de indice. O indice -2 devolve o penúltimo item da lista, o indice -3 devolve o antepenúltimo item e assim por diante.